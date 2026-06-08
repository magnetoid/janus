---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/observability/langfuse/__init__.py

Symbols in `plugins/observability/langfuse/__init__.py`.

- L44 `TraceState` (class)
- L74 `_env(name: str, default: str='')` (function)
- L78 `_env_bool(*names: str)` (function)
- L86 `_debug_enabled()` (function)
- L90 `_debug(message: str)` (function)
- L104 `_redact_key_preview(value: str)` (function) — Return a brief, log-safe preview of a credential value.
- L120 `_validate_langfuse_key(env_name: str, value: str)` (function) — Return an error message if ``value`` is not a real Langfuse key.
- L140 `_get_langfuse()` (function) — Return a cached Langfuse client, or ``None`` if unavailable.
- L222 `_trace_key(task_id: str, session_id: str)` (function)
- L230 `_truncate_text(value: str, max_chars: int)` (function)
- L236 `_maybe_parse_json_string(value: str)` (function)
- L262 `_looks_like_read_file_payload(value: Any)` (function)
- L276 `_parse_read_file_lines(content: str)` (function)
- L292 `_build_read_file_preview(lines: list[dict[str, Any]])` (function)
- L303 `_normalize_read_file_payload(value: dict[str, Any], *, args: Any=None)` (function)
- L355 `_normalize_payload(value: Any, *, tool_name: str='', args: Any=None)` (function)
- L364 `_safe_value(value: Any, *, max_chars: Optional[int]=None, depth: int=0, parse_json_strings: bool=False)` (function)
- L397 `_extract_last_user_message(messages: Any)` (function)
- L409 `_coerce_request_messages(*, request_messages: Any=None, messages: Any=None, conversation_history: Any=None, user_message: Any=None)` (function)
- L424 `_serialize_messages(messages: Any)` (function)
- L450 `_serialize_tool_calls(tool_calls: Any)` (function)
- L472 `_serialize_assistant_message(message: Any)` (function)
- L480 `_usage_and_cost(response: Any, *, provider: str, api_mode: str, model: str, base_url: str)` (function)
- L542 `_start_root_trace(task_key: str, *, task_id: str, session_id: str, platform: str, provider: str, model: str, api_mode: str, messages: Any, client: Langfuse)` (function)
- L606 `_start_child_observation(state: TraceState, *, client: Langfuse, name: str, as_type: str, input_value: Any, metadata: Optional[dict]=None, model: Optional[str]=None, model_parameters: Optional[dict]=None)` (function)
- L619 `_end_observation(observation: Any, *, output: Any=None, metadata: Optional[dict]=None, usage_details: Optional[dict]=None, cost_details: Optional[dict]=None)` (function)
- L640 `_merge_trace_output(output: Any, state: TraceState)` (function)
- L649 `_finish_trace(task_key: str, *, output: Any=None)` (function)
- L681 `_assistant_has_tool_calls(message: Any)` (function)
- L685 `_request_key(api_call_count: Any)` (function)
- L689 `on_pre_llm_call(*, task_id: str='', session_id: str='', platform: str='', model: str='', provider: str='', base_url: str='', api_mode: str='', api_call_count: int=0, messages: Any=None, turn_type: str='user', conversation_history: Any=None, user_message: Any=None, **_: Any)` (function)
- L729 `on_pre_llm_request(*, task_id: str='', session_id: str='', platform: str='', model: str='', provider: str='', base_url: str='', api_mode: str='', api_call_count: int=0, request_messages: Any=None, messages: Any=None, turn_type: str='user', message_count: int=0, tool_count: int=0, approx_input_tokens: int=0, request_char_count: int=0, max_tokens: Any=None, conversation_history: Any=None, user_message: Any=None, **_: Any)` (function)
- L801 `on_post_llm_call(*, task_id: str='', session_id: str='', provider: str='', base_url: str='', api_mode: str='', model: str='', api_call_count: int=0, assistant_message: Any=None, response: Any=None, api_duration: float=0.0, finish_reason: str='', usage: Any=None, assistant_content_chars: int=0, assistant_tool_call_count: int=0, assistant_response: Any=None, **_: Any)` (function)
- L921 `on_pre_tool_call(*, tool_name: str='', args: Any=None, task_id: str='', session_id: str='', tool_call_id: str='', **_: Any)` (function)
- L947 `on_post_tool_call(*, tool_name: str='', args: Any=None, result: Any=None, task_id: str='', session_id: str='', tool_call_id: str='', **_: Any)` (function)
- L995 `register(ctx)` (function)
