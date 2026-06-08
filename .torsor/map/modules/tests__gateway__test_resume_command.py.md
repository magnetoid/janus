---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_resume_command.py

Symbols in `tests/gateway/test_resume_command.py`.

- L16 `_make_event(text='/resume', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890')` (function) — Build a MessageEvent for testing.
- L28 `_session_key_for_event(event)` (function) — Get the session key that build_session_key produces for an event.
- L33 `_make_runner(session_db=None, current_session_id='current_session_001', event=None)` (function) — Create a bare GatewayRunner with a mock session_store and optional session_db.
- L64 `TestHandleResumeCommand` (class) — Tests for GatewayRunner._handle_resume_command.
- L68 `test_no_session_db(self)` (method) — Returns error when session database is unavailable.
- L76 `test_list_named_sessions_when_no_arg(self, tmp_path)` (method) — With no argument, lists recently titled sessions.
- L97 `test_list_shows_usage_when_no_titled(self, tmp_path)` (method) — With no arg and no titled sessions, shows instructions.
- L111 `test_resume_by_index(self, tmp_path)` (method) — Numeric argument resumes the indexed titled session from the list.
- L133 `test_resume_index_out_of_range(self, tmp_path)` (method) — Out-of-range numeric arguments show a helpful error.
- L152 `test_resume_by_name(self, tmp_path)` (method) — Resolves a title and switches to that session.
- L174 `test_resume_nonexistent_name(self, tmp_path)` (method) — Returns error for unknown session name.
- L187 `test_resume_already_on_session(self, tmp_path)` (method) — Returns friendly message when already on the requested session.
- L202 `test_resume_auto_lineage(self, tmp_path)` (method) — Asking for 'My Project' when 'My Project #2' exists gets the latest.
- L224 `test_resume_follows_compression_continuation(self, tmp_path)` (method) — Gateway /resume should reopen the live descendant after compression.
- L258 `test_resume_clears_running_agent(self, tmp_path)` (method) — Switching sessions clears any cached running agent.
- L279 `test_resume_evicts_cached_agent(self, tmp_path)` (method) — Gateway /resume evicts the cached AIAgent so the next message
- L306 `test_resume_strips_outer_brackets(self, tmp_path)` (method) — Users may copy `<session_id>` from the usage hint literally.
- L335 `test_resume_resolves_by_session_id(self, tmp_path)` (method) — The gateway should accept a bare session ID, not just a title.
