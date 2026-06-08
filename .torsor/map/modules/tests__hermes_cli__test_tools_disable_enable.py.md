---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tools_disable_enable.py

Symbols in `tests/hermes_cli/test_tools_disable_enable.py`.

- L11 `TestToolsDisableBuiltin` (class)
- L13 `test_disable_removes_toolset_from_platform(self)` (method)
- L22 `test_disable_multiple_toolsets(self)` (method)
- L32 `test_disable_already_absent_is_idempotent(self)` (method)
- L44 `TestToolsEnableBuiltin` (class)
- L46 `test_enable_adds_toolset_to_platform(self)` (method)
- L54 `test_enable_already_present_is_idempotent(self)` (method)
- L66 `TestToolsDisableMcp` (class)
- L68 `test_disable_adds_to_exclude_list(self)` (method)
- L78 `test_disable_already_excluded_is_idempotent(self)` (method)
- L88 `test_disable_unknown_server_prints_error(self, capsys)` (method)
- L102 `TestToolsEnableMcp` (class)
- L104 `test_enable_removes_from_exclude_list(self)` (method)
- L119 `TestToolsMixedTargets` (class)
- L121 `test_disable_builtin_and_mcp_together(self)` (method)
- L137 `test_builtin_toggle_does_not_persist_implicit_mcp_defaults(self)` (method)
- L158 `TestToolsList` (class)
- L160 `test_list_shows_enabled_toolsets(self, capsys)` (method)
- L168 `test_list_shows_mcp_excluded_tools(self, capsys)` (method)
- L182 `TestToolsValidation` (class)
- L184 `test_unknown_platform_prints_error(self, capsys)` (method)
- L194 `test_unknown_toolset_prints_error(self, capsys)` (method)
- L204 `test_unknown_toolset_does_not_corrupt_config(self)` (method)
- L215 `test_mixed_valid_and_invalid_applies_valid_only(self)` (method)
