"""Tests for the reflexion reasoning loop (agent/reflexion.py)."""
from types import SimpleNamespace

import pytest

from agent import reflexion as rx


def test_converges_when_critic_approves_first():
    solver = lambda task, prev, fb: "answer-v1"
    critic = lambda task, attempt: {"ok": True, "critique": ""}
    res = rx.reflect_and_solve("t", solver=solver, critic=critic, max_iterations=3)
    assert res["converged"] is True and res["iterations"] == 1 and res["answer"] == "answer-v1"


def test_retries_with_feedback_until_approved():
    seen_feedback = []

    def solver(task, prev, fb):
        seen_feedback.append(fb)
        return f"v{len(seen_feedback)}"

    # reject first attempt, approve the second
    verdicts = iter([{"ok": False, "critique": "missing edge case"}, {"ok": True, "critique": ""}])
    critic = lambda task, attempt: next(verdicts)

    res = rx.reflect_and_solve("t", solver=solver, critic=critic, max_iterations=3)
    assert res["converged"] is True and res["iterations"] == 2 and res["answer"] == "v2"
    # the second solve got the critique as feedback
    assert seen_feedback == [None, "missing edge case"]


def test_stops_at_cap_without_convergence():
    solver = lambda task, prev, fb: "still-wrong"
    critic = lambda task, attempt: {"ok": False, "critique": "nope"}
    res = rx.reflect_and_solve("t", solver=solver, critic=critic, max_iterations=2)
    assert res["converged"] is False and res["iterations"] == 2
    assert len(res["history"]) == 2


def test_best_effort_on_solver_exception():
    def solver(task, prev, fb):
        raise RuntimeError("model down")
    res = rx.reflect_and_solve("t", solver=solver, critic=lambda *a: {"ok": True}, max_iterations=2)
    assert res["error"] is not None and res["converged"] is False


def test_parse_verdict_json_and_prose():
    assert rx._parse_verdict('{"ok": true, "critique": ""}')["ok"] is True
    assert rx._parse_verdict('blah {"ok": false, "critique": "wrong"} blah') == {"ok": False, "critique": "wrong"}
    assert rx._parse_verdict("not json at all")["ok"] is False
    assert rx._parse_verdict("")["ok"] is False


def _fake_llm(replies):
    it = iter(replies)
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=next(it)))])
    return _caller


def test_deep_reason_end_to_end_with_fake_llm():
    # solve, critic-reject, solve-again, critic-approve
    llm = _fake_llm([
        "first attempt",
        '{"ok": false, "critique": "incomplete"}',
        "second attempt",
        '{"ok": true, "critique": ""}',
    ])
    res = rx.deep_reason("hard problem", llm_caller=llm, max_iterations=3)
    assert res["converged"] is True and res["answer"] == "second attempt" and res["iterations"] == 2


def test_deep_reason_best_effort_on_failure():
    def boom(**kw):
        raise RuntimeError("down")
    res = rx.deep_reason("x", llm_caller=boom)
    assert res["converged"] is False
