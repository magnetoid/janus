"""Tests for the propose_plan tool."""
import json

from agent import plan_mode as pm
import tools.plan_tool as t


def test_propose_plan_records_and_formats():
    out = t.propose_plan(["clone repo", "run tests"], task_id="p1")
    assert "1. clone repo" in out and "2. run tests" in out and "go" in out.lower()
    assert pm.load_plan("p1") == ["clone repo", "run tests"]


def test_propose_plan_string_coerced_to_list():
    assert "1. single step" in t.propose_plan("single step", task_id="p2")


def test_propose_plan_empty_returns_error():
    assert json.loads(t.propose_plan([], task_id="p3"))["success"] is False


def test_tool_registered_and_exposed():
    from toolsets import TOOLSETS, _JANUS_CORE_TOOLS
    assert "propose_plan" in TOOLSETS["memory"]["tools"]
    assert "propose_plan" in _JANUS_CORE_TOOLS
