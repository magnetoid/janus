---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_session_db_private_access.py

Symbols in `tests/acp/test_session_db_private_access.py`.

- L22 `_tmp_db(tmp_path)` (function)
- L26 `_mock_agent()` (function)
- L34 `TestUpdateSessionMeta` (class) — Direct unit tests for the new public method.
- L37 `test_method_exists(self, tmp_path)` (method)
- L44 `test_updates_model_config(self, tmp_path)` (method)
- L56 `test_updates_model_when_provided(self, tmp_path)` (method)
- L65 `test_preserves_existing_model_when_none(self, tmp_path)` (method) — Passing model=None must leave the stored model unchanged (COALESCE).
- L75 `test_uses_execute_write_not_private_api(self, tmp_path)` (method) — update_session_meta must route through _execute_write, not _conn directly.
- L94 `test_noop_on_nonexistent_session(self, tmp_path)` (method) — Updating a non-existent session must not raise.
- L104 `TestNoPrviateDBAccess` (class) — _persist() in session.py must not access db._lock or db._conn.
- L107 `test_no_db_private_lock_access(self)` (method)
- L129 `test_persist_calls_update_session_meta(self)` (method) — AST check: _persist must call db.update_session_meta().
- L156 `TestPersistRoundTrip` (class) — End-to-end: save a session and verify DB state is correct.
- L159 `test_cwd_persisted_via_update_session_meta(self, tmp_path)` (method)
- L174 `test_model_persisted_via_update_session_meta(self, tmp_path)` (method)
- L185 `test_existing_model_not_cleared_on_save(self, tmp_path)` (method) — If state.model is empty, the DB model column must not be overwritten.
