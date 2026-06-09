"""The curator candidate list surfaces the outcome (success-rate) signal."""
import pytest

from agent import curator
from agent import outcome_tracker as ot


def test_candidate_list_includes_success_rate(monkeypatch):
    monkeypatch.setattr(
        curator.skill_usage, "agent_created_report",
        lambda: [{"name": "deploy", "state": "active", "use_count": 3, "pinned": False}],
    )
    ot.record_outcome("s1", True, skills=["deploy"])
    ot.record_outcome("s2", False, skills=["deploy"])
    out = curator._render_candidate_list()
    assert "deploy" in out
    assert "success=50%(1/2)" in out


def test_candidate_list_marks_unknown_outcome_na(monkeypatch):
    monkeypatch.setattr(
        curator.skill_usage, "agent_created_report",
        lambda: [{"name": "fresh", "state": "active", "use_count": 0, "pinned": False}],
    )
    out = curator._render_candidate_list()
    assert "success=n/a" in out


def test_candidate_list_survives_missing_outcome_module(monkeypatch):
    monkeypatch.setattr(
        curator.skill_usage, "agent_created_report",
        lambda: [{"name": "x", "state": "active", "use_count": 1, "pinned": False}],
    )
    # Even if outcome stats blow up, the list must still render.
    monkeypatch.setattr("agent.outcome_tracker.skill_stats",
                        lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    out = curator._render_candidate_list()
    assert "x" in out
