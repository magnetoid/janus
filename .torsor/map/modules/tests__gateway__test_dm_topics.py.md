---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_dm_topics.py

Symbols in `tests/gateway/test_dm_topics.py`.

- L23 `_ensure_telegram_mock()` (function)
- L51 `_make_adapter(dm_topics_config=None, group_topics_config=None)` (function) — Create a TelegramAdapter with optional DM/group topics config.
- L67 `test_setup_dm_topics_loads_persisted_thread_ids()` (function) — Topics with thread_id in config should be loaded into cache, not created.
- L90 `test_setup_dm_topics_creates_when_no_thread_id()` (function) — Topics without thread_id should be created via API.
- L120 `test_setup_dm_topics_mixed_persisted_and_new()` (function) — Mix of persisted and new topics should work correctly.
- L147 `test_setup_dm_topics_skips_empty_config()` (function) — Empty dm_topics config should be a no-op.
- L159 `test_setup_dm_topics_no_config()` (function) — No dm_topics in config at all should be a no-op.
- L173 `test_create_dm_topic_handles_duplicate_error()` (function) — Duplicate topic error should return None gracefully.
- L185 `test_create_dm_topic_handles_generic_error()` (function) — Generic error should return None with warning.
- L197 `test_create_dm_topic_returns_none_without_bot()` (function) — No bot instance should return None.
- L208 `test_ensure_dm_topic_creates_on_demand_and_persists()` (function) — Named delivery targets should create missing private DM topics on demand.
- L232 `test_ensure_dm_topic_force_create_replaces_persisted_thread_id()` (function) — Refreshing a stale named topic should replace the cached persisted thread_id.
- L258 `test_persist_dm_topic_thread_id_writes_config(tmp_path)` (function) — Should write thread_id into the correct topic in config.yaml.
- L299 `test_persist_dm_topic_thread_id_skips_if_already_set(tmp_path)` (function) — Should not overwrite an existing thread_id.
- L337 `test_persist_dm_topic_thread_id_replaces_existing_when_requested(tmp_path)` (function) — Forced refresh should overwrite a stale persisted thread_id.
- L379 `test_persist_dm_topic_thread_id_preserves_config_on_write_failure(tmp_path)` (function) — Failed writes should leave the original config.yaml intact.
- L421 `test_get_dm_topic_info_finds_cached_topic()` (function) — Should return topic config when thread_id is in cache.
- L440 `test_get_dm_topic_info_returns_none_for_unknown()` (function) — Should return None for unknown thread_id.
- L456 `test_get_dm_topic_info_returns_none_without_config()` (function) — Should return None if no dm_topics config.
- L466 `test_get_dm_topic_info_returns_none_for_none_thread()` (function) — Should return None if thread_id is None.
- L477 `test_get_dm_topic_info_hot_reloads_from_config(tmp_path)` (function) — Should find a topic added to config after startup (hot-reload).
- L521 `test_cache_dm_topic_from_message()` (function) — Should cache a new topic mapping.
- L530 `test_cache_dm_topic_from_message_no_overwrite()` (function) — Should not overwrite an existing cached topic.
- L543 `_make_mock_message(chat_id=111, chat_type='private', text='hello', thread_id=None, user_id=42, user_name='Test User', forum_topic_created=None, is_topic_message=None, is_forum=None)` (function) — Create a mock Telegram Message for _build_message_event tests.
- L580 `test_build_message_event_sets_auto_skill()` (function) — When topic has a skill binding, auto_skill should be set on the event.
- L602 `test_build_message_event_no_auto_skill_without_binding()` (function) — Topics without skill binding should have auto_skill=None.
- L623 `test_build_message_event_no_auto_skill_without_thread()` (function) — Regular DM messages (no thread_id) should have auto_skill=None.
- L634 `test_build_message_event_filters_non_topic_dm_thread_id()` (function) — A DM reply-thread id should not be persisted unless Telegram marks it as a topic message.
- L647 `test_build_message_event_preserves_true_dm_topic_thread_id()` (function) — True DM topic messages should keep their thread id for routing.
- L677 `test_group_topic_skill_binding()` (function) — Group topic with skill config should set auto_skill on the event.
- L705 `test_group_topic_skill_binding_second_topic()` (function) — A different thread_id in the same group should resolve its own skill.
- L733 `test_group_topic_no_skill_binding()` (function) — Group topic without a skill key should have auto_skill=None but set chat_topic.
- L760 `test_group_topic_unmapped_thread_id()` (function) — Thread ID not in config should fall through — no skill, no topic name.
- L787 `test_group_topic_unmapped_chat_id()` (function) — Chat ID not in group_topics config should fall through silently.
- L814 `test_group_topic_no_config()` (function) — No group_topics config at all should be fine — no skill, no topic.
- L829 `test_group_topic_chat_id_int_string_coercion()` (function) — chat_id as string in config should match integer chat.id via str() coercion.
- L859 `test_build_message_event_dm_from_user_none_falls_back_to_chat_id()` (function) — When from_user is None in a DM, user_id should fall back to chat.id.
- L875 `test_build_message_event_group_from_user_none_stays_none()` (function) — When from_user is None in a group, user_id should remain None.
- L893 `test_build_message_event_dm_from_user_present_uses_user()` (function) — When from_user is present in a DM, it should be used (no fallback).
