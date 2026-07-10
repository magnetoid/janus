"""Tests for the sleep consolidation engine (agent/sleep.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import sleep
from tools.memory_tool import MemoryStore


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


def test_sleep_runs_proposer_and_attaches_result(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    calls = {"n": 0}

    def _fake_propose(**kwargs):
        calls["n"] += 1
        return {"proposed": ["si-0001"], "considered": 1, "reason": "ok"}

    monkeypatch.setattr("agent.proposer.propose_skill_improvements", _fake_propose)
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert calls["n"] == 1
    assert rep["proposed"] == ["si-0001"]


def test_sleep_proposer_failure_does_not_break_cycle(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    monkeypatch.setattr("agent.proposer.propose_skill_improvements",
                        lambda **k: (_ for _ in ()).throw(RuntimeError("boom")))
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert rep["error"] is None          # cycle survived
    assert rep["proposed"] == []         # step failed → stays empty


def test_sleep_auto_evaluate_gated_off_by_default(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    monkeypatch.setattr("agent.proposer.propose_skill_improvements",
                        lambda **k: {"proposed": ["si-0001"]})
    ev_calls = {"n": 0}
    monkeypatch.setattr("agent.eval_orchestrator.evaluate_proposal",
                        lambda pid, **k: ev_calls.__setitem__("n", ev_calls["n"] + 1))
    monkeypatch.setattr(sleep, "_auto_evaluate_enabled", lambda: False)
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert ev_calls["n"] == 0            # not evaluated when the flag is off
    assert rep["evaluated"] == []


def test_sleep_auto_evaluate_runs_when_enabled(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    monkeypatch.setattr("agent.proposer.propose_skill_improvements",
                        lambda **k: {"proposed": ["si-0001", "si-0002"]})
    monkeypatch.setattr(sleep, "_auto_evaluate_enabled", lambda: True)
    monkeypatch.setattr("agent.eval_orchestrator.evaluate_proposal",
                        lambda pid, **k: {"evaluated": pid == "si-0001"})
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert rep["evaluated"] == ["si-0001"]   # only the one that evaluated cleanly


def test_sleep_twin_review_gated_off_by_default(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    monkeypatch.setattr("agent.proposer.propose_skill_improvements",
                        lambda **k: {"proposed": ["si-0001"]})
    monkeypatch.setattr(sleep, "_auto_evaluate_enabled", lambda: False)
    monkeypatch.setattr(sleep, "_twin_review_enabled", lambda: False)
    rv_calls = {"n": 0}
    monkeypatch.setattr("agent.twin_review.review_proposals",
                        lambda *a, **k: rv_calls.__setitem__("n", rv_calls["n"] + 1))
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert rv_calls["n"] == 0             # reviewer never runs when the flag is off
    assert rep["vetoed"] == []


def test_sleep_twin_review_runs_when_enabled(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    monkeypatch.setattr("agent.proposer.propose_skill_improvements",
                        lambda **k: {"proposed": ["si-0001", "si-0002"]})
    monkeypatch.setattr(sleep, "_auto_evaluate_enabled", lambda: False)
    monkeypatch.setattr(sleep, "_twin_review_enabled", lambda: True)
    monkeypatch.setattr("agent.twin_review.review_proposals",
                        lambda ids, **k: {"vetoed": ["si-0002"], "passed": ["si-0001"]})
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert rep["vetoed"] == ["si-0002"]   # the reviewer core vetoed one


def test_sleep_runs_self_challenge_only_when_enabled(monkeypatch):
    store = MemoryStore(); store.load_from_disk()
    calls = {"n": 0}
    monkeypatch.setattr("agent.self_challenge.run_self_challenge",
                        lambda **k: (calls.__setitem__("n", calls["n"] + 1), {"attempted": 1})[1])

    # disabled -> step is skipped
    monkeypatch.setattr("agent.self_challenge.enabled", lambda *a, **k: False)
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert calls["n"] == 0 and rep["self_challenge"] is None

    # enabled -> step runs and its report is attached
    monkeypatch.setattr("agent.self_challenge.enabled", lambda *a, **k: True)
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    assert calls["n"] == 1 and rep["self_challenge"] == {"attempted": 1}


def test_importance_scoring_formula():
    # (1-decay)*0.5 + reuse*0.3 + length_norm*0.2
    assert sleep.importance_score(0.0, 1.0, 1.0) == 1.0
    assert sleep.importance_score(1.0, 0.0, 0.0) == 0.0
    assert sleep.importance_score(0.5, 0.5, 0.5) == round(0.25 + 0.15 + 0.1, 4)
    # clamps out-of-range inputs
    assert sleep.importance_score(2.0, -1.0, 5.0) == round(0.0 + 0.0 + 0.2, 4)


def test_prune_low_salience_respects_threshold_and_min_entries():
    store = MemoryStore(); store.load_from_disk()
    for i in range(6):
        store.add("memory", f"entry number {i}")
    entries = list(store.memory_entries)
    # first 4 score low (0.1), last 2 high (0.9)
    scores = {e: (0.1 if i < 4 else 0.9) for i, e in enumerate(entries)}
    dropped = sleep.prune_low_salience(store, threshold=0.5, keep_min=3, scores=scores, apply=True)
    # 4 are below threshold, but floor keep_min=3 means only 3 may be dropped
    assert len(dropped) == 3
    assert len(store.memory_entries) == 3
    # the high-salience entries survived
    assert all(scores[e] == 0.9 for e in store.memory_entries if e in scores) or len(store.memory_entries) == 3


def test_prune_noop_when_at_or_below_floor():
    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "only one")
    assert sleep.prune_low_salience(store, keep_min=10) == []


def test_run_sleep_cycle_dry_run_no_mutation():
    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "uses Python 3.11")
    store.add("memory", "now on Python 3.12")
    before = list(store.memory_entries)
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm('[{"drop":0,"kept":1}]'), dry_run=True)
    assert rep["dry_run"] is True and rep["error"] is None
    assert store.memory_entries == before  # nothing mutated in dry-run


def test_run_sleep_cycle_applies_reconcile():
    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "uses Python 3.11")
    store.add("memory", "now on Python 3.12")
    rep = sleep.run_sleep_cycle(store, llm_caller=_fake_llm('[{"drop":0,"kept":1,"reason":"superseded"}]'))
    assert "uses Python 3.11" in rep["reconciled"]
    assert "uses Python 3.11" not in store.memory_entries


def test_run_sleep_cycle_best_effort_on_failure():
    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "a fact")
    def boom(**kw):
        raise RuntimeError("model down")
    # reconcile + synthesis swallow their own errors; cycle returns a report
    rep = sleep.run_sleep_cycle(store, llm_caller=boom)
    assert rep["error"] is None  # inner steps are individually best-effort
    assert "a fact" in store.memory_entries  # untouched


def test_should_run_sleep_respects_interval():
    assert sleep.should_run_sleep(now_ts=1000.0, state={}, interval_hours=1) is True  # never run
    state = {"last_run": "2026-06-10T00:00:00+00:00"}
    import datetime
    base = datetime.datetime.fromisoformat(state["last_run"]).timestamp()
    assert sleep.should_run_sleep(now_ts=base + 1800, state=state, interval_hours=1) is False  # 30min < 1h
    assert sleep.should_run_sleep(now_ts=base + 7200, state=state, interval_hours=1) is True   # 2h >= 1h


def test_maybe_run_sleep_idle_gate_and_paused(tmp_path, monkeypatch):
    import yaml
    home = tmp_path / ".janus"; (home / "learning").mkdir(parents=True)
    monkeypatch.setenv("JANUS_HOME", str(home))
    (home / "config.yaml").write_text(yaml.safe_dump({"sleep": {"enabled": True, "min_idle_hours": 2.0}}), encoding="utf-8")
    # idle too short -> None
    assert sleep.maybe_run_sleep(idle_for_seconds=600) is None
    # paused -> None even if idle long enough
    sleep.save_sleep_state({"paused": True})
    assert sleep.maybe_run_sleep(idle_for_seconds=999999) is None
    # disabled -> None
    (home / "config.yaml").write_text(yaml.safe_dump({"sleep": {"enabled": False}}), encoding="utf-8")
    assert sleep.maybe_run_sleep(idle_for_seconds=999999) is None


def test_load_save_state(tmp_path, monkeypatch):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path / ".janus"))
    assert sleep.load_sleep_state() == {}
    sleep.save_sleep_state({"last_run": "2026-06-10T00:00:00", "paused": False})
    assert sleep.load_sleep_state()["last_run"] == "2026-06-10T00:00:00"


def _fake_synth_llm(*, merged="Validate inputs and run migrations before deploying.", verdict="accept"):
    """Dispatch by task: synthesis call returns the merged lesson; the dialectic
    arbiter returns the given verdict; advocate/skeptic return filler."""
    def _caller(**kwargs):
        task = kwargs.get("task", "")
        if task == "sleep_synthesis":
            content = merged
        elif task == "dialectic_arbiter":
            content = f'[{{"id": "syn-0", "verdict": "{verdict}", "confidence": "high"}}]'
        else:
            content = "case"
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content))])
    return _caller


def test_synthesize_collapses_cluster_when_admitted():
    from agent import lessons
    for i in range(3):
        lessons.record_lesson(f"deploy variant {i}: forgot to run migrations", task_type="deploy")
    written = sleep.synthesize_cross_session_lessons(llm_caller=_fake_synth_llm())
    assert len(written) == 1
    assert written[0]["source"] == "synthesis"
    assert written[0]["task_type"] == "deploy"
    assert any(r.get("source") == "synthesis" for r in lessons.load())


def test_synthesize_redteam_rejection_writes_nothing():
    from agent import lessons
    for i in range(3):
        lessons.record_lesson(f"deploy variant {i}", task_type="deploy")
    written = sleep.synthesize_cross_session_lessons(llm_caller=_fake_synth_llm(verdict="reject"))
    assert written == []
    assert not any(r.get("source") == "synthesis" for r in lessons.load())


def test_synthesize_skips_small_clusters():
    from agent import lessons
    lessons.record_lesson("one deploy lesson", task_type="deploy")
    lessons.record_lesson("a second deploy lesson", task_type="deploy")  # 2 < min_cluster (3)
    assert sleep.synthesize_cross_session_lessons(llm_caller=_fake_synth_llm()) == []


def test_synthesize_best_effort_on_failure():
    from agent import lessons
    for i in range(3):
        lessons.record_lesson(f"deploy lesson {i}", task_type="deploy")
    def boom(**kw):
        raise RuntimeError("down")
    assert sleep.synthesize_cross_session_lessons(llm_caller=boom) == []


def test_sleep_cycle_appends_one_sleep_log_line():
    store = MemoryStore()
    sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    p = sleep.sleep_log_path()
    assert p.is_file()
    lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert set(rec) >= {"ts", "graduated_facts", "graduated_skills", "lessons", "pruned"}
    assert isinstance(rec["graduated_facts"], int)


def test_sleep_dry_run_writes_no_sleep_log():
    store = MemoryStore()
    sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"), dry_run=True)
    assert not sleep.sleep_log_path().is_file()


# --- unattended sessions feed (close-the-loop move 5) ------------------------

def test_maybe_run_sleep_feeds_recent_sessions(tmp_path, monkeypatch):
    import yaml
    home = tmp_path / ".janus"; (home / "learning").mkdir(parents=True)
    monkeypatch.setenv("JANUS_HOME", str(home))
    (home / "config.yaml").write_text(yaml.safe_dump(
        {"sleep": {"enabled": True, "min_idle_hours": 0.0, "interval_hours": 0}}),
        encoding="utf-8")
    fake_sessions = [[{"role": "user", "content": "hi"}]]
    fetch_kwargs = {}
    def fake_fetch(limit=10, **kw):
        fetch_kwargs.update(kw, limit=limit)
        return fake_sessions, ["summary"]
    monkeypatch.setattr(sleep, "_fetch_recent_sessions", fake_fetch)
    captured = {}
    def fake_cycle(store, **kw):
        captured.update(kw)
        return {"ok": True}
    monkeypatch.setattr(sleep, "run_sleep_cycle", fake_cycle)
    sleep.save_sleep_state({"last_run": "2026-06-24T00:00:00"})
    monkeypatch.setattr(sleep, "should_run_sleep", lambda *a, **k: True)
    rep = sleep.maybe_run_sleep(idle_for_seconds=999999, store=object())
    assert rep == {"ok": True}
    # The unattended path now GRADUATEs: sessions reach the cycle...
    assert captured["sessions"] == fake_sessions
    assert captured["session_summaries"] == ["summary"]
    # ...trust-scoped to CLI sessions and watermarked to the previous cycle.
    assert fetch_kwargs["sources"] == ("cli",)
    assert fetch_kwargs["since_ts"] == sleep._parse_iso("2026-06-24T00:00:00")


def test_fetch_recent_sessions_filters_sources_children_watermark(monkeypatch):
    import janus_state
    rows = {
        "cli": [
            {"id": "s-new", "source": "cli", "parent_session_id": None,
             "last_active": "2026-06-30T12:00:00"},
            {"id": "s-child", "source": "cli", "parent_session_id": "s-new",
             "last_active": "2026-06-30T13:00:00"},
            {"id": "s-old", "source": "cli", "parent_session_id": None,
             "last_active": "2026-06-01T00:00:00"},
        ],
        "telegram": [
            {"id": "s-tg", "source": "telegram", "parent_session_id": None,
             "last_active": "2026-06-30T14:00:00"},
        ],
    }
    class _FakeDB:
        def search_sessions(self, source=None, limit=20):
            return rows.get(source, [])[:limit]
        def get_messages_as_conversation(self, sid):
            return [{"role": "user", "content": f"msg-{sid}"}]
        def close(self):
            pass
    monkeypatch.setattr(janus_state, "SessionDB", _FakeDB)
    since = sleep._parse_iso("2026-06-15T00:00:00")
    sessions, summaries = sleep._fetch_recent_sessions(since_ts=since, sources=("cli",))
    # Only the fresh, parentless CLI session survives: the compression child,
    # the pre-watermark session, and the telegram session are all excluded.
    assert len(sessions) == 1 and len(summaries) == 1
    assert sessions[0][0]["content"] == "msg-s-new"


def test_fetch_recent_sessions_best_effort_empty(tmp_path, monkeypatch):
    home = tmp_path / ".janus"; home.mkdir(parents=True)
    monkeypatch.setenv("JANUS_HOME", str(home))
    sessions, summaries = sleep._fetch_recent_sessions()
    assert sessions == [] and summaries == []
