---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_tool.py

Symbols in `tests/tools/test_terminal_tool.py`.

- L6 `setup_function()` (function)
- L10 `teardown_function()` (function)
- L14 `test_searching_for_sudo_does_not_trigger_rewrite(monkeypatch)` (function)
- L25 `test_printf_literal_sudo_does_not_trigger_rewrite(monkeypatch)` (function)
- L36 `test_non_command_argument_named_sudo_does_not_trigger_rewrite(monkeypatch)` (function)
- L47 `test_actual_sudo_command_uses_configured_password(monkeypatch)` (function)
- L57 `test_actual_sudo_after_leading_env_assignment_is_rewritten(monkeypatch)` (function)
- L67 `test_explicit_empty_sudo_password_tries_empty_without_prompt(monkeypatch)` (function)
- L82 `test_cached_sudo_password_is_used_when_env_is_unset(monkeypatch)` (function)
- L93 `test_cached_sudo_password_isolated_by_session_key(monkeypatch)` (function)
- L107 `test_passwordless_sudo_skips_interactive_prompt_and_rewrite(monkeypatch)` (function)
- L126 `test_passwordless_sudo_probe_rechecks_local_terminal(monkeypatch)` (function)
- L147 `test_passwordless_sudo_probe_is_disabled_for_nonlocal_terminal_env(monkeypatch)` (function)
- L158 `test_validate_workdir_allows_windows_drive_paths()` (function)
- L163 `test_validate_workdir_allows_windows_unc_paths()` (function)
- L167 `test_validate_workdir_blocks_shell_metacharacters_in_windows_paths()` (function)
