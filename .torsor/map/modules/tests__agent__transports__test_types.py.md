---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_types.py

Symbols in `tests/agent/transports/test_types.py`.

- L18 `TestToolCall` (class)
- L19 `test_basic_construction(self)` (method)
- L26 `test_none_id(self)` (method)
- L30 `test_provider_data(self)` (method)
- L45 `TestUsage` (class)
- L46 `test_defaults(self)` (method)
- L53 `test_explicit(self)` (method)
- L62 `TestNormalizedResponse` (class)
- L63 `test_text_only(self)` (method)
- L72 `test_with_tool_calls(self)` (method)
- L79 `test_with_reasoning(self)` (method)
- L88 `test_with_provider_data(self)` (method)
- L102 `TestBuildToolCall` (class)
- L103 `test_dict_arguments_serialized(self)` (method)
- L108 `test_string_arguments_passthrough(self)` (method)
- L112 `test_provider_fields(self)` (method)
- L122 `test_none_id(self)` (method)
- L131 `TestMapFinishReason` (class)
- L140 `test_known_reason(self)` (method)
- L146 `test_unknown_reason_defaults_to_stop(self)` (method)
- L149 `test_none_reason(self)` (method)
- L157 `TestToolCallBackwardCompat` (class) — Test duck-typing properties that let ToolCall pass through code expecting
- L161 `test_type_is_function(self)` (method)
- L165 `test_function_returns_self(self)` (method)
- L169 `test_function_name_matches(self)` (method)
- L174 `test_function_arguments_matches(self)` (method)
- L179 `test_call_id_from_provider_data(self)` (method)
- L183 `test_call_id_none_when_no_provider_data(self)` (method)
- L187 `test_response_item_id_from_provider_data(self)` (method)
- L191 `test_response_item_id_none_when_missing(self)` (method)
- L195 `test_getattr_pattern_matches_agent_loop(self)` (method) — run_agent.py uses getattr(tool_call, 'call_id', None) — verify it works.
- L202 `test_extra_content_from_provider_data(self)` (method) — Gemini thought_signature stored in provider_data is exposed via property.
- L208 `test_extra_content_none_when_no_provider_data(self)` (method)
- L212 `test_extra_content_none_when_key_absent(self)` (method)
- L216 `test_extra_content_getattr_pattern(self)` (method) — _build_assistant_message uses getattr(tc, 'extra_content', None).
- L232 `TestNormalizedResponseBackwardCompat` (class) — Test properties that replaced _nr_to_assistant_message() shim.
- L235 `test_reasoning_content_from_provider_data(self)` (method)
- L242 `test_reasoning_content_none_when_absent(self)` (method)
- L246 `test_reasoning_details_from_provider_data(self)` (method)
- L254 `test_reasoning_details_none_when_no_provider_data(self)` (method)
- L261 `test_codex_reasoning_items_from_provider_data(self)` (method)
- L269 `test_codex_reasoning_items_none_when_absent(self)` (method)
- L273 `test_codex_message_items_from_provider_data(self)` (method)
- L281 `test_codex_message_items_none_when_absent(self)` (method)
