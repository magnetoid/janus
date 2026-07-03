"""Tests for the implicit-feedback sensor network (agent/feedback_signals.py)."""
import pytest

from agent import feedback_signals as fb


@pytest.fixture
def _on(monkeypatch):
    monkeypatch.setattr(fb, "_tracking_on", lambda: True)


def test_record_signal_noop_when_tracking_off(monkeypatch):
    monkeypatch.setattr(fb, "_tracking_on", lambda: False)
    fb.record_signal("s1", "interrupt")
    assert fb.session_friction("s1") == 0.0     # nothing recorded


def test_friction_saturates(_on):
    fb.record_signal("s1", "interrupt")         # 1.0
    fb.record_signal("s1", "steer")             # 0.5  -> 1.5/3 = 0.5
    assert fb.session_friction("s1") == 0.5
    fb.record_signal("s1", "interrupt")         # +1.0 -> 2.5/3
    fb.record_signal("s1", "approval_denied")   # +0.8 -> 3.3/3 caps at 1.0
    assert fb.session_friction("s1") == 1.0


def test_unknown_kind_uses_default_weight(_on):
    fb.record_signal("s1", "mystery")           # default 0.5
    assert fb.session_friction("s1") == round(0.5 / 3.0, 4)


def test_explicit_weight_overrides(_on):
    fb.record_signal("s1", "edit", weight=3.0)  # straight to saturation
    assert fb.session_friction("s1") == 1.0


def test_clear_session(_on):
    fb.record_signal("s1", "interrupt")
    assert fb.session_friction("s1") > 0
    fb.clear_session("s1")
    assert fb.session_friction("s1") == 0.0
    fb.clear_session("s1")                       # idempotent
    fb.clear_session("")                         # safe on empty


def test_unknown_session_is_zero(_on):
    assert fb.session_friction("never") == 0.0
    assert fb.session_friction("") == 0.0
