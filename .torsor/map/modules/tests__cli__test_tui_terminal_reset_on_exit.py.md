---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_tui_terminal_reset_on_exit.py

Symbols in `tests/cli/test_tui_terminal_reset_on_exit.py`.

- L17 `_import_cli()` (function)
- L32 `_FakeStream` (class)
- L33 `__init__(self, isatty: bool=True)` (method)
- L38 `isatty(self)` (method)
- L41 `write(self, s: str)` (method)
- L45 `flush(self)` (method)
- L49 `TestResetTerminalInputModes` (class)
- L50 `test_emits_reset_seq_on_tty_when_tui_ran(self)` (method)
- L65 `test_noop_when_tui_never_ran(self)` (method) — Non-TUI one-shot CLI runs share _run_cleanup via atexit — they must
- L81 `test_noop_when_not_a_tty_and_no_dev_tty(self)` (method) — stdout redirected and /dev/tty unavailable → nothing written, no raise.
- L94 `test_falls_back_to_dev_tty_when_stdout_redirected(self)` (method) — When stdout isn't the terminal, reset via /dev/tty (issue's own
- L111 `test_swallows_stdout_errors(self)` (method)
- L126 `test_mark_tui_input_modes_active_sets_flag(self)` (method)
- L136 `test_flag_cleared_after_reset(self)` (method) — Once the modes are disabled they are no longer active — the flag must
- L154 `TestRunCleanupWiring` (class) — _run_cleanup must call the reset, as its first step, on every invocation
- L158 `_run_cleanup_isolated(self, cli_mod, **extra_patches)` (method) — Invoke _run_cleanup with heavy/real teardown steps stubbed out so the
- L198 `test_run_cleanup_calls_reset(self)` (method)
- L203 `test_reset_runs_even_when_a_cleanup_step_raises(self)` (method) — The reset is the first step, so a failing teardown step can't skip
