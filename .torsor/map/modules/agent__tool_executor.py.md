---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/tool_executor.py

Symbols in `agent/tool_executor.py`.

- L55 `_ra()` (function) — Lazy reference to ``run_agent`` so patches like ``run_agent._set_interrupt`` work.
- L61 `_emit_terminal_post_tool_call(agent, *, function_name: str, function_args: dict, result: Any, effective_task_id: str, tool_call_id: str, duration_ms: int=0, status: str | None=None, error_type: str | None=None, error_message: str | None=None, middleware_trace: Optional[list[dict[str, Any]]]=None)` (function)
- L96 `_cancelled_tool_result(reason: str='user interrupt')` (function)
- L106 `_emit_cancelled_terminal_post_tool_call(agent, *, function_name: str, function_args: dict, effective_task_id: str, tool_call_id: str, start_time: float, reason: str='user interrupt', error_type: str='keyboard_interrupt', middleware_trace: Optional[list[dict[str, Any]]]=None)` (function)
- L135 `_tool_search_scoped_names(agent)` (function) — Return the deferrable tool names the session may invoke via tool_call.
- L184 `_apply_tool_request_middleware_for_agent(agent, *, function_name: str, function_args: dict, effective_task_id: str, tool_call_id: str)` (function)
- L211 `_run_agent_tool_execution_middleware(agent, *, function_name: str, function_args: dict, effective_task_id: str, tool_call_id: str, execute)` (function)
- L243 `execute_tool_calls_concurrent(agent, assistant_message, messages: list, effective_task_id: str, api_call_count: int=0)` (function) — Execute multiple tool calls concurrently using a thread pool.
- L770 `execute_tool_calls_sequential(agent, assistant_message, messages: list, effective_task_id: str, api_call_count: int=0)` (function) — Execute tool calls sequentially (original behavior). Used for single calls or interactive tools.
