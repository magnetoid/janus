---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_session.py

Symbols in `tests/acp/test_session.py`.

- L16 `_mock_agent()` (function)
- L21 `manager()` (function) — SessionManager with a mock agent factory (avoids needing API keys).
- L31 `TestCreateSession` (class)
- L32 `test_create_session_returns_state(self, manager)` (method)
- L40 `test_create_session_registers_task_cwd(self, manager, monkeypatch)` (method)
- L47 `test_register_task_cwd_translates_windows_drive_for_wsl_tools(self, monkeypatch)` (method)
- L67 `test_session_ids_are_unique(self, manager)` (method)
- L72 `test_get_session(self, manager)` (method)
- L77 `test_get_nonexistent_session_returns_none(self, manager)` (method)
- L88 `TestWslCwdTranslation` (class)
- L89 `test_translate_acp_cwd_converts_windows_drive_path_when_wsl(self, monkeypatch)` (method)
- L94 `test_translate_acp_cwd_handles_forward_slashes_when_wsl(self, monkeypatch)` (method)
- L99 `test_translate_acp_cwd_leaves_windows_drive_path_unchanged_off_wsl(self, monkeypatch)` (method)
- L104 `test_translate_acp_cwd_leaves_posix_path_unchanged_on_wsl(self, monkeypatch)` (method)
- L109 `test_create_session_stores_translated_cwd_on_wsl(self, manager, monkeypatch)` (method)
- L116 `test_fork_session_stores_translated_cwd_on_wsl(self, manager, monkeypatch)` (method)
- L125 `test_update_cwd_stores_translated_cwd_on_wsl(self, manager, monkeypatch)` (method)
- L139 `TestForkSession` (class)
- L140 `test_fork_session_deep_copies_history(self, manager)` (method)
- L157 `test_fork_session_has_new_id(self, manager)` (method)
- L163 `test_fork_nonexistent_returns_none(self, manager)` (method)
- L172 `TestListAndCleanup` (class)
- L173 `test_list_sessions_empty(self, manager)` (method)
- L176 `test_list_sessions_returns_created(self, manager)` (method)
- L187 `test_list_sessions_hides_empty_threads(self, manager)` (method)
- L191 `test_save_session_preserves_existing_messages_on_encode_failure(self, manager)` (method) — Regression for #13675: a bad message in state.history must not
- L216 `test_cleanup_clears_all(self, manager)` (method)
- L225 `test_remove_session(self, manager)` (method)
- L238 `TestPersistence` (class) — Verify that sessions are persisted to SessionDB and can be restored.
- L241 `test_create_session_includes_registered_mcp_toolsets(self, tmp_path, monkeypatch)` (method)
- L278 `test_create_session_writes_to_db(self, manager)` (method)
- L289 `test_get_session_restores_from_db(self, manager)` (method) — Simulate process restart: create session, drop from memory, get again.
- L313 `test_save_session_updates_db(self, manager)` (method)
- L323 `test_remove_session_deletes_from_db(self, manager)` (method)
- L330 `test_cleanup_removes_all_from_db(self, manager)` (method)
- L340 `test_list_sessions_includes_db_only(self, manager)` (method) — Sessions only in DB (not in memory) appear in list_sessions.
- L355 `test_list_sessions_filters_by_cwd(self, manager)` (method)
- L366 `test_list_sessions_matches_windows_and_wsl_paths(self, manager)` (method)
- L374 `test_list_sessions_prefers_title_then_preview(self, manager)` (method)
- L388 `test_list_sessions_sorted_by_most_recent_activity(self, manager)` (method)
- L402 `test_fork_restores_source_from_db(self, manager)` (method) — Forking a session that is only in DB should work.
- L418 `test_update_cwd_restores_from_db(self, manager)` (method)
- L435 `test_only_restores_acp_sessions(self, manager)` (method) — get_session should not restore non-ACP sessions from DB.
- L443 `test_sessions_searchable_via_fts(self, manager)` (method) — ACP sessions stored in SessionDB are searchable via FTS5.
- L456 `test_tool_calls_persisted(self, manager)` (method) — Messages with tool_calls should round-trip through the DB.
- L483 `test_assistant_reasoning_fields_persisted(self, manager)` (method) — ACP session restore should preserve assistant reasoning context.
- L516 `test_restore_preserves_persisted_provider_snapshot(self, tmp_path, monkeypatch)` (method) — Restored ACP sessions should keep their original runtime provider.
- L563 `test_acp_agents_route_human_output_to_stderr(self, tmp_path, monkeypatch)` (method) — ACP agents must keep stdout clean for JSON-RPC stdio transport.
