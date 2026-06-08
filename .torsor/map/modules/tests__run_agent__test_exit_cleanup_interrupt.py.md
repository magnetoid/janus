---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_exit_cleanup_interrupt.py

Symbols in `tests/run_agent/test_exit_cleanup_interrupt.py`.

- L15 `_mock_runtime_provider(monkeypatch)` (function) — run_job calls resolve_runtime_provider which can try real network
- L32 `TestCronJobCleanup` (class) — cron/scheduler.py — end_session + close in the finally block.
- L35 `test_keyboard_interrupt_in_end_session_does_not_skip_close(self)` (method) — If end_session raises KeyboardInterrupt, close() must still run.
- L63 `test_keyboard_interrupt_in_close_does_not_propagate(self)` (method) — If close() raises KeyboardInterrupt, it must not escape run_job.
