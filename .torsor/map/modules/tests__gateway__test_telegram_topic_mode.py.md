---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_topic_mode.py

Symbols in `tests/gateway/test_telegram_topic_mode.py`.

- L19 `_make_source(*, thread_id: str | None=None)` (function)
- L30 `_make_event(text: str, *, thread_id: str | None=None)` (function)
- L38 `_make_group_source(*, thread_id: str | None=None)` (function)
- L49 `_make_group_event(text: str, *, thread_id: str | None=None)` (function)
- L57 `_make_runner(session_db=None)` (function)
- L161 `test_root_telegram_dm_prompt_is_system_lobby_when_topic_mode_enabled(monkeypatch)` (function)
- L183 `test_root_telegram_dm_new_shows_create_topic_instruction(monkeypatch)` (function)
- L207 `test_telegram_topic_prompt_still_runs_agent_when_topic_mode_enabled(monkeypatch)` (function)
- L225 `test_managed_topic_binding_reuses_restored_session_over_static_lane_session(tmp_path, monkeypatch)` (function)
- L270 `test_telegram_group_prompt_is_not_topic_lobby_even_when_dm_topic_mode_enabled(tmp_path, monkeypatch)` (function)
- L292 `test_topic_command_is_private_dm_only_and_does_not_enable_group_topic_mode(tmp_path, monkeypatch)` (function)
- L315 `test_group_new_keeps_existing_reset_semantics_when_dm_topic_mode_enabled(tmp_path, monkeypatch)` (function)
- L348 `test_new_inside_telegram_topic_resets_current_topic_with_parallel_tip(monkeypatch)` (function)
- L390 `test_new_inside_telegram_topic_rewrites_binding_to_new_session(tmp_path, monkeypatch)` (function) — Regression: /new inside a topic must rewrite the binding table.
- L452 `test_topic_binding_follows_compression_tip_on_read(tmp_path, monkeypatch)` (function) — Stale topic bindings auto-heal to the compression child on next inbound.
- L535 `test_topic_root_command_explicitly_migrates_and_enables_topic_mode(tmp_path, monkeypatch)` (function)
- L564 `test_topic_root_command_lists_unlinked_sessions_for_restore(tmp_path, monkeypatch)` (function)
- L617 `test_topic_root_command_handles_no_unlinked_sessions(tmp_path, monkeypatch)` (function)
- L639 `test_topic_command_inside_bound_topic_shows_current_session(tmp_path, monkeypatch)` (function)
- L675 `test_topic_restore_inside_topic_binds_old_session_and_returns_last_assistant_message(tmp_path, monkeypatch)` (function)
- L713 `test_topic_restore_refuses_session_owned_by_another_telegram_user(tmp_path, monkeypatch)` (function)
- L736 `test_topic_restore_refuses_already_linked_session(tmp_path, monkeypatch)` (function)
- L766 `test_first_message_inside_topic_records_topic_binding(tmp_path, monkeypatch)` (function)
- L800 `test_topic_root_command_creates_and_pins_system_topic(tmp_path, monkeypatch)` (function)
- L836 `test_auto_generated_title_renames_bound_telegram_topic(tmp_path)` (function)
- L864 `test_auto_generated_title_does_not_rename_topic_bound_to_other_session(tmp_path)` (function)
- L888 `test_operator_declared_topic_is_not_auto_renamed(tmp_path)` (function) — Topics registered in extra.dm_topics keep their operator-chosen name.
- L927 `test_disable_topic_auto_rename_extra_skips_rename(tmp_path)` (function) — extra.disable_topic_auto_rename=True must short-circuit auto-rename.
- L954 `test_schedule_topic_rename_respects_disable_flag(tmp_path)` (function) — The scheduling entry-point must also honour disable_topic_auto_rename.
- L983 `test_telegram_topic_auto_rename_disabled_string_truthy(tmp_path)` (function) — Common truthy string forms ('1', 'true', 'on', 'yes') must disable rename.
- L1005 `test_general_topic_is_treated_as_root_lobby(tmp_path)` (function) — Messages in the Telegram General topic (thread_id=1) route to the lobby, not a lane.
- L1024 `test_lobby_reminder_is_debounced_per_chat(tmp_path)` (function) — Consecutive root-DM prompts should only surface one lobby reminder per cooldown.
- L1044 `test_binding_survives_session_deletion_via_cascade(tmp_path)` (function) — Deleting a session with a topic binding must not raise FK errors.
- L1071 `test_migration_rebuilds_v1_binding_table_with_cascade_fk(tmp_path)` (function) — v1 → v2 migration rebuilds the bindings table when FK lacks ON DELETE CASCADE.
- L1123 `test_topic_help_subcommand_returns_usage(tmp_path)` (function) — /topic help surfaces usage without activating anything.
- L1144 `test_topic_off_disables_mode_and_clears_bindings(tmp_path, monkeypatch)` (function) — /topic off flips the row off AND deletes bindings for this chat.
- L1177 `test_topic_off_is_idempotent_when_never_enabled(tmp_path)` (function) — /topic off against a chat that never ran /topic is a no-op message.
- L1188 `test_topic_refuses_unauthorized_user(tmp_path, monkeypatch)` (function) — Unauthorized DMs cannot flip multi-session mode on.
- L1218 `_seed_two_topic_bindings(session_db)` (function) — Create two topics for the same user in topic mode, oldest first.
- L1251 `test_recover_returns_none_for_known_topic(tmp_path)` (function)
- L1259 `test_recover_preserves_unknown_thread_id_for_new_topic(tmp_path)` (function)
- L1270 `test_recover_rewrites_lobby_thread_id_to_most_recent(tmp_path)` (function)
- L1279 `test_recover_returns_none_when_topic_mode_disabled(tmp_path)` (function)
- L1287 `test_recover_returns_none_when_no_bindings_yet(tmp_path)` (function)
- L1295 `test_recover_returns_none_for_brand_new_topic(tmp_path)` (function)
- L1320 `test_list_telegram_topic_bindings_for_chat(tmp_path)` (function)
- L1327 `test_list_telegram_topic_bindings_for_chat_no_table(tmp_path)` (function)
- L1344 `test_get_telegram_topic_binding_by_session_returns_binding(tmp_path)` (function) — Reverse lookup by session_id returns the binding row.
- L1365 `test_get_telegram_topic_binding_by_session_returns_none_for_unknown(tmp_path)` (function) — Returns None when no binding exists for the given session_id.
- L1379 `test_session_split_restores_source_thread_id_from_binding(tmp_path)` (function) — After a session split, source.thread_id is restored from the binding.
