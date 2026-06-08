---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_anthropic_mcp_prefix_strip.py

Symbols in `tests/agent/test_anthropic_mcp_prefix_strip.py`.

- L20 `_make_tool_use_block(name: str, block_id: str='tc_1', input_data: dict | None=None)` (function) — Create a fake Anthropic tool_use content block.
- L30 `_make_response(*blocks, stop_reason='end_turn')` (function) — Create a fake Anthropic Messages response.
- L40 `_FakeRegistry` (class) — Minimal fake tool registry for testing prefix stripping logic.
- L43 `__init__(self, registered_names: set[str])` (method)
- L46 `get_entry(self, name: str)` (method)
- L56 `TestAnthropicMcpPrefixStrip` (class) — Verify that strip_tool_prefix only strips OAuth-injected prefixes.
- L59 `_get_transport(self)` (method)
- L63 `test_strips_prefix_for_oauth_injected_tool(self)` (method) — OAuth tools: mcp_read_file -> read_file (stripped).
- L81 `test_preserves_native_mcp_server_tool_name(self)` (method) — Native MCP tools: mcp_composio_SEARCH -> mcp_composio_SEARCH (kept).
- L102 `test_no_strip_when_flag_false(self)` (method) — When strip_tool_prefix=False, names are never modified.
- L115 `test_no_strip_when_not_mcp_prefixed(self)` (method) — Non-mcp_ names are untouched regardless of strip flag.
- L128 `test_preserves_name_when_neither_in_registry(self)` (method) — When neither stripped nor full name is in registry, keep full name.
- L145 `test_mixed_tools_same_response(self)` (method) — Both OAuth and native MCP tools in the same response.
- L167 `test_both_stripped_and_full_registered_prefers_full(self)` (method) — Edge case: both 'foo' and 'mcp_foo' exist in registry.
- L186 `TestAnthropicOAuthOutgoingPrefix` (class) — Verify the outgoing-side companion fix: build_anthropic_kwargs must not
- L191 `_build(self, tools, is_oauth=True)` (method)
- L202 `test_oauth_adds_prefix_to_bare_tool_name(self)` (method) — OAuth + bare name → prefix added (existing Claude Code convention).
- L211 `test_oauth_does_not_double_prefix_native_mcp_tool(self)` (method) — OAuth + already-prefixed native MCP name → left alone.
- L226 `test_oauth_mixed_native_and_bare_tools(self)` (method) — Mixed: native MCP preserved, bare names prefixed.
- L239 `test_non_oauth_path_untouched(self)` (method) — Non-OAuth requests never get the prefix — schemas pass through as-is.
