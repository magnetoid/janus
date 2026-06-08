---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_gemini_native_adapter.py

Symbols in `tests/agent/test_gemini_native_adapter.py`.

- L11 `DummyResponse` (class)
- L12 `__init__(self, status_code=200, payload=None, headers=None, text=None)` (method)
- L18 `json(self)` (method)
- L22 `test_build_native_request_preserves_thought_signature_on_tool_replay()` (function)
- L55 `test_build_native_request_uses_original_function_name_for_tool_result()` (function)
- L88 `test_build_native_request_strips_json_schema_only_fields_from_tool_parameters()` (function)
- L128 `test_translate_native_response_surfaces_reasoning_and_tool_calls()` (function)
- L158 `test_native_client_uses_x_goog_api_key_and_native_models_endpoint(monkeypatch)` (function)
- L201 `test_native_http_error_keeps_status_and_retry_after()` (function)
- L229 `test_native_client_accepts_injected_http_client()` (function)
- L237 `test_native_client_rejects_empty_api_key_with_actionable_message()` (function) — Empty/whitespace api_key must raise at construction, not produce a cryptic
- L251 `test_async_native_client_streams_without_requiring_async_iterator_from_sync_client()` (function)
- L279 `test_stream_event_translation_emits_tool_call_delta_with_stable_index()` (function)
- L307 `test_stream_event_translation_keeps_identical_calls_in_distinct_parts()` (function)
- L331 `test_max_tokens_none_defaults_to_gemini_output_ceiling()` (function) — max_tokens=None must send the model's full output ceiling, not omit it.
- L348 `test_explicit_max_tokens_is_respected()` (function)
