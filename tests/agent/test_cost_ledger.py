"""Tests for the per-turn cost ledger + session spend ceiling (agent/cost_ledger.py)."""
from agent import cost_ledger as cl


def test_record_load_and_session_total():
    assert cl.record_turn("s1", "opus", input_tokens=100, output_tokens=20, cost_usd=0.01) is True
    assert cl.record_turn("s1", "opus", input_tokens=50, output_tokens=10, cost_usd=0.02) is True
    assert cl.record_turn("s2", "sonnet", cost_usd=0.005) is True
    rows = cl.load_ledger()
    assert len(rows) == 3
    assert rows[0]["session_id"] == "s1" and rows[0]["model"] == "opus"
    assert cl.session_total_usd("s1") == 0.03
    assert cl.session_total_usd("s2") == 0.005
    assert cl.session_total_usd("nope") == 0.0


def test_session_cost_limit_from_config():
    assert cl.session_cost_limit_usd({"budget": {"session_cost_usd": 1.5}}) == 1.5
    assert cl.session_cost_limit_usd({"budget": {"session_cost_usd": 0}}) is None    # 0 = unlimited
    assert cl.session_cost_limit_usd({}) is None                                     # default unlimited
    assert cl.session_cost_limit_usd({"budget": {"session_cost_usd": None}}) is None


def test_over_session_budget_logic():
    assert cl.over_session_budget(0.5, None) is False        # unlimited
    assert cl.over_session_budget(0.5, 0) is False           # 0 = unlimited
    assert cl.over_session_budget(0.4, 1.0) is False         # under ceiling
    assert cl.over_session_budget(1.0, 1.0) is True          # at ceiling
    assert cl.over_session_budget(1.2, 1.0) is True          # over ceiling


def test_record_turn_best_effort_on_bad_input():
    assert cl.record_turn("s", "m", cost_usd=None) is True   # None cost coerced to 0.0
    assert cl.load_ledger()[-1]["cost_usd"] == 0.0
