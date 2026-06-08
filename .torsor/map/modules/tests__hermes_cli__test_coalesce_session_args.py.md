---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_coalesce_session_args.py

Symbols in `tests/hermes_cli/test_coalesce_session_args.py`.

- L6 `TestCoalesceSessionNameArgs` (class) — Ensure unquoted multi-word session names are merged into one token.
- L11 `test_continue_multiword_unquoted(self)` (method) — hermes -c Pokemon Agent Dev → -c 'Pokemon Agent Dev'
- L17 `test_continue_long_form_multiword(self)` (method) — hermes --continue Pokemon Agent Dev
- L23 `test_continue_single_word(self)` (method) — hermes -c MyProject (no merging needed)
- L30 `test_continue_already_quoted(self)` (method) — hermes -c 'Pokemon Agent Dev' (shell already merged)
- L36 `test_continue_bare_flag(self)` (method) — hermes -c (no name — means 'continue latest')
- L40 `test_continue_followed_by_flag(self)` (method) — hermes -c -w (no name consumed, -w stays separate)
- L44 `test_continue_multiword_then_flag(self)` (method) — hermes -c my project -w
- L50 `test_continue_multiword_then_subcommand(self)` (method) — hermes -c my project chat -q hello
- L58 `test_resume_multiword(self)` (method) — hermes -r My Session Name
- L64 `test_resume_long_form_multiword(self)` (method) — hermes --resume My Session Name
- L70 `test_resume_multiword_then_flag(self)` (method) — hermes -r My Session -w
- L78 `test_worktree_and_continue_multiword(self)` (method) — hermes -w -c Pokemon Agent Dev (the original failing case)
- L84 `test_continue_multiword_and_worktree(self)` (method) — hermes -c Pokemon Agent Dev -w (order reversed)
- L92 `test_no_session_flags_passthrough(self)` (method) — hermes -w chat -q hello (nothing to merge)
- L97 `test_empty_argv(self)` (method)
- L102 `test_stops_at_sessions_subcommand(self)` (method) — hermes -c my project sessions list → stops before 'sessions'
- L108 `test_stops_at_setup_subcommand(self)` (method) — hermes -c my setup → 'setup' is a subcommand, not part of name
