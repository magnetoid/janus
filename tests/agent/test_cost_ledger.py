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


# --- rolling spend caps (move 3: safety floor) ------------------------------

def _at(iso, cost):
    return {"ts": iso, "session_id": "s", "model": "m", "cost_usd": cost}


def test_spend_since_sums_window_across_sessions():
    now = 1_000_000.0
    from datetime import datetime, timezone
    def iso(offset):  # `offset` seconds before `now`
        return datetime.fromtimestamp(now - offset, tz=timezone.utc).isoformat()
    rows = [_at(iso(10), 1.0), _at(iso(100), 2.0), _at(iso(100000), 5.0)]
    # window covering the last 1000s catches the first two rows only
    assert cl.spend_since(now - 1000, rows=rows) == 3.0
    # unparseable/missing ts is EXCLUDED — counting it would inflate every
    # window monotonically and permanently trip the cap (no recovery path).
    assert cl.spend_since(now - 1000, rows=[{"ts": "not-a-date", "cost_usd": 4.0}]) == 0.0


def test_rolling_spend_day_and_month():
    import time
    from datetime import datetime, timezone
    now = time.time()
    def iso(offset):
        return datetime.fromtimestamp(now - offset, tz=timezone.utc).isoformat()
    for cost, off in [(1.0, 3600), (2.0, 3 * 86400), (8.0, 40 * 86400)]:
        cl.record_turn("s", "m", cost_usd=cost, ts=iso(off))
    assert cl.rolling_spend("day", now_ts=now) == 1.0        # only the 1h-ago row
    assert cl.rolling_spend("month", now_ts=now) == 3.0      # 1h + 3d rows


def test_spend_cap_exceeded_reason():
    cl.record_turn("s", "m", cost_usd=5.0)  # ts defaults to now
    reason = cl.spend_cap_exceeded({"budget": {"daily_usd": 3.0}})
    assert reason and "24h" in reason and "cap" in reason
    assert cl.spend_cap_exceeded({"budget": {"daily_usd": 100.0}}) is None  # under cap
    assert cl.spend_cap_exceeded({"budget": {}}) is None                    # unset
