---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_whatsapp_formatting.py

Symbols in `tests/gateway/test_whatsapp_formatting.py`.

- L21 `_make_adapter()` (function) — Create a WhatsAppAdapter with test attributes (bypass __init__).
- L56 `_AsyncCM` (class) — Minimal async context manager returning a fixed value.
- L59 `__init__(self, value)` (method)
- L62 `__aenter__(self)` (method)
- L65 `__aexit__(self, *exc)` (method)
- L73 `TestFormatMessage` (class) — WhatsApp markdown conversion.
- L76 `test_bold_double_asterisk(self)` (method)
- L80 `test_bold_double_underscore(self)` (method)
- L84 `test_strikethrough(self)` (method)
- L88 `test_headers_converted_to_bold(self)` (method)
- L94 `test_links_converted(self)` (method)
- L99 `test_code_blocks_protected(self)` (method) — Code blocks should not have their content reformatted.
- L108 `test_inline_code_protected(self)` (method) — Inline code should not have its content reformatted.
- L116 `test_empty_content(self)` (method)
- L121 `test_plain_text_unchanged(self)` (method)
- L125 `test_already_whatsapp_italic(self)` (method) — Single *italic* should pass through unchanged.
- L131 `test_multiline_mixed(self)` (method)
- L145 `TestMessageLimits` (class) — WhatsApp message length limits.
- L148 `test_max_message_length_is_practical(self)` (method)
- L152 `test_chunk_limit_reserves_default_self_chat_prefix(self, monkeypatch)` (method)
- L161 `test_chunk_limit_does_not_reserve_prefix_in_bot_mode(self, monkeypatch)` (method)
- L172 `TestSendChunking` (class) — WhatsApp send() splits long messages into chunks.
- L176 `test_short_message_single_send(self)` (method)
- L188 `test_long_message_chunked(self)` (method)
- L203 `test_chunks_leave_room_for_bridge_prefix(self, monkeypatch)` (method)
- L221 `test_empty_message_no_send(self)` (method)
- L228 `test_whitespace_only_no_send(self)` (method)
- L235 `test_format_applied_before_send(self)` (method) — Markdown should be converted to WhatsApp format before sending.
- L250 `test_reply_to_only_on_first_chunk(self)` (method) — reply_to should only be set on the first chunk.
- L274 `test_bridge_error_returns_failure(self)` (method)
- L285 `test_not_connected_returns_failure(self)` (method)
- L298 `TestBridgeEventMetadata` (class) — WhatsApp bridge metadata is preserved for downstream consumers.
- L302 `test_quoted_reply_metadata_is_preserved_in_raw_message(self)` (method)
- L333 `TestWhatsAppTier` (class) — WhatsApp should be classified as TIER_MEDIUM.
- L336 `test_whatsapp_streaming_follows_global(self)` (method)
- L341 `test_whatsapp_tool_progress_is_new(self)` (method)
