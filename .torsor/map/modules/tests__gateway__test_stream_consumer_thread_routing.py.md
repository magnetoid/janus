---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_stream_consumer_thread_routing.py

Symbols in `tests/gateway/test_stream_consumer_thread_routing.py`.

- L19 `_make_adapter(send_result=None, edit_result=None, max_length=4096)` (function)
- L31 `TestInitialReplyToId` (class) — Verify initial_reply_to_id is passed as reply_to on first send.
- L35 `test_first_send_uses_initial_reply_to_id(self)` (method) — When initial_reply_to_id is set, first adapter.send() should
- L55 `test_first_send_without_initial_reply_to_id(self)` (method) — When initial_reply_to_id is None, first send should have
- L70 `test_subsequent_edits_ignore_initial_reply_to_id(self)` (method) — After first send, edits should use message_id, not initial_reply_to_id.
- L93 `test_metadata_passed_on_first_send(self)` (method) — Metadata (containing thread_id) should be forwarded on first send.
- L109 `TestOverflowFirstMessage` (class) — Verify thread routing is preserved when the first message overflows.
- L113 `test_overflow_first_send_uses_initial_reply_to_id(self)` (method) — When first message exceeds platform limit and is split into chunks,
- L139 `TestFeishuFallbackThreadRouting` (class) — Verify FeishuAdapter._send_raw_message routes to topic on fallback.
- L143 `test_create_uses_thread_id_when_available(self)` (method) — When reply_to=None and metadata has thread_id, message.create
- L200 `test_create_uses_chat_id_when_no_thread(self)` (method) — When reply_to=None and metadata has no thread_id, message.create
