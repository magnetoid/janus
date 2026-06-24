"""Tests for Plan Mode (agent/plan_mode.py)."""
from agent import plan_mode as pm


def test_enabled_default_on_and_gated():
    assert pm.enabled({}) is True
    assert pm.enabled({"plan_mode": {"enabled": False}}) is False


def test_directive_gated():
    assert "plan" in pm.directive({}).lower()
    assert pm.directive({"plan_mode": {"enabled": False}}) == ""


def test_should_plan_hard_only(monkeypatch):
    monkeypatch.setattr("agent.task_complexity.classify_complexity", lambda p, **k: "hard")
    assert pm.should_plan("design and prove a distributed lock", {}) is True
    monkeypatch.setattr("agent.task_complexity.classify_complexity", lambda p, **k: "simple")
    assert pm.should_plan("what time is it", {}) is False


def test_should_plan_forced_overrides_complexity(monkeypatch):
    monkeypatch.setattr("agent.task_complexity.classify_complexity", lambda p, **k: "simple")
    assert pm.should_plan("anything", {}, forced=True) is True


def test_should_plan_disabled_even_when_forced():
    assert pm.should_plan("x", {"plan_mode": {"enabled": False}}, forced=True) is False


def test_force_flag_is_one_shot():
    pm.set_forced("s1")
    assert pm.consume_forced("s1") is True
    assert pm.consume_forced("s1") is False


def test_record_load_clear_plan():
    pm.record_plan("s2", ["  step a ", "step b", "  "])  # blanks dropped/trimmed
    assert pm.load_plan("s2") == ["step a", "step b"]
    assert pm.clear("s2") == 2
    assert pm.load_plan("s2") == []


def test_format_plan():
    out = pm.format_plan(["clone repo", "run tests"])
    assert "1. clone repo" in out and "2. run tests" in out
    assert "go" in out.lower()
    assert pm.format_plan([]) == ""


def test_sessions_isolated():
    pm.record_plan("sA", ["only A"])
    assert pm.load_plan("sB") == []


def test_best_effort_never_raises():
    assert isinstance(pm.directive(None), str)
    assert isinstance(pm.should_plan("", {}), bool)
    assert isinstance(pm.load_plan("nope"), list)
