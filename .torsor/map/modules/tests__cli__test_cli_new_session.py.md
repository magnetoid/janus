---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_new_session.py

Symbols in `tests/cli/test_cli_new_session.py`.

- L17 `_FakeCompressor` (class) — Minimal stand-in for ContextCompressor.
- L20 `__init__(self)` (method)
- L28 `_FakeAgent` (class)
- L29 `__init__(self, session_id: str, session_start)` (method)
- L56 `reset_session_state(self)` (method) — Mirror the real AIAgent.reset_session_state().
- L78 `_make_cli(env_overrides=None, config_overrides=None, **kwargs)` (function) — Create a HermesCLI instance with minimal mocking.
- L124 `_prepare_cli_with_active_session(tmp_path)` (function)
- L144 `_reset_session_id_context()` (function)
- L152 `test_new_command_creates_real_fresh_session_and_resets_agent_state(tmp_path)` (function)
- L178 `test_new_command_rotates_hermes_session_id_env_and_context(tmp_path)` (function)
- L193 `test_reset_command_is_alias_for_new_session(tmp_path)` (function)
- L204 `test_clear_command_starts_new_session_before_redrawing(tmp_path)` (function)
- L220 `test_new_session_resets_token_counters(tmp_path)` (function) — Regression test for #2099: /new must zero all token counters.
- L255 `test_new_session_with_title(capsys)` (function) — new_session(title=...) creates a session and sets the title.
- L274 `test_new_session_with_duplicate_title_surfaces_error(capsys)` (function) — new_session(title=...) handles ValueError from a duplicate-title conflict.
