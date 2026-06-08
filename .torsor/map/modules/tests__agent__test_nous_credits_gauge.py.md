---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_nous_credits_gauge.py

Symbols in `tests/agent/test_nous_credits_gauge.py`.

- L16 `_acct(**kwargs)` (function)
- L24 `_window(snap)` (function)
- L28 `test_parser_captures_monthly_credits()` (function)
- L38 `test_parser_monthly_credits_absent_is_none()` (function)
- L43 `test_gauge_present_with_monthly_credits()` (function)
- L60 `test_gauge_90pct()` (function)
- L68 `test_gauge_debt_clamps_to_100()` (function)
- L77 `test_gauge_at_cap_is_zero_used()` (function)
- L85 `test_no_monthly_credits_falls_back_to_magnitudes()` (function)
- L97 `test_nan_remaining_no_window_no_nan_string()` (function) — json.loads parses bare NaN by default; isinstance(nan, float) is True.
- L109 `test_inf_cap_no_window()` (function)
- L118 `test_rollover_balance_exceeds_cap_no_window()` (function) — remaining > cap (rollover spanning the period) makes monthly_credits a
- L130 `test_bool_monthly_credits_no_window()` (function)
- L139 `test_zero_monthly_credits_no_divzero()` (function)
- L148 `test_failopen_none_and_logged_out()` (function)
