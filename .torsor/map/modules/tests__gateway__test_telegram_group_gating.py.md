---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_group_gating.py

Symbols in `tests/gateway/test_telegram_group_gating.py`.

- L11 `_make_adapter(require_mention=None, free_response_chats=None, mention_patterns=None, exclusive_bot_mentions=None, ignored_threads=None, allowed_topics=None, allow_from=None, group_allow_from=None, allowed_chats=None, group_allowed_chats=None, guest_mode=None, observe_unmentioned_group_messages=None, bot_username='hermes_bot')` (function)
- L88 `_group_message(text='hello', *, chat_id=-100, from_user_id=111, from_user_name='Alice Example', thread_id=None, reply_to_bot=False, entities=None, caption=None, caption_entities=None)` (function)
- L118 `_dm_message(text='hello', *, from_user_id=111)` (function)
- L133 `_mention_entity(text, mention='@hermes_bot')` (function)
- L138 `_mention_entities(text, mentions)` (function)
- L142 `_bot_command_entity(text, command)` (function) — Entity Telegram emits for a ``/cmd`` or ``/cmd@botname`` token.
- L153 `test_group_messages_can_be_opened_via_config()` (function)
- L159 `test_unmentioned_group_messages_can_be_observed_without_dispatching()` (function)
- L194 `test_observed_group_context_uses_shared_source_and_prompt_for_later_mentions()` (function)
- L228 `test_observed_group_context_replays_as_current_message_context_not_user_turns()` (function)
- L258 `test_observed_group_context_does_not_hide_current_user_turn_behind_history_offset()` (function)
- L284 `test_observed_group_context_wraps_multimodal_current_message_without_mutating_parts()` (function)
- L303 `test_observed_group_context_replays_normally_without_telegram_prompt()` (function)
- L316 `test_observed_group_context_preserves_slash_command_text_for_dispatch()` (function)
- L350 `test_unmentioned_group_observe_requires_chat_allowlist_for_shared_context()` (function)
- L373 `test_shared_group_observe_source_is_authorized_by_group_allowed_chats(monkeypatch)` (function)
- L391 `test_unmentioned_group_observe_respects_chat_allowlist()` (function)
- L415 `_FakeSessionEntry` (class)
- L419 `_FakeSessionStore` (class)
- L420 `__init__(self)` (method)
- L424 `get_or_create_session(self, source)` (method)
- L428 `append_to_transcript(self, session_id, message, skip_db=False)` (method)
- L432 `test_group_messages_can_require_direct_trigger_via_config()` (function)
- L473 `test_explicit_multi_bot_mentions_route_only_to_named_bots()` (function)
- L486 `test_entityless_multi_bot_mentions_still_route_exclusively()` (function)
- L498 `test_intern_bots_ignore_messages_addressed_to_other_intern_bot()` (function)
- L508 `test_bot_command_addressed_to_other_bot_is_exclusive_even_when_mentions_not_required()` (function)
- L519 `test_raw_bot_mention_fallback_does_not_match_email_or_substring()` (function)
- L527 `test_exclusive_bot_mentions_can_be_disabled_for_legacy_groups()` (function)
- L539 `test_free_response_chats_bypass_mention_requirement()` (function)
- L546 `test_guest_mode_allows_only_direct_mentions_outside_allowed_chats()` (function)
- L565 `test_guest_mode_defaults_to_false_for_allowed_chat_bypass()` (function)
- L576 `test_guest_mode_mention_dropped_in_ignored_thread()` (function) — A guest mention in an ignored thread is still dropped — thread gate runs first.
- L593 `test_ignored_threads_drop_group_messages_before_other_gates()` (function)
- L601 `test_allowed_topics_drop_other_forum_topics_before_other_gates()` (function)
- L611 `test_allowed_topics_do_not_filter_dms()` (function)
- L617 `test_allowed_topics_treat_missing_thread_as_general_topic()` (function)
- L624 `test_regex_mention_patterns_allow_custom_wake_words()` (function)
- L632 `test_invalid_regex_patterns_are_ignored()` (function)
- L639 `test_config_bridges_telegram_group_settings(monkeypatch, tmp_path)` (function)
- L694 `test_config_bridges_telegram_user_allowlists(monkeypatch, tmp_path)` (function)
- L722 `test_config_env_overrides_telegram_user_allowlists(monkeypatch, tmp_path)` (function)
- L743 `test_dm_allow_from_is_enforced_by_gateway_authorization_not_trigger_gate()` (function)
- L750 `test_group_allow_from_is_enforced_by_gateway_authorization_not_trigger_gate()` (function)
- L756 `test_top_level_require_mention_bridges_to_telegram(monkeypatch, tmp_path)` (function) — require_mention at the config.yaml top level (alongside group_sessions_per_user)
- L784 `test_top_level_require_mention_does_not_override_telegram_section(monkeypatch, tmp_path)` (function) — When telegram.require_mention is explicitly set, top-level require_mention
- L807 `test_config_bridges_telegram_ignored_threads(monkeypatch, tmp_path)` (function)
- L831 `_group_location_message(*, chat_id=-100, from_user_id=111, from_user_name='Alice Example', lat=37.7749, lon=-122.4194)` (function)
- L865 `_group_voice_message(*, chat_id=-100, from_user_id=111, from_user_name='Alice Example', caption=None)` (function)
- L904 `test_unmentioned_location_message_observed_in_group()` (function)
- L931 `test_triggered_location_message_uses_shared_session_in_observe_mode()` (function)
- L959 `test_unmentioned_voice_message_observed_in_group()` (function)
- L986 `test_triggered_voice_message_uses_shared_session_in_observe_mode()` (function)
- L1014 `_group_photo_message(*, chat_id=-100, caption='Veja esta foto', file_size=1024)` (function)
- L1030 `_group_document_message(*, chat_id=-100, caption='Este arquivo', document=None)` (function)
- L1050 `test_unmentioned_photo_observed_with_cached_path(monkeypatch, tmp_path)` (function)
- L1079 `test_unmentioned_document_observed_with_cached_path(monkeypatch, tmp_path)` (function)
- L1106 `test_unmentioned_large_document_observed_without_download(monkeypatch)` (function)
- L1136 `test_unmentioned_unsupported_document_observed_without_caching(monkeypatch)` (function)
