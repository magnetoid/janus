"""Tests for the pin_agreement / recall_agreements tools."""
import json

from agent import agreements as ag
import tools.agreements_tool as t


def test_pin_agreement_records_and_marks():
    out = t.pin_agreement("deploy only to staging", task_id="s1")
    assert out == ag.format_agreement("deploy only to staging")
    assert any(i["text"] == "deploy only to staging" for i in ag.load("s1"))


def test_pin_agreement_empty_returns_error():
    assert json.loads(t.pin_agreement("   ", task_id="s1"))["success"] is False


def test_recall_agreements_returns_block():
    t.pin_agreement("never force-push main", task_id="s2")
    block = t.recall_agreements(task_id="s2")
    assert "never force-push main" in block and "Standing agreements" in block


def test_recall_empty_session():
    assert "No standing agreements" in t.recall_agreements(task_id="empty-sess")


def test_tools_registered_in_memory_toolset():
    from toolsets import TOOLSETS, _JANUS_CORE_TOOLS
    assert "pin_agreement" in TOOLSETS["memory"]["tools"]
    assert "recall_agreements" in TOOLSETS["memory"]["tools"]
    assert "pin_agreement" in _JANUS_CORE_TOOLS and "recall_agreements" in _JANUS_CORE_TOOLS
