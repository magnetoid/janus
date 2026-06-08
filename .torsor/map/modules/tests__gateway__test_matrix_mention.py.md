---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_matrix_mention.py

Symbols in `tests/gateway/test_matrix_mention.py`.

- L18 `_make_adapter(tmp_path=None)` (function) — Create a MatrixAdapter with mocked config.
- L37 `_set_dm(adapter, room_id='!room1:example.org', is_dm=True)` (function) — Mark a room as DM (or not) in the adapter's cache.
- L42 `_make_event(body, sender='@alice:example.org', event_id='$evt1', room_id='!room1:example.org', formatted_body=None, thread_id=None, mention_user_ids=None)` (function) — Create a fake room message event.
- L86 `TestIsBotMentioned` (class)
- L87 `setup_method(self)` (method)
- L90 `test_full_user_id_in_body(self)` (method)
- L93 `test_localpart_in_body(self)` (method)
- L96 `test_localpart_case_insensitive(self)` (method)
- L99 `test_matrix_pill_in_formatted_body(self)` (method)
- L103 `test_no_mention(self)` (method)
- L106 `test_empty_body(self)` (method)
- L109 `test_partial_localpart_no_match(self)` (method)
- L116 `test_m_mentions_user_ids_authoritative(self)` (method) — m.mentions.user_ids alone is sufficient — no body text needed.
- L123 `test_m_mentions_user_ids_with_body_mention(self)` (method) — Both m.mentions and body mention — should still be True.
- L130 `test_m_mentions_user_ids_other_user_only(self)` (method) — m.mentions with a different user — bot is NOT mentioned.
- L137 `test_m_mentions_user_ids_empty_list(self)` (method) — Empty user_ids list — falls through to text detection.
- L144 `test_m_mentions_user_ids_none(self)` (method) — None mention_user_ids — falls through to text detection.
- L152 `TestStripMention` (class)
- L153 `setup_method(self)` (method)
- L156 `test_strip_full_user_id(self)` (method)
- L160 `test_localpart_preserved(self)` (method) — Bare localpart (no @) is preserved — avoids false positives in paths.
- L165 `test_localpart_in_path_preserved(self)` (method) — Localpart inside a file path must not be damaged.
- L170 `test_strip_localpart_when_explicit_at_mention(self)` (method)
- L174 `test_does_not_strip_bare_localpart_word(self)` (method)
- L179 `test_strip_returns_empty_for_mention_only(self)` (method)
- L189 `TestOutboundMentions` (class)
- L190 `setup_method(self)` (method)
- L197 `_sent_content(mock_client)` (method)
- L202 `test_send_adds_matrix_mentions_and_formatted_body(self)` (method)
- L217 `test_send_dedupes_mentions_and_ignores_code_spans(self)` (method)
- L228 `test_edit_message_preserves_mentions(self)` (method)
- L249 `test_send_simple_notice_adds_mentions(self)` (method)
- L268 `test_require_mention_default_ignores_unmentioned(monkeypatch)` (function) — Default (require_mention=true): messages without mention are ignored.
- L282 `test_require_mention_default_processes_mentioned(monkeypatch)` (function) — Default: messages with mention are processed, mention stripped.
- L298 `test_require_mention_html_pill(monkeypatch)` (function) — Bot mentioned via HTML pill should be processed.
- L313 `test_require_mention_m_mentions_user_ids(monkeypatch)` (function) — m.mentions.user_ids is authoritative per MSC3952 — no body mention needed.
- L334 `test_require_mention_m_mentions_other_user_ignored(monkeypatch)` (function) — m.mentions.user_ids mentioning another user should NOT activate the bot.
- L351 `test_require_mention_dm_always_responds(monkeypatch)` (function) — DMs always respond regardless of mention setting.
- L367 `test_dm_strips_full_mxid(monkeypatch)` (function) — DMs strip the full MXID from body when require_mention is on (default).
- L384 `test_dm_preserves_localpart_in_body(monkeypatch)` (function) — DMs no longer strip bare localpart — only the full MXID is removed.
- L401 `test_bare_mention_passes_empty_string(monkeypatch)` (function) — A message that is only a mention should pass through as empty, not be dropped.
- L417 `test_require_mention_free_response_room(monkeypatch)` (function) — Free-response rooms bypass mention requirement.
- L433 `test_require_mention_bot_participated_thread(monkeypatch)` (function) — Threads with prior bot participation bypass mention requirement.
- L449 `test_require_mention_disabled(monkeypatch)` (function) — MATRIX_REQUIRE_MENTION=false: all messages processed.
- L465 `test_require_mention_disabled_skips_stripping(monkeypatch)` (function) — MATRIX_REQUIRE_MENTION=false: mention text is NOT stripped from body.
- L486 `test_auto_thread_default_creates_thread(monkeypatch)` (function) — Default (auto_thread=true): sets thread_id to event.event_id.
- L501 `test_auto_thread_preserves_existing_thread(monkeypatch)` (function) — If message is already in a thread, thread_id is not overridden.
- L517 `test_auto_thread_skips_dm(monkeypatch)` (function) — DMs should not get auto-threaded.
- L533 `test_auto_thread_disabled(monkeypatch)` (function) — MATRIX_AUTO_THREAD=false: thread_id stays None.
- L548 `test_auto_thread_tracks_participation(monkeypatch)` (function) — Auto-created threads are tracked in _threads.
- L567 `TestThreadPersistence` (class)
- L568 `test_empty_state_file(self, tmp_path, monkeypatch)` (method) — No state file → empty set.
- L580 `test_track_thread_persists(self, tmp_path, monkeypatch)` (method) — mark() writes to disk.
- L596 `test_threads_survive_reload(self, tmp_path, monkeypatch)` (method) — Persisted threads are loaded by a new adapter instance.
- L611 `test_cap_max_tracked_threads(self, tmp_path, monkeypatch)` (method) — Thread set is trimmed to max_tracked.
- L637 `test_dm_mention_thread_disabled_by_default(monkeypatch)` (function) — Default (dm_mention_threads=false): DM with mention should NOT create a thread.
- L653 `test_dm_mention_thread_creates_thread(monkeypatch)` (function) — MATRIX_DM_MENTION_THREADS=true: DM with @mention creates a thread.
- L672 `test_dm_mention_thread_no_mention_no_thread(monkeypatch)` (function) — MATRIX_DM_MENTION_THREADS=true: DM without mention does NOT create a thread.
- L688 `test_dm_mention_thread_preserves_existing_thread(monkeypatch)` (function) — MATRIX_DM_MENTION_THREADS=true: DM already in a thread keeps that thread_id.
- L705 `test_dm_mention_thread_tracks_participation(monkeypatch)` (function) — DM mention-thread tracks the thread in _threads.
- L725 `TestMatrixConfigBridge` (class)
- L726 `test_yaml_bridge_sets_env_vars(self, monkeypatch, tmp_path)` (method) — Matrix YAML config should bridge to env vars.
- L774 `test_yaml_bridge_sets_dm_mention_threads(self, monkeypatch, tmp_path)` (method) — Matrix YAML dm_mention_threads should bridge to env var.
- L799 `test_env_vars_take_precedence_over_yaml(self, monkeypatch)` (method) — Env vars should not be overwritten by YAML values.
