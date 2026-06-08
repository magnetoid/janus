---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_model_reset.py

Symbols in `tests/gateway/test_session_model_reset.py`.

- L13 `_make_source()` (function)
- L23 `_make_event(text: str)` (function)
- L27 `_make_runner()` (function)
- L70 `test_new_command_clears_session_model_override()` (function) — /new must remove the session-scoped model override for that session.
- L94 `test_new_command_no_override_is_noop()` (function) — /new with no prior model override must not raise.
- L109 `test_new_command_only_clears_own_session()` (function) — /new must only clear the override for the session that triggered it.
