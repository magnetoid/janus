---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_setup_noninteractive.py

Symbols in `tests/hermes_cli/test_setup_noninteractive.py`.

- L10 `_make_setup_args(**overrides)` (function)
- L18 `_make_chat_args(**overrides)` (function)
- L35 `TestNonInteractiveSetup` (class) — Verify setup paths exit cleanly in headless/non-interactive environments.
- L38 `test_cmd_setup_allows_noninteractive_flag_without_tty(self)` (method) — The CLI entrypoint should not block --non-interactive before setup.py handles it.
- L53 `test_cmd_setup_defers_no_tty_handling_to_setup_wizard(self)` (method) — Bare `hermes setup` should reach setup.py, which prints headless guidance.
- L68 `test_non_interactive_flag_skips_wizard(self, capsys)` (method) — --non-interactive should print guidance and not enter the wizard.
- L86 `test_no_tty_skips_wizard(self, capsys)` (method) — When stdin has no TTY, the setup wizard should print guidance and return.
- L106 `test_reset_flag_rewrites_config_before_noninteractive_exit(self, tmp_path, monkeypatch, capsys)` (method) — --reset should rewrite config.yaml even when the wizard cannot run interactively.
- L126 `test_chat_first_run_headless_skips_setup_prompt(self, capsys)` (method) — Bare `hermes` should not prompt for input when no provider exists and stdin is headless.
- L147 `test_main_accepts_tts_setup_section(self, monkeypatch)` (method) — `hermes setup tts` should parse and dispatch like other setup sections.
