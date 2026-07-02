"""Tests for the autonomy safety floor (agent/autonomy_guard.py).

The freeze sentinel and config flag are checked with the isolated JANUS_HOME the
autouse fixture provides; spend caps are exercised via the ledger.
"""
from agent import autonomy_guard as ag
from agent import cost_ledger as cl


def test_freeze_unfreeze_via_sentinel():
    assert ag.frozen() is False
    assert ag.freeze("runaway tree") is True
    assert ag.frozen() is True
    assert ag.freeze_reason_text() == "runaway tree"
    reason = ag.blocked_reason()
    assert reason and "frozen" in reason and "runaway tree" in reason
    ag.unfreeze()
    assert ag.frozen() is False
    assert ag.blocked_reason() is None


def test_config_frozen_flag_blocks():
    # No sentinel, but config says frozen -> blocked.
    assert ag.frozen({"autonomy": {"frozen": True}}) is True
    assert ag.blocked_reason({"autonomy": {"frozen": True}}) is not None
    assert ag.frozen({"autonomy": {"frozen": False}}) is False


def test_sentinel_wins_over_config():
    ag.freeze("hard stop")
    # Even if config says not frozen, the sentinel keeps it frozen.
    assert ag.frozen({"autonomy": {"frozen": False}}) is True
    ag.unfreeze()


def test_spend_cap_blocks_when_over():
    cl.record_turn("s", "m", cost_usd=9.0)  # ts=now
    reason = ag.blocked_reason({"budget": {"daily_usd": 5.0}})
    assert reason and "cap" in reason
    # generous cap -> allowed
    assert ag.blocked_reason({"budget": {"daily_usd": 1000.0}}) is None


def test_freeze_takes_precedence_over_spend():
    # Frozen AND over budget -> the freeze reason is reported first.
    cl.record_turn("s", "m", cost_usd=9.0)
    ag.freeze("stop everything")
    reason = ag.blocked_reason({"budget": {"daily_usd": 5.0}})
    assert "frozen" in reason
    ag.unfreeze()
