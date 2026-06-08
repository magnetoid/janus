---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_session_handoff.py

Symbols in `tests/hermes_cli/test_session_handoff.py`.

- L22 `TestHandoffStateDB` (class) — Test the handoff schema + helper methods on SessionDB.
- L26 `db(self, tmp_path, monkeypatch)` (method)
- L32 `_make_session(self, db, session_id, source='cli', title=None)` (method) — Insert a session row directly for testing.
- L42 `test_columns_exist(self, db)` (method)
- L48 `test_request_handoff_marks_pending(self, db)` (method)
- L61 `test_request_handoff_rejects_in_flight(self, db)` (method)
- L73 `test_request_handoff_after_terminal_state_resets_error(self, db)` (method)
- L87 `test_list_pending_handoffs_excludes_running_and_terminal(self, db)` (method)
- L104 `test_claim_handoff_is_atomic(self, db)` (method)
- L115 `test_complete_handoff_clears_error(self, db)` (method)
- L130 `test_fail_handoff_records_reason(self, db)` (method)
- L141 `test_fail_handoff_truncates_long_reasons(self, db)` (method)
- L154 `test_get_handoff_state_for_unknown_session(self, db)` (method)
- L157 `test_full_pending_to_completed_flow(self, db)` (method) — End-to-end sequence the CLI + gateway watcher follow.
- L186 `TestHandoffCommandRegistration` (class) — Slash-command surface checks.
- L189 `test_command_registered(self)` (method)
- L196 `test_command_is_cli_only(self)` (method) — `/handoff` is initiated from the CLI; gateway shouldn't expose it.
