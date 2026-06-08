---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_api_server_normalize.py

Symbols in `tests/gateway/test_api_server_normalize.py`.

- L6 `TestNormalizeChatContent` (class) — Content normalization converts array-based content parts to plain text.
- L9 `test_none_returns_empty_string(self)` (method)
- L12 `test_plain_string_returned_as_is(self)` (method)
- L15 `test_empty_string_returned_as_is(self)` (method)
- L18 `test_text_content_part(self)` (method)
- L22 `test_input_text_content_part(self)` (method)
- L26 `test_output_text_content_part(self)` (method)
- L30 `test_multiple_text_parts_joined_with_newline(self)` (method)
- L37 `test_mixed_string_and_dict_parts(self)` (method)
- L41 `test_image_url_parts_silently_skipped(self)` (method)
- L48 `test_integer_content_converted(self)` (method)
- L51 `test_boolean_content_converted(self)` (method)
- L54 `test_deeply_nested_list_respects_depth_limit(self)` (method) — Nesting beyond max_depth returns empty string.
- L61 `test_large_list_capped(self)` (method) — Lists beyond MAX_CONTENT_LIST_SIZE are truncated.
- L68 `test_oversized_string_truncated(self)` (method) — Strings beyond 64KB are truncated.
- L74 `test_empty_text_parts_filtered(self)` (method)
- L82 `test_dict_without_type_skipped(self)` (method)
- L86 `test_empty_list_returns_empty(self)` (method)
