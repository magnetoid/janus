---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_protocol.py

Symbols in `tests/agent/lsp/test_protocol.py`.

- L38 `test_encode_message_uses_compact_separators_and_utf8()` (function)
- L56 `test_encode_message_handles_unicode_in_strings()` (function)
- L70 `_stream_from_bytes(data: bytes)` (function) — Build an asyncio.StreamReader pre-populated with ``data``.
- L79 `test_read_message_round_trip()` (function)
- L87 `test_read_message_clean_eof_returns_none()` (function)
- L93 `test_read_message_truncated_body_raises()` (function)
- L102 `test_read_message_missing_content_length_raises()` (function)
- L110 `test_read_message_two_messages_back_to_back()` (function)
- L119 `test_read_message_rejects_runaway_header()` (function) — A pathological server that streams headers without ever emitting
- L135 `test_make_request_includes_id_and_method()` (function)
- L140 `test_make_request_omits_params_when_none()` (function)
- L145 `test_make_notification_omits_id()` (function)
- L151 `test_make_response_carries_result()` (function)
- L156 `test_make_error_response_shape()` (function)
- L168 `test_classify_message_request()` (function)
- L173 `test_classify_message_response()` (function)
- L178 `test_classify_message_notification()` (function)
- L183 `test_classify_message_invalid()` (function)
- L193 `test_lsp_request_error_carries_code_and_data()` (function)
