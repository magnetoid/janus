---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_text_batching.py

Symbols in `tests/gateway/test_text_batching.py`.

- L24 `_make_event(text: str, platform: Platform, chat_id: str='12345', msg_type: MessageType=MessageType.TEXT)` (function)
- L41 `_make_discord_adapter()` (function) — Create a minimal DiscordAdapter for testing text batching.
- L60 `TestDiscordTextBatching` (class)
- L62 `test_single_message_dispatched_after_delay(self)` (method)
- L79 `test_split_messages_aggregated(self)` (method) — Two rapid messages from the same chat should be merged.
- L97 `test_three_way_split_aggregated(self)` (method)
- L115 `test_different_chats_not_merged(self)` (method)
- L126 `test_batch_cleans_up_after_flush(self)` (method)
- L135 `test_adaptive_delay_for_near_limit_chunk(self)` (method) — Chunks near the 2000-char limit should trigger longer delay.
- L151 `test_shield_protects_handle_message_from_cancel(self)` (method) — Regression guard: a follow-up chunk arriving while
- L219 `_make_matrix_adapter()` (function) — Create a minimal MatrixAdapter for testing text batching.
- L238 `TestMatrixTextBatching` (class)
- L240 `test_single_message_dispatched_after_delay(self)` (method)
- L253 `test_split_messages_aggregated(self)` (method)
- L269 `test_different_rooms_not_merged(self)` (method)
- L280 `test_adaptive_delay_for_near_limit_chunk(self)` (method) — Chunks near the 4000-char limit should trigger longer delay.
- L293 `test_batch_cleans_up_after_flush(self)` (method)
- L304 `_make_wecom_adapter()` (function) — Create a minimal WeComAdapter for testing text batching.
- L323 `TestWeComTextBatching` (class)
- L325 `test_single_message_dispatched_after_delay(self)` (method)
- L338 `test_split_messages_aggregated(self)` (method)
- L354 `test_different_chats_not_merged(self)` (method)
- L365 `test_adaptive_delay_for_near_limit_chunk(self)` (method) — Chunks near the 4000-char limit should trigger longer delay.
- L378 `test_batch_cleans_up_after_flush(self)` (method)
- L389 `_make_telegram_adapter()` (function) — Create a minimal TelegramAdapter for testing adaptive delay.
- L408 `TestTelegramAdaptiveDelay` (class)
- L410 `test_short_chunk_uses_normal_delay(self)` (method)
- L419 `test_near_limit_chunk_uses_split_delay(self)` (method) — A chunk near the 4096-char limit should trigger longer delay.
- L434 `test_split_continuation_merged(self)` (method) — Two near-limit chunks should both be merged.
- L453 `_make_feishu_adapter()` (function) — Create a minimal FeishuAdapter for testing adaptive delay.
- L476 `TestFeishuAdaptiveDelay` (class)
- L478 `test_short_chunk_uses_normal_delay(self)` (method)
- L487 `test_near_limit_chunk_uses_split_delay(self)` (method) — A chunk near the 4096-char limit should trigger longer delay.
- L501 `test_split_continuation_merged(self)` (method)
