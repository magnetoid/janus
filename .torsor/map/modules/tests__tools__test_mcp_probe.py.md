---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_probe.py

Symbols in `tests/tools/test_mcp_probe.py`.

- L11 `_reset_mcp_state()` (function) — Ensure clean MCP module state before/after each test.
- L24 `TestProbeMcpServerTools` (class) — Tests for the lightweight probe_mcp_server_tools function.
- L27 `test_returns_empty_when_mcp_not_available(self)` (method)
- L33 `test_returns_empty_when_no_config(self)` (method)
- L39 `test_returns_empty_when_all_servers_disabled(self)` (method)
- L49 `test_returns_tools_from_successful_server(self)` (method) — Successfully probed server returns its tools list.
- L91 `test_failed_server_omitted_from_results(self)` (method) — Servers that fail to connect are silently skipped.
- L130 `test_handles_tool_without_description(self)` (method) — Tools without descriptions get empty string.
- L164 `test_cleanup_called_even_on_failure(self)` (method) — _stop_mcp_loop is called even when probe fails.
- L180 `test_skips_disabled_servers(self)` (method) — Disabled servers are not probed.
