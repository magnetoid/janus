---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_compression_boundary.py

Symbols in `tests/run_agent/test_compression_boundary.py`.

- L16 `_tc(call_id: str)` (function) — Create a minimal tool_call dict.
- L21 `_tool_result(call_id: str, content: str='result')` (function) — Create a tool result message.
- L26 `_assistant_with_tools(*call_ids: str)` (function) — Create an assistant message with tool_calls.
- L31 `_make_compressor(**kwargs)` (function)
- L48 `TestAlignBoundaryBackward` (class) — Test that compress-end boundary never splits a tool_call/result group.
- L51 `test_boundary_at_clean_position(self)` (method) — Boundary after a user message — no adjustment needed.
- L67 `test_boundary_after_assistant_with_tools(self)` (method) — Original case: boundary right after assistant with tool_calls.
- L82 `test_boundary_in_middle_of_tool_results(self)` (method) — THE BUG: boundary falls between tool results of the same group.
- L103 `test_boundary_at_last_tool_result(self)` (method) — Boundary right after last tool result — messages[idx-1] is tool.
- L120 `test_boundary_with_consecutive_tool_groups(self)` (method) — Two consecutive tool groups — only walk back to the nearest parent.
- L143 `TestCompressionToolResultPreservation` (class) — Verify that compress() never silently drops tool results.
- L146 `test_parallel_tool_results_not_lost(self)` (method) — The exact scenario that triggered silent data loss before the fix.
