---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_background_tui_refresh.py

Symbols in `tests/cli/test_cli_background_tui_refresh.py`.

- L13 `_make_cli()` (function) — Create a minimal HermesCLI instance for testing.
- L25 `TestBackgroundCommandTuiRefresh` (class) — Tests for TUI refresh in background command output.
- L28 `test_invalidate_called_before_success_output(self)` (method) — App.invalidate() is called before printing background success output.
- L59 `test_invalidate_called_before_error_output(self)` (method) — App.invalidate() is called before printing background error output.
- L81 `test_no_crash_when_app_is_none(self)` (method) — No crash when _app is None (non-TUI mode).
- L91 `test_background_task_thread_safety(self)` (method) — Background task tracking is thread-safe.
