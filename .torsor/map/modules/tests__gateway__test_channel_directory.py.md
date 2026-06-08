---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_channel_directory.py

Symbols in `tests/gateway/test_channel_directory.py`.

- L20 `_write_directory(tmp_path, platforms)` (function) — Helper to write a fake channel directory.
- L28 `TestLoadDirectory` (class)
- L29 `test_missing_file(self, tmp_path)` (method)
- L35 `test_valid_file(self, tmp_path)` (method)
- L43 `test_corrupt_file(self, tmp_path)` (method)
- L51 `TestBuildChannelDirectoryWrites` (class)
- L52 `test_failed_write_preserves_previous_cache(self, tmp_path, monkeypatch)` (method)
- L72 `TestResolveChannelName` (class)
- L73 `_setup(self, tmp_path, platforms)` (method)
- L77 `test_exact_match(self, tmp_path)` (method)
- L88 `test_case_insensitive(self, tmp_path)` (method)
- L96 `test_guild_qualified_match(self, tmp_path)` (method)
- L107 `test_prefix_match_unambiguous(self, tmp_path)` (method)
- L118 `test_prefix_match_ambiguous_returns_none(self, tmp_path)` (method)
- L128 `test_no_channels_returns_none(self, tmp_path)` (method)
- L132 `test_no_match_returns_none(self, tmp_path)` (method)
- L139 `test_topic_name_resolves_to_composite_id(self, tmp_path)` (method)
- L146 `test_id_match_takes_precedence_over_name(self, tmp_path)` (method) — A raw channel ID resolves to itself, even when a different
- L161 `test_display_label_with_type_suffix_resolves(self, tmp_path)` (method)
- L175 `TestBuildFromSessions` (class)
- L176 `_write_sessions(self, tmp_path, sessions_data)` (method) — Write sessions.json at the path _build_from_sessions expects.
- L182 `test_builds_from_sessions_json(self, tmp_path)` (method)
- L216 `test_missing_sessions_file(self, tmp_path)` (method)
- L221 `test_deduplication_by_chat_id(self, tmp_path)` (method)
- L232 `test_keeps_distinct_topics_with_same_chat_id(self, tmp_path)` (method)
- L269 `TestFormatDirectoryForDisplay` (class)
- L270 `test_empty_directory(self, tmp_path)` (method)
- L275 `test_telegram_display(self, tmp_path)` (method)
- L291 `test_discord_grouped_by_guild(self, tmp_path)` (method)
- L307 `TestLookupChannelType` (class)
- L308 `_setup(self, tmp_path, platforms)` (method)
- L312 `test_forum_channel(self, tmp_path)` (method)
- L321 `test_regular_channel(self, tmp_path)` (method)
- L330 `test_unknown_chat_id_returns_none(self, tmp_path)` (method)
- L339 `test_unknown_platform_returns_none(self, tmp_path)` (method)
- L343 `test_channel_without_type_key_returns_none(self, tmp_path)` (method)
- L353 `_make_slack_adapter(team_clients)` (function) — Build a stand-in for SlackAdapter exposing only ``_team_clients``.
- L358 `_make_slack_client(pages)` (function) — Build an AsyncWebClient mock whose ``users_conversations`` returns pages.
- L365 `TestBuildSlack` (class) — _build_slack actually calls users.conversations on each workspace client.
- L368 `test_no_team_clients_falls_back_to_sessions(self, tmp_path)` (method)
- L381 `test_lists_channels_from_users_conversations(self, tmp_path)` (method)
- L402 `test_paginates_via_response_metadata_cursor(self, tmp_path)` (method)
- L421 `test_per_workspace_error_does_not_block_others(self, tmp_path)` (method)
- L436 `test_session_dms_merged_when_not_in_api_results(self, tmp_path)` (method)
- L458 `test_skips_channels_with_no_id_or_name(self, tmp_path)` (method)
- L475 `test_response_not_ok_breaks_pagination_for_that_workspace(self, tmp_path)` (method)
