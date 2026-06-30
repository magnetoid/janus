"""Tests for the Reflexion write-back lesson store (agent/lessons.py)."""
from types import SimpleNamespace

from agent import lessons


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


def test_record_and_load():
    rec = lessons.record_lesson("Run the test suite before deploying.", task_type="deploy staging")
    assert rec is not None
    assert rec["task_type"] == "deploy-staging"  # slugified
    assert lessons.load()[0]["lesson"].startswith("Run the test suite")


def test_record_dedupes_exact_repeats():
    lessons.record_lesson("Always pin the dependency version.")
    second = lessons.record_lesson("always pin the dependency version.")  # case-insensitive dup
    assert second is None
    assert len(lessons.load()) == 1


def test_empty_lesson_is_ignored():
    assert lessons.record_lesson("   ") is None
    assert lessons.load() == []


def test_recall_ranks_relevant_lesson_first():
    lessons.record_lesson("Check the postgres connection pool size first.", task_type="db-tuning")
    lessons.record_lesson("Use rsync, not scp, for large transfers.", task_type="file-transfer")
    hits = lessons.recall_lessons("how to tune the postgres database")
    assert hits
    assert "postgres" in hits[0]["lesson"]


def test_recall_no_overlap_returns_nothing():
    lessons.record_lesson("Use rsync for large transfers.", task_type="file-transfer")
    assert lessons.recall_lessons("quantum chromodynamics entanglement") == []


def test_recall_empty_query_returns_nothing():
    lessons.record_lesson("Anything at all here.")
    assert lessons.recall_lessons("   ") == []


def test_reflect_on_failure_parses_lesson():
    msgs = [
        {"role": "user", "content": "Deploy the app to staging."},
        {"role": "assistant", "content": "Deploying... it broke because tests were skipped."},
    ]
    llm = _fake_llm('{"task_type": "deploy-staging", "lesson": "Always run tests before deploy."}')
    out = lessons.reflect_on_failure(msgs, llm_caller=llm)
    assert out == {"task_type": "deploy-staging", "lesson": "Always run tests before deploy."}


def test_reflect_handles_no_generalizable_lesson():
    msgs = [
        {"role": "user", "content": "Do the thing."},
        {"role": "assistant", "content": "A flaky network blip, nothing to learn."},
    ]
    out = lessons.reflect_on_failure(msgs, llm_caller=_fake_llm('{"task_type": "", "lesson": ""}'))
    assert out is None


def test_reflect_tolerates_garbage_reply():
    msgs = [{"role": "user", "content": "x"}, {"role": "assistant", "content": "y"}]
    assert lessons.reflect_on_failure(msgs, llm_caller=_fake_llm("not json at all")) is None


def test_format_lessons_for_prompt():
    hits = [{"task_type": "deploy", "lesson": "Run tests first."}]
    block = lessons.format_lessons_for_prompt(hits)
    assert "past mistakes" in block.lower()
    assert "Run tests first." in block
    assert lessons.format_lessons_for_prompt([]) == ""


def test_stats_counts_by_task_type():
    lessons.record_lesson("a lesson here", task_type="deploy")
    lessons.record_lesson("another lesson there", task_type="deploy")
    lessons.record_lesson("a third distinct lesson", task_type="db")
    s = lessons.stats()
    assert s["total"] == 3
    assert s["by_task_type"]["deploy"] == 2
    assert s["by_task_type"]["db"] == 1


def test_max_lessons_cap_keeps_recent(monkeypatch):
    monkeypatch.setattr(lessons, "_MAX_LESSONS", 3)
    for i in range(6):
        lessons.record_lesson(f"lesson number {i} about testing")
    kept = lessons.load()
    assert len(kept) == 3
    assert kept[-1]["lesson"] == "lesson number 5 about testing"  # newest survived


def test_auto_mine_writes_lesson_on_failure(monkeypatch):
    """A classified-failure session flows through auto_mine into a stored lesson."""
    import yaml
    from janus_constants import get_janus_home
    from agent import auto_mine
    from agent import outcome_tracker

    # enable outcome tracking via on-disk config (auto_mine reads config.yaml)
    home = get_janus_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"learning": {"track_outcomes": True, "reflexion": True}}),
        encoding="utf-8",
    )
    # stub the two model-backed steps; the wiring under test is everything between
    monkeypatch.setattr(outcome_tracker, "classify_session", lambda *a, **k: False)
    monkeypatch.setattr(
        lessons, "reflect_on_failure",
        lambda *a, **k: {"task_type": "deploy-staging", "lesson": "Run tests before deploying."},
    )
    msgs = [
        {"role": "user", "content": "Deploy to staging.", "session_id": "sess-1"},
        {"role": "assistant", "content": "ok"},
        {"role": "user", "content": "did it work?"},
        {"role": "assistant", "content": "no, it failed"},
        {"role": "user", "content": "why"},
        {"role": "assistant", "content": "tests were skipped"},
    ]
    auto_mine.maybe_automine(msgs, run_in_thread=False)

    stored = lessons.load()
    assert any("Run tests before deploying." in r["lesson"] for r in stored)


