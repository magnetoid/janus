---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_slash_command_interrupt.py

Symbols in `tests/cli/test_slash_command_interrupt.py`.

- L19 `_make_cli()` (function)
- L28 `_dispatch(cli, user_input: str, process_command_side_effect=None)` (function) — Mirror the production dispatch shape from cli.py around line 14236.
- L54 `TestSlashCommandKeyboardInterrupt` (class)
- L55 `test_keyboardinterrupt_in_slash_command_does_not_set_exit(self)` (method) — Ctrl+C in the middle of /skills browse must NOT set _should_exit.
- L74 `test_normal_slash_command_returns_truthy_keeps_session_alive(self)` (method) — A successful slash command (returns truthy) must NOT set _should_exit.
- L82 `test_slash_command_returning_false_sets_exit(self)` (method) — The legitimate exit signal — process_command() returning False —
- L91 `test_other_exceptions_propagate(self)` (method) — Only KeyboardInterrupt is caught locally. Other exceptions must
