---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_mirror.py

Symbols in `tests/gateway/test_mirror.py`.

- L13 `_setup_sessions(tmp_path, sessions_data)` (function) — Helper to write a fake sessions.json and patch module-level paths.
- L22 `TestFindSessionId` (class)
- L23 `test_finds_matching_session(self, tmp_path)` (method)
- L38 `test_returns_most_recent(self, tmp_path)` (method)
- L58 `test_thread_id_disambiguates_same_chat(self, tmp_path)` (method)
- L78 `test_user_id_disambiguates_same_group_chat(self, tmp_path)` (method)
- L98 `test_ambiguous_same_group_chat_without_user_id_returns_none(self, tmp_path)` (method)
- L118 `test_no_match_returns_none(self, tmp_path)` (method)
- L132 `test_missing_sessions_file(self, tmp_path)` (method)
- L138 `test_platform_case_insensitive(self, tmp_path)` (method)
- L154 `TestMirrorToSession` (class)
- L155 `test_successful_mirror(self, tmp_path)` (method)
- L181 `test_successful_mirror_uses_thread_id(self, tmp_path)` (method)
- L204 `test_successful_mirror_uses_user_id_for_group_session(self, tmp_path)` (method)
- L233 `test_no_matching_session(self, tmp_path)` (method)
- L242 `test_error_returns_false(self, tmp_path)` (method)
- L249 `TestAppendToSqlite` (class)
- L250 `test_connection_is_closed_after_use(self, tmp_path)` (method) — Verify _append_to_sqlite closes the SessionDB connection.
- L261 `test_connection_closed_even_on_error(self, tmp_path)` (method) — Verify connection is closed even when append_message raises.
