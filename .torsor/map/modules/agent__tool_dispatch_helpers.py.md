---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/tool_dispatch_helpers.py

Symbols in `agent/tool_dispatch_helpers.py`.

- L79 `_is_destructive_command(cmd: str)` (function) — Heuristic: does this terminal command look like it modifies/deletes files?
- L90 `_is_mcp_tool_parallel_safe(tool_name: str)` (function) — Check if an MCP tool comes from a server with parallel tool calls enabled.
- L103 `_should_parallelize_tool_batch(tool_calls)` (function) — Return True when a tool-call batch is safe to run concurrently.
- L149 `_extract_parallel_scope_path(tool_name: str, function_args: dict)` (function) — Return the normalized file target for path-scoped tools.
- L166 `_paths_overlap(left: Path, right: Path)` (function) — Return True when two paths may refer to the same subtree.
- L177 `_is_multimodal_tool_result(value: Any)` (function) — True if the value is a multimodal tool result envelope.
- L191 `_multimodal_text_summary(value: Any)` (function) — Extract a plain text view of a multimodal tool result.
- L216 `_append_subdir_hint_to_multimodal(value: Dict[str, Any], hint: str)` (function) — Mutate a multimodal tool-result envelope to append a subdir hint.
- L237 `_extract_file_mutation_targets(tool_name: str, args: Dict[str, Any])` (function) — Return the file paths a ``write_file`` or ``patch`` call is targeting.
- L272 `_extract_error_preview(result: Any, max_len: int=180)` (function) — Pull a one-line error summary out of a tool result for footer display.
- L297 `_trajectory_normalize_msg(msg: Dict[str, Any])` (function) — Strip image blobs from a message for trajectory saving.
- L320 `make_tool_result_message(name: str, content: Any, tool_call_id: str)` (function) — Build a tool-result message dict with both the OpenAI-format ``name``
- L364 `_is_untrusted_tool(name: Optional[str])` (function)
- L372 `_maybe_wrap_untrusted(name: str, content: Any)` (function) — Wrap string content from high-risk tools in untrusted-data delimiters.
