---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_codex_runtime_switch.py

Symbols in `tests/hermes_cli/test_codex_runtime_switch.py`.

- L16 `TestParseArgs` (class)
- L30 `test_valid_args(self, arg, expected)` (method)
- L35 `test_invalid_arg_returns_error(self)` (method)
- L41 `TestGetCurrentRuntime` (class)
- L42 `test_default_when_unset(self)` (method)
- L47 `test_unrecognized_falls_back_to_auto(self)` (method)
- L52 `test_explicit_codex(self)` (method)
- L57 `test_handles_non_dict_config(self)` (method)
- L63 `TestSetRuntime` (class)
- L64 `test_creates_model_section_if_missing(self)` (method)
- L70 `test_returns_previous_value(self)` (method)
- L76 `test_invalid_value_raises(self)` (method)
- L81 `TestApply` (class)
- L82 `test_read_only_call_reports_state(self)` (method)
- L93 `test_no_change_when_already_set(self)` (method)
- L99 `test_enable_blocked_when_codex_missing(self)` (method)
- L110 `test_enable_succeeds_when_codex_present(self)` (method)
- L135 `test_disable_does_not_check_binary(self)` (method)
- L145 `test_persist_callback_failure_reported(self)` (method)
- L158 `test_enable_triggers_mcp_migration(self)` (method) — Enabling codex_app_server should auto-migrate Hermes mcp_servers
- L187 `test_disable_does_not_trigger_migration(self)` (method) — Switching back to auto must not write to ~/.codex/.
- L198 `test_migration_failure_does_not_block_enable(self)` (method) — If MCP migration raises, the runtime change still proceeds —
- L212 `test_binary_check_cached_within_apply(self)` (method) — check_codex_binary_ok is invoked at most once per apply() call.
- L231 `test_binary_check_cached_on_read_only_call(self)` (method) — Read-only call (new_value=None) calls the binary check exactly
