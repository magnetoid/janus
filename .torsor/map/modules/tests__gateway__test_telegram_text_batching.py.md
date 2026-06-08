---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_text_batching.py

Symbols in `tests/gateway/test_telegram_text_batching.py`.

- L19 `_make_adapter()` (function) — Create a minimal TelegramAdapter for testing text batching.
- L37 `_make_event(text: str, chat_id: str='12345')` (function)
- L45 `TestTextBatching` (class)
- L47 `test_single_message_dispatched_after_delay(self)` (method)
- L64 `test_split_messages_aggregated(self)` (method) — Two rapid messages from the same chat should be merged.
- L84 `test_three_way_split_aggregated(self)` (method) — Three rapid messages should all merge.
- L103 `test_different_chats_not_merged(self)` (method) — Messages from different chats should be separate batches.
- L115 `test_batch_cleans_up_after_flush(self)` (method) — After flushing, internal state should be clean.
- L126 `test_dm_topic_batching_recovers_thread_before_keying(self)` (method) — DM-topic text batches should use the recovered topic lane.
