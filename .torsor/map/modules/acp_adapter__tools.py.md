---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/tools.py

Symbols in `acp_adapter/tools.py`.

- L81 `get_tool_kind(tool_name: str)` (function) — Return the ACP ToolKind for a hermes tool, defaulting to 'other'.
- L86 `make_tool_call_id()` (function) — Generate a unique tool call ID.
- L91 `build_tool_title(tool_name: str, args: Dict[str, Any])` (function) — Build a human-readable title for a tool call.
- L183 `_text(content: str)` (function)
- L187 `_json_loads_maybe(value: Optional[str])` (function)
- L205 `_tool_result_failed(result: Optional[str], tool_name: str | None=None)` (function) — Return True when a structured Hermes tool result clearly failed.
- L243 `_truncate_text(text: str, limit: int=5000)` (function)
- L249 `_fenced_text(text: str, language: str='')` (function) — Return a Markdown fence that cannot be broken by backticks in text.
- L256 `_format_todo_result(result: Optional[str])` (function)
- L288 `_format_read_file_result(result: Optional[str], args: Optional[Dict[str, Any]])` (function)
- L315 `_format_search_files_result(result: Optional[str])` (function)
- L374 `_format_execute_code_result(result: Optional[str])` (function)
- L389 `_extract_markdown_headings(content: str, limit: int=8)` (function)
- L402 `_format_skill_view_result(result: Optional[str])` (function)
- L435 `_format_skill_manage_result(result: Optional[str], args: Optional[Dict[str, Any]])` (function)
- L465 `_format_web_search_result(result: Optional[str])` (function)
- L485 `_format_web_extract_result(result: Optional[str])` (function) — Return only web_extract errors for ACP; success stays compact via title.
- L516 `_format_process_result(result: Optional[str], args: Optional[Dict[str, Any]])` (function)
- L563 `_format_delegate_result(result: Optional[str])` (function)
- L609 `_format_session_search_result(result: Optional[str])` (function)
- L640 `_format_memory_result(result: Optional[str], args: Optional[Dict[str, Any]])` (function)
- L667 `_format_edit_result(tool_name: str, result: Optional[str], args: Optional[Dict[str, Any]])` (function)
- L690 `_format_browser_result(tool_name: str, result: Optional[str], args: Optional[Dict[str, Any]])` (function)
- L716 `_format_media_or_cron_result(tool_name: str, result: Optional[str])` (function)
- L729 `_format_structured_value(key: str, value: Any, *, indent: int=0, max_depth: int=3, max_items: int=8)` (function) — Render nested JSON-ish values as compact Markdown bullets, not inline blobs.
- L819 `_format_generic_structured_result(tool_name: str, result: Optional[str], *, fallback_to_text: bool=True)` (function)
- L871 `_build_polished_completion_content(tool_name: str, result: Optional[str], function_args: Optional[Dict[str, Any]])` (function)
- L910 `_strip_diff_prefix(path: str)` (function)
- L917 `_parse_unified_diff_content(diff_text: str)` (function) — Convert unified diff text into ACP diff content blocks.
- L976 `_build_tool_complete_content(tool_name: str, result: Optional[str], *, function_args: Optional[Dict[str, Any]]=None, snapshot: Any=None)` (function) — Build structured ACP completion content, falling back to plain text.
- L1017 `build_tool_start(tool_call_id: str, tool_name: str, arguments: Dict[str, Any], *, edit_diff: Any=None)` (function) — Create a ToolCallStart event for the given hermes tool invocation.
- L1245 `_is_structured_json_result(result: Optional[str])` (function)
- L1249 `build_tool_complete(tool_call_id: str, tool_name: str, result: Optional[str]=None, function_args: Optional[Dict[str, Any]]=None, snapshot: Any=None)` (function) — Create a ToolCallUpdate (progress) event for a completed tool call.
- L1282 `extract_locations(arguments: Dict[str, Any])` (function) — Extract file-system locations from tool arguments.
