---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_quick_commands.py

Symbols in `tests/cli/test_quick_commands.py`.

- L11 `TestCLIQuickCommands` (class) — Test quick command dispatch in HermesCLI.process_command.
- L15 `_printed_plain(call_arg)` (method)
- L20 `_make_cli(self, quick_commands)` (method)
- L34 `test_exec_command_runs_and_prints_output(self)` (method)
- L42 `test_exec_command_uses_chat_console_when_tui_is_live(self)` (method)
- L56 `test_exec_command_stderr_shown_on_no_stdout(self)` (method)
- L63 `test_exec_command_no_output_shows_fallback(self)` (method)
- L70 `test_alias_command_routes_to_target(self)` (method) — Alias quick commands rewrite to the target command.
- L78 `test_alias_command_passes_args(self)` (method) — Alias quick commands forward user arguments to the target.
- L85 `test_alias_no_target_shows_error(self)` (method)
- L92 `test_unsupported_type_shows_error(self)` (method)
- L99 `test_missing_command_field_shows_error(self)` (method)
- L106 `test_quick_command_takes_priority_over_skill_commands(self)` (method) — Quick commands must be checked before skill slash commands.
- L115 `test_unknown_command_still_shows_error(self)` (method)
- L123 `test_timeout_shows_error(self)` (method)
- L134 `TestGatewayQuickCommands` (class) — Test quick command dispatch in GatewayRunner._handle_message.
- L137 `_make_event(self, command, args='')` (method)
- L151 `test_exec_command_returns_output(self)` (method)
- L164 `test_exec_command_does_not_leak_credentials(self)` (method) — Quick command exec must sanitize env — API keys must not appear in output.
- L182 `test_exec_command_output_is_redacted(self, monkeypatch)` (method) — Quick command output must redact sensitive patterns before returning.
- L204 `test_unsupported_type_returns_error(self)` (method)
- L218 `test_timeout_returns_error(self)` (method)
- L234 `test_gateway_config_object_supports_quick_commands(self)` (method)
