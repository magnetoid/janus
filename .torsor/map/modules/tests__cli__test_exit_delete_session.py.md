---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_exit_delete_session.py

Symbols in `tests/cli/test_exit_delete_session.py`.

- L12 `_make_cli()` (function) — Bare HermesCLI suitable for process_command() tests.
- L29 `TestExitDeleteFlag` (class)
- L30 `test_plain_exit_does_not_arm_delete(self)` (method)
- L36 `test_plain_quit_does_not_arm_delete(self)` (method)
- L42 `test_exit_delete_arms_flag(self)` (method)
- L48 `test_quit_delete_arms_flag(self)` (method)
- L54 `test_exit_delete_short_form(self)` (method) — `-d` is a convenience alias for `--delete`.
- L61 `test_quit_alias_q_is_not_quit(self)` (method) — `/q` is the alias for `/queue`, not `/quit`. This test documents
- L72 `test_delete_flag_is_case_insensitive(self)` (method)
- L78 `test_delete_flag_trims_whitespace(self)` (method)
- L84 `test_unknown_exit_argument_does_not_exit(self)` (method) — Unrecognised args should NOT exit the CLI — they surface an
- L94 `test_unknown_exit_argument_prints_help(self)` (method)
- L105 `TestCommandRegistry` (class)
- L106 `test_quit_command_advertises_delete_flag(self)` (method) — The CommandDef args_hint should surface `--delete` in /help and
- L114 `test_exit_alias_resolves_to_quit_with_hint(self)` (method)
