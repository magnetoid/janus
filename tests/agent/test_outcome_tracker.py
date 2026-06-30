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


# --- tool-failure reward penalty (Increment 3.1) ----------------------------

def test_tool_failure_rate_counts_error_results():
    snap = [
        {"role": "user", "content": "go"},
        {"role": "tool", "content": '{"error": "boom"}'},
        {"role": "tool", "content": '{"error": "again"}'},
        {"role": "tool", "content": '{"error": "thrice"}'},
        {"role": "tool", "content": '{"error": "four"}'},
        {"role": "tool", "content": '{"ok": true}'},
    ]
    assert ot.tool_failure_rate(snap) == 0.8                                  # 4 of 5
    assert ot.tool_failure_rate([{"role": "tool", "content": '{"ok": 1}'}]) == 0.0
    assert ot.tool_failure_rate([]) == 0.0                                    # no tool results


def test_reward_penalised_by_tool_failures():
    clean = ot.record_outcome("s1", True, skills=["x"], tool_failure_rate=0.0)
    noisy = ot.record_outcome("s2", True, skills=["x"], tool_failure_rate=0.8)
    assert clean["reward"] == 1.0
    assert noisy["reward"] < clean["reward"]      # secondary penalty applied
    assert noisy["success"] is True               # primary verdict unchanged
    assert noisy["tool_failure_rate"] == 0.8


def test_skill_reward_trajectory_uses_reward_with_back_compat(monkeypatch):
    ot.record_outcome("s1", True, skills=["deploy"], tool_failure_rate=0.0)   # reward 1.0
    ot.record_outcome("s2", True, skills=["deploy"], tool_failure_rate=1.0)   # reward 0.5
    assert ot.skill_reward_trajectory("deploy") == [1.0, 0.5]
    # a pre-reward record falls back to its boolean success
    recs = ot.load() + [{"session_id": "old", "success": True, "skills": ["deploy"]}]
    monkeypatch.setattr(ot, "load", lambda: recs)
    assert ot.skill_reward_trajectory("deploy")[-1] == 1.0
