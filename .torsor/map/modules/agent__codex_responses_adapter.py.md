---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/codex_responses_adapter.py

Symbols in `agent/codex_responses_adapter.py`.

- L26 `_classify_responses_issuer(*, is_xai_responses: bool=False, is_github_responses: bool=False, is_codex_backend: bool=False, base_url: Optional[str]=None)` (function) — Stable identifier for the Responses endpoint that mints encrypted_content.
- L79 `_chat_content_to_responses_parts(content: Any, *, role: str='user')` (function) — Convert chat-style multimodal content to Responses API input parts.
- L130 `_summarize_user_message_for_log(content: Any)` (function) — Return a short text summary of a user message for logging/trajectory.
- L175 `_deterministic_call_id(fn_name: str, arguments: str, index: int=0)` (function) — Generate a deterministic call_id from tool call content.
- L187 `_split_responses_tool_id(raw_id: Any)` (function) — Split a stored tool id into (call_id, response_item_id).
- L204 `_derive_responses_function_call_id(call_id: str, response_item_id: Optional[str]=None)` (function) — Build a valid Responses `function_call.id` (must start with `fc_`).
- L237 `_responses_tools(tools: Optional[List[Dict[str, Any]]]=None)` (function) — Convert chat-completions tool schemas to Responses function-tool schemas.
- L265 `_normalize_responses_message_status(value: Any, *, default: str='completed')` (function) — Normalize a Responses assistant message status for replay.
- L279 `_chat_messages_to_responses_input(messages: List[Dict[str, Any]], *, is_xai_responses: bool=False, replay_encrypted_reasoning: bool=True, current_issuer_kind: Optional[str]=None)` (function) — Convert internal chat-style messages to Responses input items.
- L552 `_preflight_codex_input_items(raw_items: Any)` (function)
- L762 `_preflight_codex_api_kwargs(api_kwargs: Any, *, allow_stream: bool=False)` (function)
- L949 `_extract_responses_message_text(item: Any)` (function) — Extract assistant text from a Responses message output item.
- L966 `_extract_responses_reasoning_text(item: Any)` (function) — Extract a compact reasoning text from a Responses reasoning item.
- L983 `_format_responses_error(error_obj: Any, response_status: str)` (function) — Build a human-readable error string from a Responses ``response.error`` payload.
- L1029 `_normalize_codex_response(response: Any, *, issuer_kind: Optional[str]=None)` (function) — Normalize a Responses API object to an assistant_message-like object.
