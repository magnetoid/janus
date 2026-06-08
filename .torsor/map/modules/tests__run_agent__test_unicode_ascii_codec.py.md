---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_unicode_ascii_codec.py

Symbols in `tests/run_agent/test_unicode_ascii_codec.py`.

- L18 `TestStripNonAscii` (class) — Tests for _strip_non_ascii helper.
- L21 `test_ascii_only(self)` (method)
- L24 `test_removes_non_ascii(self)` (method)
- L27 `test_removes_emoji(self)` (method)
- L30 `test_chinese_chars(self)` (method)
- L33 `test_empty_string(self)` (method)
- L36 `test_only_non_ascii(self)` (method)
- L40 `TestSanitizeMessagesNonAscii` (class) — Tests for _sanitize_messages_non_ascii.
- L43 `test_no_change_ascii_only(self)` (method)
- L48 `test_sanitizes_content_string(self)` (method)
- L53 `test_sanitizes_content_list(self)` (method)
- L61 `test_sanitizes_name_field(self)` (method)
- L66 `test_sanitizes_tool_calls(self)` (method)
- L82 `test_handles_non_dict_messages(self)` (method)
- L86 `test_empty_messages(self)` (method)
- L89 `test_multiple_messages(self)` (method)
- L101 `TestSurrogateVsAsciiSanitization` (class) — Test that surrogate and ASCII sanitization work independently.
- L104 `test_surrogates_still_handled(self)` (method) — Surrogates are caught by _sanitize_messages_surrogates, not _non_ascii.
- L112 `test_surrogates_in_name_and_tool_calls_are_sanitized(self)` (method)
- L132 `test_ascii_codec_strips_all_non_ascii(self)` (method) — ASCII codec case: all non-ASCII is stripped, not replaced.
- L139 `test_no_surrogates_returns_false(self)` (method) — When no surrogates present, _sanitize_messages_surrogates returns False.
- L145 `TestApiKeyNonAsciiSanitization` (class) — Tests for API key sanitization in the UnicodeEncodeError recovery.
- L153 `test_strip_non_ascii_from_api_key(self)` (method) — _strip_non_ascii removes ʋ from an API key string.
- L158 `test_api_key_at_position_153(self)` (method) — Reproduce the exact error: ʋ at position 153 in 'Bearer <key>'.
- L172 `TestSanitizeToolsNonAscii` (class) — Tests for _sanitize_tools_non_ascii.
- L175 `test_sanitizes_tool_description_and_parameter_descriptions(self)` (method)
- L199 `test_no_change_for_ascii_only_tools(self)` (method)
- L222 `TestSanitizeStructureNonAscii` (class)
- L223 `test_sanitizes_nested_dict_structure(self)` (method)
- L235 `TestApiKeyClientSync` (class) — Verify that ASCII recovery updates the live OpenAI client's api_key.
- L244 `test_client_api_key_updated_on_sanitize(self)` (method) — Simulate the recovery path and verify client.api_key is synced.
- L279 `test_client_none_does_not_crash(self)` (method) — Recovery should not crash when client is None (pre-init).
- L299 `TestApiMessagesAndApiKwargsSanitized` (class) — Regression tests for #6843 follow-up: api_messages and api_kwargs must
- L311 `test_api_messages_with_reasoning_content_is_sanitized(self)` (method) — api_messages may contain reasoning_content not in messages.
- L329 `test_api_kwargs_with_non_ascii_extra_body_is_sanitized(self)` (method) — api_kwargs may contain non-ASCII in extra_body or other fields.
- L342 `test_messages_clean_but_api_messages_dirty_both_get_sanitized(self)` (method) — Even when canonical messages are clean, api_messages may be dirty.
- L359 `test_reasoning_field_in_canonical_messages_is_sanitized(self)` (method) — The canonical messages list stores reasoning as 'reasoning', not
