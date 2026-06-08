---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tui_gateway/test_goal_command.py

Symbols in `tests/tui_gateway/test_goal_command.py`.

- L22 `hermes_home(tmp_path, monkeypatch)` (function)
- L37 `server(hermes_home)` (function)
- L61 `session(server)` (function)
- L77 `_call(server, method, **params)` (function)
- L85 `test_goal_bare_shows_status_when_none_set(server, session)` (function)
- L92 `test_goal_whitespace_only_shows_status(server, session)` (function)
- L99 `test_goal_status_alias_shows_status(server, session)` (function)
- L106 `test_goal_set_returns_send_with_notice(server, session)` (function)
- L125 `test_goal_pause_after_set(server, session)` (function)
- L137 `test_goal_resume_reactivates(server, session)` (function)
- L150 `test_goal_clear_removes_active_goal(server, session)` (function)
- L168 `test_goal_stop_and_done_are_clear_aliases(server, session)` (function)
- L179 `test_goal_requires_session(server)` (function)
- L188 `test_slash_exec_rejects_goal_routes_to_command_dispatch(server, session)` (function) — slash.exec must reject /goal with 4018 so the TUI client falls through
- L199 `test_pending_input_commands_includes_goal(server)` (function) — Guard: _PENDING_INPUT_COMMANDS must list 'goal' — removing it would
