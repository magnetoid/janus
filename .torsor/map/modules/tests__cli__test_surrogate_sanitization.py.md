---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_surrogate_sanitization.py

Symbols in `tests/cli/test_surrogate_sanitization.py`.

- L19 `TestSanitizeSurrogates` (class) — Test the _sanitize_surrogates() helper.
- L22 `test_normal_text_unchanged(self)` (method)
- L26 `test_empty_string(self)` (method)
- L29 `test_single_surrogate_replaced(self)` (method)
- L33 `test_multiple_surrogates_replaced(self)` (method)
- L37 `test_all_surrogate_range(self)` (method) — Verify the regex catches the full surrogate range.
- L44 `test_result_is_json_serializable(self)` (method) — Sanitized text must survive json.dumps + utf-8 encoding.
- L52 `test_original_surrogates_fail_encoding(self)` (method) — Confirm the original bug: surrogates crash utf-8 encoding.
- L60 `TestSanitizeMessagesSurrogates` (class) — Test the _sanitize_messages_surrogates() helper for message lists.
- L63 `test_clean_messages_returns_false(self)` (method)
- L70 `test_dirty_string_content_sanitized(self)` (method)
- L78 `test_dirty_multimodal_content_sanitized(self)` (method)
- L89 `test_mixed_clean_and_dirty(self)` (method)
- L100 `test_non_dict_items_skipped(self)` (method)
- L104 `test_tool_messages_sanitized(self)` (method) — Tool results could also contain surrogates from file reads etc.
- L113 `TestReasoningFieldSurrogates` (class) — Surrogates in reasoning fields (byte-level reasoning models).
- L122 `test_reasoning_field_sanitized(self)` (method)
- L130 `test_reasoning_content_field_sanitized(self)` (method) — api_messages carry `reasoning_content` built from `reasoning`.
- L139 `test_reasoning_details_nested_sanitized(self)` (method) — reasoning_details is a list of dicts with nested string fields.
- L157 `test_deeply_nested_reasoning_sanitized(self)` (method) — Nested dicts / lists inside extra fields are recursed into.
- L180 `test_reasoning_end_to_end_json_serialization(self)` (method) — After sanitization, the full message dict must serialize clean.
- L198 `test_no_surrogates_returns_false(self)` (method) — Clean reasoning fields don't trigger a modification.
- L212 `TestSanitizeStructureSurrogates` (class) — Test the _sanitize_structure_surrogates() helper for nested payloads.
- L215 `test_empty_payload(self)` (method)
- L219 `test_flat_dict(self)` (method)
- L225 `test_flat_list(self)` (method)
- L231 `test_nested_dict_in_list(self)` (method)
- L237 `test_deeply_nested(self)` (method)
- L248 `test_clean_payload_returns_false(self)` (method)
- L252 `test_non_string_values_ignored(self)` (method)
- L260 `TestApiMessagesSurrogateRecovery` (class) — Integration: verify the recovery block sanitizes api_messages.
- L270 `test_api_messages_reasoning_content_sanitized(self)` (method) — The extended sanitizer catches reasoning_content in api_messages.
- L293 `TestRunConversationSurrogateSanitization` (class) — Integration: verify run_conversation sanitizes user_message.
- L299 `test_user_message_surrogates_sanitized(self, mock_api, mock_stream, mock_sys)` (method) — Surrogates in user_message are stripped before API call.
