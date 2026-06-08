---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_thread_fallback.py

Symbols in `tests/gateway/test_telegram_thread_fallback.py`.

- L33 `FakeNetworkError` (class)
- L37 `FakeBadRequest` (class)
- L41 `FakeTimedOut` (class)
- L45 `FakeRetryAfter` (class)
- L46 `__init__(self, seconds)` (method)
- L52 `_FakeInlineKeyboardButton` (class)
- L53 `__init__(self, text, callback_data=None, **kwargs)` (method)
- L59 `_FakeInlineKeyboardMarkup` (class)
- L60 `__init__(self, inline_keyboard)` (method)
- L64 `_FakeInputMediaPhoto` (class)
- L65 `__init__(self, media, caption=None, **kwargs)` (method)
- L109 `_inject_fake_telegram(monkeypatch)` (function) — Inject fake telegram modules so the adapter can import from them.
- L118 `_make_adapter()` (function)
- L138 `test_non_forum_group_reply_thread_id_does_not_fork_session_key()` (function) — Reply-derived thread ids in ordinary groups must not create topic lanes.
- L172 `test_forum_group_topic_message_preserves_thread_session_key()` (function) — Real Telegram forum-topic messages should still route by topic id.
- L202 `test_forum_general_topic_without_message_thread_id_keeps_thread_context()` (function) — Forum General-topic messages should keep synthetic thread context.
- L231 `test_send_omits_general_topic_thread_id()` (function) — Telegram sends to forum General should omit message_thread_id=1.
- L257 `test_send_typing_preserves_general_topic_thread_id()` (function) — Typing for forum General must send message_thread_id=1, not None.
- L285 `test_send_typing_does_not_fall_back_to_root_for_dm_topic()` (function) — Typing failures in DM topics should not show an indicator in All Messages.
- L304 `test_send_typing_attempts_api_call_for_dm_topic_reply_fallback()` (function) — Hermes-created DM topic lanes should still attempt scoped typing.
- L336 `test_send_typing_falls_back_without_thread_on_bad_request()` (function) — When DM topic typing with message_thread_id fails, retry without it.
- L375 `test_send_retries_without_thread_on_thread_not_found()` (function) — When message_thread_id keeps failing, retry once then fall back.
- L408 `test_send_retries_transient_thread_not_found_before_fallback()` (function) — A one-off Telegram thread-not-found response should still land in the topic.
- L438 `test_send_private_dm_topic_uses_direct_messages_topic_id()` (function) — Private Telegram topics route sends via direct_messages_topic_id.
- L460 `test_base_gateway_metadata_marks_telegram_dm_topics_as_reply_fallback()` (function)
- L477 `test_base_gateway_metadata_for_resumed_telegram_dm_topic_uses_direct_topic()` (function) — Resumed/synthetic DM-topic events may have no reply anchor.
- L494 `test_base_gateway_replies_to_triggering_message_for_telegram_dm_topic()` (function) — Private DM topic lanes should anchor replies to the active user message.
- L510 `test_gateway_runner_busy_ack_replies_to_triggering_message_for_telegram_dm_topic(monkeypatch, tmp_path)` (function) — GatewayRunner's duplicate thread metadata must match the base helper.
- L573 `test_send_uses_reply_fallback_for_hermes_dm_topics()` (function) — Hermes-created Telegram DM topics route with thread id plus reply anchor.
- L601 `test_send_uses_reply_anchor_when_direct_topic_fallback_metadata_exists()` (function) — Restart/update replay metadata keeps the anchor authoritative when present.
- L630 `test_send_created_private_topic_uses_message_thread_without_anchor()` (function) — Topics created via createForumTopic are addressable by message_thread_id directly.
- L657 `test_created_private_topic_thread_not_found_fails_without_root_fallback()` (function) — Created private-topic sends must not retry into All Messages on stale thread IDs.
- L684 `test_send_uses_metadata_reply_fallback_for_streaming_dm_topics()` (function) — Metadata-only sends still stay in Hermes-created Telegram DM topics.
- L712 `test_send_reply_fallback_applies_to_every_chunk_for_dm_topics()` (function) — Long Telegram DM-topic fallback sends must anchor every chunk.
- L741 `test_send_model_picker_uses_metadata_reply_fallback_for_dm_topics()` (function) — Inline keyboard sends also consume the metadata reply fallback.
- L774 `test_send_dm_topic_fallback_without_anchor_does_not_crash()` (function) — DM-topic fallback without an anchor uses direct topic routing.
- L802 `test_send_dm_topic_reply_not_found_fails_closed()` (function) — If Telegram deletes the reply anchor, private-topic sends must not fall back elsewhere.
- L841 `test_native_media_dm_topic_reply_not_found_retry_drops_thread_id(tmp_path, method_name, bot_method_name, path_kw, filename, payload)` (function)
- L881 `test_animation_dm_topic_reply_not_found_retry_drops_thread_id()` (function)
- L912 `test_media_group_dm_topic_reply_not_found_retry_drops_thread_id(tmp_path)` (function)
- L944 `test_send_image_url_dm_topic_reply_not_found_retry_drops_thread_id(monkeypatch)` (function)
- L978 `test_send_image_upload_dm_topic_reply_not_found_retry_drops_thread_id(monkeypatch)` (function)
- L1040 `test_slash_confirm_private_topic_callback_followup_sends_thread_and_reply(monkeypatch)` (function)
- L1082 `test_slash_confirm_forum_callback_followup_keeps_existing_thread_behavior(monkeypatch)` (function)
- L1125 `test_base_send_image_fallback_preserves_metadata()` (function) — Base image fallback should pass metadata through instead of referencing kwargs.
- L1158 `test_send_raises_on_other_bad_request()` (function) — Non-thread BadRequest errors should NOT be retried — they fail immediately.
- L1178 `test_send_without_thread_id_unaffected()` (function) — Normal sends without thread_id should work as before.
- L1202 `test_send_retries_network_errors_normally()` (function) — Real transient network errors (not BadRequest) should still be retried.
- L1226 `test_send_does_not_retry_timeout()` (function) — TimedOut (subclass of NetworkError) should NOT be retried in send().
- L1254 `test_send_retries_wrapped_connect_timeout()` (function) — Retry TimedOut only when it wraps a TCP connect timeout.
- L1286 `test_send_marks_wrapped_connect_timeout_retryable_after_exhaustion()` (function) — Final SendResult remains retryable for outer gateway retry handling.
- L1311 `test_send_retries_pool_timeout()` (function) — Retry TimedOut when it is an httpx pool-timeout (request not sent).
- L1342 `test_send_marks_pool_timeout_retryable_after_exhaustion()` (function) — Pool timeout that never clears stays retryable for outer retry handling.
- L1365 `test_thread_fallback_only_fires_once()` (function) — After clearing thread_id, subsequent chunks should also use None.
- L1396 `test_send_retries_retry_after_errors()` (function) — Telegram flood control should back off and retry instead of failing fast.
