---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# model_tools.py

Symbols in `model_tools.py`.

- L47 `_get_tool_loop()` (function) — Return a long-lived event loop for running async tool handlers.
- L62 `_get_worker_loop()` (function) — Return a persistent event loop for the current worker thread.
- L84 `_run_async(coro)` (function) — Run an async coroutine from a sync context.
- L257 `_clear_tool_defs_cache()` (function) — Drop memoized get_tool_definitions() results. Called when dynamic
- L264 `get_tool_definitions(enabled_toolsets: Optional[List[str]]=None, disabled_toolsets: Optional[List[str]]=None, quiet_mode: bool=False, skip_tool_search_assembly: bool=False)` (function) — Get tool definitions for model API calls with toolset-based filtering.
- L337 `_compute_tool_definitions(enabled_toolsets: Optional[List[str]]=None, disabled_toolsets: Optional[List[str]]=None, quiet_mode: bool=False, skip_tool_search_assembly: bool=False)` (function) — Uncached implementation of :func:`get_tool_definitions`.
- L526 `_resolve_active_context_length()` (function) — Look up the active model's context length for the tool-search gate.
- L586 `_sanitize_tool_error(error_msg: str)` (function) — Strip structural framing tokens from a tool error before showing it to the model.
- L606 `coerce_tool_args(tool_name: str, args: Dict[str, Any])` (function) — Coerce tool call arguments to match their JSON Schema types.
- L690 `_coerce_value(value: str, expected_type, schema: dict | None=None)` (function) — Attempt to coerce a string *value* to *expected_type*.
- L719 `_schema_allows_null(schema: dict | None)` (function) — Return True when a JSON Schema fragment explicitly permits null.
- L743 `_coerce_json(value: str, expected_python_type: type)` (function) — Parse *value* as JSON when the schema expects an array or object.
- L774 `_coerce_number(value: str, integer_only: bool=False)` (function) — Try to parse *value* as a number.  Returns original string on failure.
- L792 `_coerce_boolean(value: str)` (function) — Try to parse *value* as a boolean.  Returns original string on failure.
- L802 `_tool_result_observer_fields(result: Any)` (function)
- L812 `_emit_post_tool_call_hook(*, function_name: str, function_args: Dict[str, Any], result: Any, task_id: Optional[str]=None, session_id: Optional[str]=None, tool_call_id: Optional[str]=None, turn_id: Optional[str]=None, api_request_id: Optional[str]=None, duration_ms: int=0, status: Optional[str]=None, error_type: Optional[str]=None, error_message: Optional[str]=None, middleware_trace: Optional[List[Dict[str, Any]]]=None)` (function) — Emit the ``post_tool_call`` observer hook.
- L863 `handle_function_call(function_name: str, function_args: Dict[str, Any], task_id: Optional[str]=None, tool_call_id: Optional[str]=None, session_id: Optional[str]=None, turn_id: Optional[str]=None, api_request_id: Optional[str]=None, user_task: Optional[str]=None, enabled_tools: Optional[List[str]]=None, skip_pre_tool_call_hook: bool=False, skip_tool_request_middleware: bool=False, tool_request_middleware_trace: Optional[List[Dict[str, Any]]]=None, enabled_toolsets: Optional[List[str]]=None, disabled_toolsets: Optional[List[str]]=None)` (function) — Main function call dispatcher that routes calls to the tool registry.
- L1194 `get_all_tool_names()` (function) — Return all registered tool names.
- L1199 `get_toolset_for_tool(tool_name: str)` (function) — Return the toolset a tool belongs to.
- L1204 `get_available_toolsets()` (function) — Return toolset availability info for UI display.
- L1209 `check_toolset_requirements()` (function) — Return {toolset: available_bool} for every registered toolset.
- L1214 `check_tool_availability(quiet: bool=False)` (function) — Return (available_toolsets, unavailable_info).
