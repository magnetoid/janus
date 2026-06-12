"""Tests for continual-learning instrumentation (agent/outcome_tracker.py)."""
from agent import outcome_tracker as ot


def test_metrics_insufficient_data_is_honest():
    ot.record_outcome("s1", True, skills=["a"])
    m = ot.learning_metrics()
    assert m["sessions"] == 1
    assert m["forward_transfer"] is None
    assert "Insufficient data" in m["summary"]


def test_forward_transfer_detects_improvement():
    # early sessions mostly fail, later sessions mostly succeed
    for i in range(3):
        ot.record_outcome(f"e{i}", False, skills=["x"])
    for i in range(3):
        ot.record_outcome(f"m{i}", False, skills=["x"])
    for i in range(3):
        ot.record_outcome(f"l{i}", True, skills=["x"])
    fwt = ot.forward_transfer()
    assert fwt is not None and fwt > 0  # late third beats early third


def test_forward_transfer_detects_decline():
    for i in range(3):
        ot.record_outcome(f"e{i}", True, skills=["x"])
    for i in range(3):
        ot.record_outcome(f"m{i}", True, skills=["x"])
    for i in range(3):
        ot.record_outcome(f"l{i}", False, skills=["x"])
    assert ot.forward_transfer() < 0


def test_backward_transfer_over_recurring_skill():
    # skill "deploy" used across both halves; success rate rises in the 2nd half
    for i in range(4):
        ot.record_outcome(f"e{i}", i >= 3, skills=["deploy"])  # 1/4 early
    for i in range(4):
        ot.record_outcome(f"l{i}", i >= 1, skills=["deploy"])  # 3/4 late
    bwt = ot.backward_transfer()
    assert bwt is not None and bwt > 0


def test_forgetting_flags_regressing_skill():
    # skill succeeds early, then fails recently -> forgetting > 0
    for i in range(5):
        ot.record_outcome(f"e{i}", True, skills=["parse"])
    for i in range(5):
        ot.record_outcome(f"l{i}", False, skills=["parse"])
    fgt = ot.forgetting(window=5)
    assert fgt is not None and fgt > 0


def test_skill_diversity_collapse_signals_warning():
    # older window: diverse skills; recent window: one skill repeated
    for i in range(3):
        ot.record_outcome(f"o{i}", True, skills=[f"skill{i}"])
    for i in range(3):
        ot.record_outcome(f"r{i}", True, skills=["same"])
    trend = ot.diversity_trend(window=3)
    assert trend is not None and trend < 0  # diversity dropped


def test_entropy_bounds():
    assert ot._normalized_entropy([]) is None
    assert ot._normalized_entropy([5]) == 0.0          # single category = no diversity
    assert ot._normalized_entropy([1, 1, 1, 1]) == 1.0  # perfectly even = max


def test_learning_metrics_bundles_warnings():
    for i in range(5):
        ot.record_outcome(f"e{i}", True, skills=["parse"])
    for i in range(5):
        ot.record_outcome(f"l{i}", False, skills=["parse"])
    m = ot.learning_metrics()
    assert m["forgetting"] is not None
    # a regressing skill should produce at least one warning
    assert any("regress" in w or "declin" in w for w in m["warnings"])