def test_auto_mine_records_live_model_strength_on_success(monkeypatch):
    """A classified-success session attributes the outcome to the model that ran
    it via model_strengths.record(source="live") — the live routing signal [A-PR4]."""
    import yaml
    from janus_constants import get_janus_home
    from agent import auto_mine, outcome_tracker, model_strengths

    home = get_janus_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"learning": {"track_outcomes": True}}), encoding="utf-8")
    monkeypatch.setattr(outcome_tracker, "classify_session", lambda *a, **k: True)
    rec: dict = {}
    monkeypatch.setattr(
        model_strengths, "record",
        lambda *, task, model, source="", score=None, **k: rec.update(
            task=task, model=model, source=source, score=score),
    )
    msgs = [
        {"role": "user", "content": "Build a CSV parser.", "session_id": "sess-2"},
        {"role": "assistant", "content": "ok"},
        {"role": "user", "content": "does it handle quotes?"},
        {"role": "assistant", "content": "yes"},
        {"role": "user", "content": "great"},
        {"role": "assistant", "content": "done"},
    ]
    auto_mine.maybe_automine(msgs, run_in_thread=False, model="anthropic/claude-opus-4-8")
    assert rec.get("source") == "live"
    assert rec.get("model") == "anthropic/claude-opus-4-8"
    assert rec.get("score") == 1.0


# --- recency-weighted recall (Increment 2.1) --------------------------------

def _utc(y=2026, mo=6, d=30):
    from datetime import datetime, timezone
    return datetime(y, mo, d, tzinfo=timezone.utc)


def test_recency_decay_halves_each_half_life():
    from datetime import timedelta
    now = _utc()
    iso = lambda days: (now - timedelta(days=days)).isoformat()
    assert lessons._recency_decay(iso(0), now=now, half_life_days=30) == 1.0
    assert abs(lessons._recency_decay(iso(30), now=now, half_life_days=30) - 0.5) < 1e-9
    assert abs(lessons._recency_decay(iso(60), now=now, half_life_days=30) - 0.25) < 1e-9


def test_recency_decay_safe_defaults():
    now = _utc()
    assert lessons._recency_decay("", now=now) == 1.0                       # no ts
    assert lessons._recency_decay("not-a-date", now=now) == 1.0             # unparseable
    assert lessons._recency_decay("2099-01-01T00:00:00+00:00", now=now) == 1.0  # future
    # half_life 0 disables decay even for an old timestamp
    assert lessons._recency_decay("2020-01-01T00:00:00+00:00", now=now, half_life_days=0) == 1.0


def test_recency_half_life_from_config():
    assert lessons._recency_half_life_days({"learning": {"lessons": {"recency_half_life_days": 7}}}) == 7.0
    assert lessons._recency_half_life_days({}) == 30.0                       # default
    assert lessons._recency_half_life_days({"learning": {"lessons": {"recency_half_life_days": 0}}}) == 0.0


def test_recall_newer_lesson_outranks_equal_overlap_older(monkeypatch):
    from datetime import timedelta
    now = _utc()
    old_ts = (now - timedelta(days=120)).isoformat()
    new_ts = (now - timedelta(days=1)).isoformat()
    # Identical text → identical lexical overlap; only recency differs.
    recs = [
        {"lesson": "tune the postgres connection pool", "task_type": "db", "ts": old_ts},
        {"lesson": "tune the postgres connection pool", "task_type": "db", "ts": new_ts},
    ]
    monkeypatch.setattr(lessons, "load", lambda: recs)
    # Force the lexical path so the assertion is independent of an embedding backend.
    def _no_embed(*a, **k):
        raise RuntimeError("no embeddings in test")
    monkeypatch.setattr("agent.embeddings.hybrid_rerank", _no_embed)

    hits = lessons.recall_lessons("tune postgres pool", now=now, half_life_days=30)
    assert len(hits) == 2
    assert hits[0]["ts"] == new_ts                  # newer wins the tie
    assert hits[0]["score"] > hits[1]["score"]
