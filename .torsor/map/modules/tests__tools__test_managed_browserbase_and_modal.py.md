---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_managed_browserbase_and_modal.py

Symbols in `tests/tools/test_managed_browserbase_and_modal.py`.

- L20 `_load_tool_module(module_name: str, filename: str)` (function)
- L29 `_load_plugin_module(module_name: str, relpath: str)` (function) — Load a plugin module by file path from ``plugins/``.
- L44 `_reset_modules(prefixes: tuple[str, ...])` (function)
- L51 `_restore_tool_and_agent_modules()` (function)
- L68 `_enable_managed_nous_tools(monkeypatch)` (function) — Ensure managed_nous_tools_enabled() returns True even after module reloads.
- L87 `_install_fake_tools_package()` (function)
- L196 `test_browser_use_explicit_local_mode_stays_local_even_when_managed_gateway_is_ready(tmp_path)` (function)
- L217 `test_browserbase_does_not_use_gateway_only_configuration()` (function)
- L237 `test_browser_use_availability_skips_refresh_for_expired_cached_gateway_token(tmp_path, monkeypatch)` (function)
- L275 `test_browser_use_managed_gateway_adds_idempotency_key_and_persists_external_call_id()` (function)
- L315 `test_browser_use_managed_gateway_reuses_pending_idempotency_key_after_timeout()` (function)
- L363 `test_browser_use_managed_gateway_preserves_pending_idempotency_key_for_in_progress_conflicts()` (function)
- L424 `test_browser_use_managed_gateway_uses_new_idempotency_key_for_a_new_session_after_success()` (function)
- L461 `test_terminal_tool_prefers_managed_modal_when_gateway_ready_and_no_direct_creds()` (function)
- L496 `test_terminal_tool_auto_mode_prefers_managed_modal_when_available()` (function)
- L532 `test_terminal_tool_auto_mode_falls_back_to_direct_modal_when_managed_unavailable()` (function)
- L568 `test_terminal_tool_respects_direct_modal_mode_without_falling_back_to_managed()` (function)
- L598 `TestShellEscapeBypass` (class) — Regression for #36846/#36847: backslash escapes and empty-string
- L603 `test_backslash_escape_bypass_caught(self)` (method)
- L608 `test_empty_string_literal_bypass_caught(self)` (method)
- L613 `test_plain_dangerous_still_caught(self)` (method)
- L617 `test_benign_command_not_flagged(self)` (method)
