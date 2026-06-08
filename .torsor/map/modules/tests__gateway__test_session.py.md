---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session.py

Symbols in `tests/gateway/test_session.py`.

- L23 `TestSessionSourceRoundtrip` (class)
- L24 `test_full_roundtrip(self)` (method)
- L45 `test_full_roundtrip_with_chat_topic(self)` (method) — chat_topic should survive to_dict/from_dict roundtrip.
- L63 `test_minimal_roundtrip(self)` (method)
- L71 `test_chat_id_coerced_to_string(self)` (method) — from_dict should handle numeric chat_id (common from Telegram).
- L80 `test_missing_optional_fields(self)` (method)
- L92 `test_unknown_platform_rejected_for_bad_names(self)` (method) — Arbitrary platform names are rejected (no accidental enum pollution).
- L102 `TestSessionSourceDescription` (class)
- L103 `test_local_cli(self)` (method)
- L110 `test_dm_with_username(self)` (method)
- L118 `test_dm_without_username_falls_back_to_user_id(self)` (method)
- L125 `test_group_shows_chat_name(self)` (method)
- L133 `test_channel_type(self)` (method)
- L141 `test_thread_id_appended(self)` (method)
- L150 `test_unknown_chat_type_uses_name(self)` (method)
- L158 `TestLocalCliFactory` (class)
- L159 `test_local_cli_defaults(self)` (method)
- L170 `TestBuildSessionContextPrompt` (class)
- L171 `test_telegram_prompt_contains_platform_and_chat(self)` (method)
- L197 `test_bluebubbles_prompt_mentions_short_conversational_i_message_format(self)` (method)
- L216 `test_discord_prompt(self)` (method)
- L238 `test_slack_prompt_includes_platform_notes(self)` (method)
- L259 `test_discord_prompt_with_channel_topic(self)` (method) — Channel topic should appear in the session context prompt.
- L283 `test_prompt_omits_channel_topic_when_none(self)` (method) — Channel Topic line should NOT appear when chat_topic is None.
- L305 `test_local_prompt_mentions_machine(self)` (method)
- L317 `test_local_delivery_path_uses_display_hermes_home(self)` (method)
- L330 `test_whatsapp_prompt(self)` (method)
- L347 `test_multi_user_thread_prompt(self)` (method) — Shared thread sessions show multi-user note instead of single user.
- L370 `test_non_thread_group_shows_user(self)` (method) — Regular group messages (no thread) still show the user name.
- L390 `test_shared_non_thread_group_prompt_hides_single_user(self)` (method) — Shared non-thread group sessions should avoid pinning one user.
- L412 `test_dm_thread_shows_user_not_multi(self)` (method) — DM threads are single-user and should show User, not multi-user note.
- L433 `TestSenderPrefixWithBackfill` (class) — Regression: sender prefix must not wrap the backfill context block.
- L442 `runner(self)` (method)
- L454 `source(self)` (method)
- L463 `test_plain_message_gets_prefix(self, runner, source)` (method) — Normal message without backfill gets [sender] prefix.
- L472 `test_backfill_prefix_only_on_trigger(self, runner, source)` (method) — Backfill context must NOT get the sender prefix.
- L487 `test_backfill_preserves_context_block(self, runner, source)` (method) — The backfill block should pass through unchanged — no double-prefixing.
- L503 `TestSessionStoreRewriteTranscript` (class) — Regression: /retry and /undo must persist truncated history to DB.
- L507 `store(self, tmp_path, monkeypatch)` (method)
- L514 `test_rewrite_replaces_transcript(self, store, tmp_path)` (method)
- L537 `test_rewrite_with_empty_list(self, store)` (method)
- L548 `TestLoadTranscriptDBOnly` (class) — After spec 002, load_transcript reads only from state.db.
- L551 `test_db_only_returns_empty_for_nonexistent(self, tmp_path, monkeypatch)` (method)
- L559 `test_db_only_returns_messages(self, tmp_path, monkeypatch)` (method)
- L575 `TestSessionStoreSwitchSession` (class) — Regression coverage for gateway /resume session switching semantics.
- L578 `test_switch_session_reopens_target_session_in_db(self, tmp_path)` (method)
- L614 `TestWhatsAppSessionKeyConsistency` (class) — Regression: WhatsApp session keys must collapse JID/LID aliases to a
- L619 `store(self, tmp_path)` (method)
- L627 `test_whatsapp_dm_uses_canonical_identifier(self)` (method)
- L637 `test_whatsapp_dm_aliases_share_one_session_key(self, tmp_path, monkeypatch)` (method)
- L663 `test_whatsapp_group_participant_aliases_share_session_key(self, tmp_path, monkeypatch)` (method) — With group_sessions_per_user, the same human flipping between
- L695 `test_whatsapp_group_shared_sessions_untouched_by_canonicalisation(self)` (method) — When group_sessions_per_user is False, participant_id is not in the
- L710 `test_store_delegates_to_build_session_key(self, store)` (method) — SessionStore._generate_session_key must produce the same result.
- L720 `test_store_creates_distinct_group_sessions_per_user(self, store)` (method)
- L743 `test_store_shares_group_sessions_when_disabled_in_config(self, store)` (method)
- L768 `test_telegram_dm_includes_chat_id(self)` (method) — Non-WhatsApp DMs should also include chat_id to separate users.
- L778 `test_distinct_dm_chat_ids_get_distinct_session_keys(self)` (method) — Different DM chats must not collapse into one shared session.
- L787 `test_discord_group_includes_chat_id(self)` (method) — Group/channel keys include chat_type and chat_id.
- L797 `test_group_sessions_are_isolated_per_user_when_user_id_present(self)` (method)
- L815 `test_group_sessions_can_be_shared_when_isolation_disabled(self)` (method)
- L832 `test_group_thread_includes_thread_id(self)` (method) — Forum-style threads need a distinct session key within one group.
- L843 `test_group_thread_sessions_are_shared_by_default(self)` (method) — Threads default to shared sessions — user_id is NOT appended.
- L863 `test_group_thread_sessions_can_be_isolated_per_user(self)` (method) — thread_sessions_per_user=True restores per-user isolation in threads.
- L875 `test_non_thread_group_sessions_still_isolated_per_user(self)` (method) — Regular group messages (no thread_id) remain per-user by default.
- L893 `test_discord_thread_sessions_shared_by_default(self)` (method) — Discord threads are shared across participants by default.
- L913 `test_dm_thread_sessions_not_affected(self)` (method) — DM threads use their own keying logic and are not affected.
- L927 `TestWhatsAppIdentifierPublicHelpers` (class) — Contract tests for the public WhatsApp identifier helpers.
- L935 `test_normalize_strips_jid_suffix(self)` (method)
- L938 `test_normalize_strips_lid_suffix(self)` (method)
- L941 `test_normalize_strips_device_suffix(self)` (method)
- L944 `test_normalize_strips_leading_plus(self)` (method)
- L947 `test_normalize_handles_bare_numeric(self)` (method)
- L950 `test_normalize_handles_empty_and_none(self)` (method)
- L954 `test_canonical_without_mapping_returns_normalized(self, tmp_path, monkeypatch)` (method) — With no bridge mapping files, the normalized input is returned.
- L959 `test_canonical_walks_lid_mapping(self, tmp_path, monkeypatch)` (method) — LID is resolved to its paired phone identity via lid-mapping files.
- L973 `test_canonical_empty_input(self, tmp_path, monkeypatch)` (method)
- L978 `TestSessionStoreEntriesAttribute` (class) — Regression: /reset must access _entries, not _sessions.
- L981 `test_entries_attribute_exists(self)` (method)
- L990 `TestHasAnySessions` (class) — Tests for has_any_sessions() fix (issue #351).
- L994 `store_with_mock_db(self, tmp_path)` (method) — SessionStore with a mocked database.
- L1004 `test_uses_database_count_when_available(self, store_with_mock_db)` (method) — has_any_sessions should use database session_count, not len(_entries).
- L1015 `test_first_session_ever_returns_false(self, store_with_mock_db)` (method) — First session ever should return False (only current session in DB).
- L1024 `test_fallback_without_database(self, tmp_path)` (method) — Should fall back to len(_entries) when DB is not available.
- L1040 `TestLastPromptTokens` (class) — Tests for the last_prompt_tokens field — actual API token tracking.
- L1043 `test_session_entry_default(self)` (method) — New sessions should have last_prompt_tokens=0.
- L1055 `test_session_entry_roundtrip(self)` (method) — last_prompt_tokens should survive serialization/deserialization.
- L1071 `test_session_entry_from_old_data(self)` (method) — Old session data without last_prompt_tokens should default to 0.
- L1087 `test_update_session_sets_last_prompt_tokens(self, tmp_path)` (method) — update_session should store the actual prompt token count.
- L1109 `test_update_session_none_does_not_change(self, tmp_path)` (method) — update_session with default (None) should not change last_prompt_tokens.
- L1132 `test_update_session_zero_resets(self, tmp_path)` (method) — update_session with last_prompt_tokens=0 should reset the field.
- L1155 `TestRewriteTranscriptPreservesReasoning` (class) — rewrite_transcript must not drop reasoning fields from SQLite.
- L1158 `test_reasoning_survives_rewrite(self, tmp_path)` (method)
- L1200 `test_db_rewrite_is_atomic_on_insert_failure(self, tmp_path, monkeypatch)` (method)
