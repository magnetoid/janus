"""Tests for opt-in auto-fire session-end mining (agent/auto_mine.py)."""
import pytest

from agent import auto_mine


MESSAGES = [{"role": "user", "content": f"m{i}"} for i in range(8)]


def _write_config(home, **flags):
    import yaml
    cfg = {"memory": {"session_mining": flags.get("memory", False)},
           "skills": {"session_mining": flags.get("skills", False)}}
    (home / "config.yaml").write_text(yaml.safe_dump(cfg), encoding="utf-8")


def test_skips_short_sessions(janus_home_dir):
    _write_config(janus_home_dir, memory=True, skills=True)
    assert auto_mine.maybe_automine(MESSAGES[:3]) is None


def test_noop_when_flags_off(janus_home_dir):
    _write_config(janus_home_dir, memory=False, skills=False)
    assert auto_mine.maybe_automine(MESSAGES) is None


def test_noop_when_no_config(janus_home_dir):
    assert auto_mine.maybe_automine(MESSAGES) is None


def test_runs_miners_when_opted_in(janus_home_dir, monkeypatch):
    _write_config(janus_home_dir, memory=True, skills=True)
    calls = {"memory": 0, "skills": 0}

    def _mem(messages, store, **kw):
        calls["memory"] += 1
        return {"added": {"user": 0, "memory": 0}, "skipped_duplicates": 0, "error": None}

    def _skill(messages, **kw):
        calls["skills"] += 1
        return {"proposals": [], "written": [], "error": None}

    monkeypatch.setattr("agent.memory_miner.mine_session_memory", _mem)
    monkeypatch.setattr("agent.skill_miner.mine_session_skills", _skill)

    # run synchronously for a deterministic assertion
    auto_mine.maybe_automine(MESSAGES, run_in_thread=False)
    assert calls == {"memory": 1, "skills": 1}


def test_only_memory_flag_runs_only_memory(janus_home_dir, monkeypatch):
    _write_config(janus_home_dir, memory=True, skills=False)
    hits = {"memory": 0, "skills": 0}
    monkeypatch.setattr("agent.memory_miner.mine_session_memory",
                        lambda *a, **k: hits.__setitem__("memory", hits["memory"] + 1))
    monkeypatch.setattr("agent.skill_miner.mine_session_skills",
                        lambda *a, **k: hits.__setitem__("skills", hits["skills"] + 1))
    auto_mine.maybe_automine(MESSAGES, run_in_thread=False)
    assert hits["memory"] == 1 and hits["skills"] == 0


def test_governor_frozen_pauses_durable_writes(janus_home_dir, monkeypatch):
    """When the governor is FROZEN, memory + skill mining are paused (gap G7)."""
    _write_config(janus_home_dir, memory=True, skills=True)
    hits = {"memory": 0, "skills": 0}
    monkeypatch.setattr("agent.memory_miner.mine_session_memory",
                        lambda *a, **k: hits.__setitem__("memory", hits["memory"] + 1))
    monkeypatch.setattr("agent.skill_miner.mine_session_skills",
                        lambda *a, **k: hits.__setitem__("skills", hits["skills"] + 1))
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen",
                        lambda: True)
    auto_mine.maybe_automine(MESSAGES, run_in_thread=False)
    assert hits == {"memory": 0, "skills": 0}


@pytest.fixture
def janus_home_dir(tmp_path, monkeypatch):
    home = tmp_path / ".janus"
    home.mkdir()
    monkeypatch.setenv("JANUS_HOME", str(home))
    return home


def test_explicit_session_id_reaches_reconcile(janus_home_dir, monkeypatch):
    """Move 4 plumbing: the agent's session_id (not a per-message field) must
    reach record_outcome so the lesson-efficacy join matches log_recall's key."""
    import yaml
    (janus_home_dir / "config.yaml").write_text(
        yaml.safe_dump({"learning": {"track_outcomes": True}}), encoding="utf-8")
    from agent import lessons
    monkeypatch.setattr(lessons, "_outcome_tracking_on", lambda: True)
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda msgs: True)
    monkeypatch.setattr("agent.outcome_tracker.skills_used_in", lambda msgs: [])
    monkeypatch.setattr("agent.outcome_tracker.tool_failure_rate", lambda msgs: 0.0)

    les = lessons.record_lesson("A threaded lesson.", task_type="x")
    lessons.log_recall("real-sid", [les["id"]])   # keyed on the agent session id
    # messages carry NO per-message session_id — only the explicit arg should work
    auto_mine.maybe_automine(MESSAGES, run_in_thread=False, session_id="real-sid")
    assert {r["id"]: r for r in lessons.load()}[les["id"]]["helpful"] == 1
