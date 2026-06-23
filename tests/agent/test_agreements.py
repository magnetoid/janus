"""Tests for Standing Agreements (agent/agreements.py)."""
from agent import agreements as ag


def test_enabled_default_on_and_gated():
    assert ag.enabled({}) is True
    assert ag.enabled({"agreements": {"enabled": False}}) is False
    assert ag.enabled({"agreements": {"enabled": True}}) is True


def test_directive_present_when_enabled_empty_when_disabled():
    assert "STANDING AGREEMENT" in ag.directive({})
    assert ag.directive({"agreements": {"enabled": False}}) == ""


def test_format_agreement_marks_and_normalizes():
    out = ag.format_agreement("  use  the   shared fixture  ")
    assert out == f"{ag.AGREEMENT_MARKER}: use the shared fixture"


def test_is_agreement_message_detects_marked():
    assert ag.is_agreement_message({"role": "assistant", "content": ag.format_agreement("x")})
    assert ag.is_agreement_message(ag.format_agreement("y"))  # raw string
    # multimodal content blocks
    assert ag.is_agreement_message(
        {"content": [{"type": "text", "text": ag.format_agreement("z")}]})
    assert ag.is_agreement_message({"role": "user", "content": "just a normal message"}) is False
    assert ag.is_agreement_message({"role": "user", "content": ""}) is False


def test_record_load_dedup_clear():
    sid = "sess-1"
    assert ag.load(sid) == []
    e = ag.record(sid, "deploy only to staging", source="user")
    assert e and e["text"] == "deploy only to staging" and e["source"] == "user"
    assert ag.record(sid, "Deploy Only To Staging") is None  # case-insensitive dedup
    assert len(ag.load(sid)) == 1
    ag.record(sid, "never force-push main")
    assert len(ag.load(sid)) == 2
    assert ag.clear(sid) == 2
    assert ag.load(sid) == []


def test_record_empty_returns_none():
    assert ag.record("s", "   ") is None


def test_render_for_prompt():
    sid = "sess-2"
    assert ag.render_for_prompt(sid) == ""
    ag.record(sid, "agreement A")
    ag.record(sid, "agreement B")
    block = ag.render_for_prompt(sid)
    assert "Standing agreements in effect:" in block
    assert "- agreement A" in block and "- agreement B" in block


def test_sessions_are_isolated():
    ag.record("sA", "only in A")
    assert ag.load("sB") == []


def test_best_effort_never_raises():
    assert isinstance(ag.directive(None), str)
    assert isinstance(ag.load("nope"), list)
    assert ag.is_agreement_message(None) is False
