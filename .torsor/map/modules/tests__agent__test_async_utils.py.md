---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_async_utils.py

Symbols in `tests/agent/test_async_utils.py`.

- L19 `_no_unawaited_warnings(caught, *, coro_name: str='')` (function) — Return True if no "X was never awaited" warning slipped through.
- L39 `TestSafeScheduleThreadsafe` (class)
- L40 `test_returns_future_on_success(self)` (method)
- L74 `test_closed_loop_returns_none_and_closes_coroutine(self)` (method)
- L91 `test_none_loop_returns_none_and_closes_coroutine(self)` (method)
- L105 `test_scheduling_exception_closes_coroutine(self)` (method) — If run_coroutine_threadsafe raises, close the coroutine and return None.
- L129 `test_logs_at_specified_level(self, caplog)` (method)
- L149 `test_non_coroutine_arg_does_not_crash(self)` (method) — Defensive: even if the caller hands us something weird, don't blow up.
