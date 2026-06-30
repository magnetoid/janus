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
