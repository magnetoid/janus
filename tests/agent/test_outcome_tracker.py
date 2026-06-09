"""Tests for outcome-based reinforcement (agent/outcome_tracker.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import outcome_tracker as ot


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


def test_record_and_overall_stats():
    ot.record_outcome("s1", True, skills=["deploy", "test"])
    ot.record_outcome("s2", False, skills=["deploy"])
    ot.record_outcome("s3", True, skills=["test"])
    o = ot.overall_stats()
    assert o["sessions"] == 3 and o["successes"] == 2 and o["success_rate"] == 0.667


def test_skill_success_rates():
    ot.record_outcome("s1", True, skills=["deploy"])
    ot.record_outcome("s2", False, skills=["deploy"])
    ot.record_outcome("s3", True, skills=["test"])
    stats = ot.skill_stats()
    assert stats["deploy"] == {"uses": 2, "successes": 1, "success_rate": 0.5}
    assert ot.skill_success_rate("test") == 1.0
    assert ot.skill_success_rate("unknown") is None


def test_recent_success_rate_window():
    for i in range(5):
        ot.record_outcome(f"s{i}", success=(i % 2 == 0))  # T F T F T
    assert ot.recent_success_rate(window=2) == 0.5  # last two: F, T


def test_skills_used_in_from_tool_calls_and_text():
    messages = [
        {"role": "assistant", "tool_calls": [
            {"function": {"name": "skill_view", "arguments": json.dumps({"name": "deploy"})}}]},
        {"role": "assistant", "content": "let me skill_view(name='research') now"},
        {"role": "user", "content": "ok"},
    ]
    assert ot.skills_used_in(messages) == ["deploy", "research"]


def test_classify_success_failure_unclear():
    msgs = [{"role": "user", "content": "do X"}, {"role": "assistant", "content": "done"}]
    assert ot.classify_session(msgs, llm_caller=_fake_llm("SUCCESS")) is True
    assert ot.classify_session(msgs, llm_caller=_fake_llm("FAILURE")) is False
    assert ot.classify_session(msgs, llm_caller=_fake_llm("UNCLEAR")) is None


def test_classify_best_effort_on_failure():
    msgs = [{"role": "user", "content": "x"}, {"role": "assistant", "content": "y"}]
    def boom(**kw):
        raise RuntimeError("down")
    assert ot.classify_session(msgs, llm_caller=boom) is None
