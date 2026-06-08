---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tui_gateway/test_undo_command.py

Symbols in `tests/tui_gateway/test_undo_command.py`.

- L27 `hermes_home(tmp_path, monkeypatch)` (function)
- L36 `server(hermes_home)` (function)
- L54 `db(hermes_home)` (function)
- L59 `session_with_history(server, db)` (function) — Build a session with 3 user turns + assistant replies persisted in DB.
- L87 `_call(server, method, **params)` (function)
- L91 `test_undo_returns_prefill_with_target_text(server, session_with_history)` (function)
- L101 `test_undo_truncates_in_memory_history(server, session_with_history, db)` (function)
- L113 `test_undo_n_backs_up_multiple_turns(server, session_with_history, db)` (function) — /undo 2 backs up two user turns to "question 2".
- L126 `test_undo_n_clamps_to_oldest_turn(server, session_with_history, db)` (function) — /undo with N larger than the number of user turns backs up to the oldest.
- L135 `test_undo_rejects_invalid_count(server, session_with_history)` (function)
- L142 `test_undo_soft_deletes_rows_in_db(server, session_with_history, db)` (function)
- L156 `test_undo_notifies_memory_provider(server, session_with_history)` (function)
- L166 `test_undo_refuses_when_session_busy(server, session_with_history)` (function)
- L174 `test_undo_errors_when_no_active_session(server)` (function)
- L180 `test_undo_in_pending_input_commands(server)` (function) — Registry sanity: /undo must be in _PENDING_INPUT_COMMANDS so
