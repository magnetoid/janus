---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_structured_content.py

Symbols in `tests/tools/test_mcp_structured_content.py`.

- L13 `_FakeContentBlock` (class) — Minimal content block with .text and .type attributes.
- L16 `__init__(self, text: str, block_type: str='text')` (method)
- L21 `_FakeCallToolResult` (class) — Minimal CallToolResult stand-in.
- L28 `__init__(self, content, is_error=False, structuredContent=None)` (method)
- L34 `_fake_run_on_mcp_loop(coro_or_factory, timeout=30)` (function)
- L53 `_patch_mcp_server()` (function) — Patch _servers and the MCP event loop so _make_tool_handler can run.
- L65 `TestStructuredContentPreservation` (class) — Ensure structuredContent from CallToolResult is forwarded.
- L68 `test_text_only_result(self, _patch_mcp_server)` (method) — When no structuredContent, result is text-only (existing behaviour).
- L81 `test_both_content_and_structured(self, _patch_mcp_server)` (method) — When both content and structuredContent are present, combine them.
- L98 `test_both_content_and_structured_desktop_commander(self, _patch_mcp_server)` (method) — Real-world case: Desktop Commander returns file text in content,
- L116 `test_structured_content_none_falls_back_to_text(self, _patch_mcp_server)` (method) — When structuredContent is explicitly None, fall back to text.
- L130 `test_empty_text_with_structured_content(self, _patch_mcp_server)` (method) — When content blocks are empty but structuredContent exists.
