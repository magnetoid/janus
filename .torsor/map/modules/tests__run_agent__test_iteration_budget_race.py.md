---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_iteration_budget_race.py

Symbols in `tests/run_agent/test_iteration_budget_race.py`.

- L10 `test_iteration_budget_used_is_thread_safe()` (function) — Iterating `used` while other threads consume/refund must not crash.
- L53 `test_iteration_budget_consume_returns_false_when_exhausted()` (function) — consume() must return False once the budget is exhausted.
- L64 `test_iteration_budget_refund_restores_consume()` (function) — refund() after consume() must allow one more consume().
- L76 `test_iteration_budget_used_reflects_consume_and_refund()` (function) — used property must accurately reflect consume() and refund() calls.
- L93 `test_iteration_budget_remaining()` (function) — remaining property must equal max_total - used.
