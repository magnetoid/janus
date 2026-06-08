---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_session_id_env.py

Symbols in `tests/run_agent/test_session_id_env.py`.

- L14 `_cleanup_env()` (function) — Remove HERMES_SESSION_ID before/after each test.
- L21 `test_session_id_env_set_on_init()` (function) — AIAgent.__init__ sets HERMES_SESSION_ID in the environment.
- L34 `test_session_id_env_uses_provided_id()` (function) — When session_id is passed explicitly, HERMES_SESSION_ID reflects it.
- L49 `test_session_id_contextvar_set()` (function) — AIAgent.__init__ also sets the ContextVar for concurrency safety.
