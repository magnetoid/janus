---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/agent_runtime_helpers.py

Symbols in `agent/agent_runtime_helpers.py`.

- L45 `_ra()` (function) — Lazy ``run_agent`` reference for test-patch routing.
- L56 `agent_runtime_owns_post_tool_hook(agent: Any, function_name: str)` (function) — Return True when an agent-level tool path emits its own post hook.
- L66 `convert_to_trajectory_format(agent, messages: List[Dict[str, Any]], user_query: str, completed: bool)` (function) — Convert internal message format to trajectory format for saving.
- L237 `sanitize_tool_call_arguments(messages: list, *, logger=None, session_id: str=None)` (function) — Repair corrupted assistant tool-call argument JSON in-place.
- L347 `repair_message_sequence(agent, messages: List[Dict])` (function) — Collapse malformed role-alternation left in the live history.
- L449 `strip_think_blocks(agent, content: str)` (function) — Remove reasoning/thinking blocks from content, returning only visible text.
- L545 `recover_with_credential_pool(agent, *, status_code: Optional[int], has_retried_429: bool, classified_reason: Optional[FailoverReason]=None, error_context: Optional[Dict[str, Any]]=None)` (function) — Attempt credential recovery via pool rotation.
- L725 `try_recover_primary_transport(agent, api_error: Exception, *, retry_count: int, max_retries: int)` (function) — Attempt one extra primary-provider recovery cycle for transient transport failures.
- L809 `drop_thinking_only_and_merge_users(messages: List[Dict[str, Any]])` (function) — Drop thinking-only assistant turns; merge any adjacent user messages left behind.
- L895 `restore_primary_runtime(agent)` (function) — Restore the primary runtime at the start of a new turn.
- L991 `extract_reasoning(agent, assistant_message)` (function) — Extract reasoning/thinking content from an assistant message.
- L1073 `dump_api_request_debug(agent, api_kwargs: Dict[str, Any], *, reason: str, error: Optional[Exception]=None)` (function) — Dump a debug-friendly HTTP request record for the active inference API.
- L1154 `anthropic_prompt_cache_policy(agent, *, provider: Optional[str]=None, base_url: Optional[str]=None, api_mode: Optional[str]=None, model: Optional[str]=None)` (function) — Decide whether to apply Anthropic prompt caching and which layout to use.
- L1260 `create_openai_client(agent, client_kwargs: dict, *, reason: str, shared: bool)` (function)
- L1354 `switch_model(agent, new_model, new_provider, api_key='', base_url='', api_mode='')` (function) — Switch the model/provider in-place for a live agent.
- L1621 `invoke_tool(agent, function_name: str, function_args: dict, effective_task_id: str, tool_call_id: Optional[str]=None, messages: list=None, pre_tool_block_checked: bool=False, skip_tool_request_middleware: bool=False, tool_request_middleware_trace: Optional[List[Dict[str, Any]]]=None)` (function) — Invoke a single tool and return the result string. No display logic.
- L1822 `repair_tool_call(agent, tool_name: str)` (function) — Attempt to repair a mismatched tool name before aborting.
- L1896 `sanitize_api_messages(messages: List[Dict[str, Any]])` (function) — Fix orphaned tool_call / tool_result pairs before every LLM call.
- L1968 `looks_like_codex_intermediate_ack(agent, user_message: str, assistant_content: str, messages: List[Dict[str, Any]])` (function) — Detect a planning/ack message that should continue instead of ending the turn.
- L2042 `copy_reasoning_content_for_api(agent, source_msg: dict, api_msg: dict)` (function) — Copy provider-facing reasoning fields onto an API replay message.
- L2113 `reapply_reasoning_echo_for_provider(agent, api_messages: list)` (function) — Re-pad assistant turns with reasoning_content for the active provider.
- L2144 `_iter_pool_sockets(client: Any)` (function) — Yield raw sockets reachable from an OpenAI/httpx client pool.
- L2215 `cleanup_dead_connections(agent)` (function) — Detect and clean up dead TCP connections on the primary client.
- L2259 `extract_api_error_context(error: Exception)` (function) — Extract structured rate-limit details from provider errors.
- L2339 `apply_pending_steer_to_tool_results(agent, messages: list, num_tool_msgs: int)` (function) — Append any pending /steer text to the last tool result in this turn.
- L2404 `force_close_tcp_sockets(client: Any)` (function) — Abort in-flight TCP I/O by shutting down sockets WITHOUT closing FDs.
