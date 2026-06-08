---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_dynamic_discovery.py

Symbols in `tests/tools/test_mcp_dynamic_discovery.py`.

- L13 `_make_mcp_tool(name: str, desc: str='')` (function)
- L17 `TestRegisterServerTools` (class) — Tests for the extracted _register_server_tools helper.
- L21 `mock_registry(self)` (method)
- L24 `test_exposes_live_server_aliases(self, mock_registry)` (method) — Registered MCP tools are reachable via live raw-server aliases.
- L39 `TestRefreshTools` (class) — Tests for MCPServerTask._refresh_tools nuke-and-repave cycle.
- L43 `mock_registry(self)` (method)
- L47 `test_nuke_and_repave(self, mock_registry)` (method) — Old tools are removed and new tools registered on refresh.
- L79 `TestMessageHandler` (class) — Tests for MCPServerTask._make_message_handler dispatch.
- L83 `test_dispatches_tool_list_changed(self)` (method)
- L105 `test_ignores_exceptions_and_other_messages(self)` (method)
- L116 `TestDeregister` (class) — Tests for ToolRegistry.deregister.
- L119 `test_removes_tool(self)` (method)
- L126 `test_cleans_up_toolset_check(self)` (method)
- L135 `test_preserves_toolset_check_if_other_tools_remain(self)` (method)
- L144 `test_removes_toolset_alias_when_last_tool_is_removed(self)` (method)
- L153 `test_preserves_toolset_alias_while_toolset_still_exists(self)` (method)
- L163 `test_noop_for_unknown_tool(self)` (method)
