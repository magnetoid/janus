---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_session_boundary_hooks.py

Symbols in `tests/cli/test_session_boundary_hooks.py`.

- L7 `test_session_hooks_in_valid_hooks()` (function) — Verify on_session_finalize and on_session_reset are registered as valid hooks.
- L14 `test_session_finalize_on_reset(mock_invoke_hook)` (function) — Verify on_session_finalize fires when /new or /reset is used.
- L40 `test_session_finalize_on_cleanup(mock_invoke_hook)` (function) — Verify on_session_finalize fires during CLI exit cleanup.
- L61 `test_interrupted_session_end_helper_emits_observer_shape(mock_invoke_hook)` (function) — Verify quiet single-query interruption emits a correlated session end.
- L91 `test_hook_errors_are_caught(mock_invoke_hook)` (function) — Verify hook exceptions are caught and don't crash the agent.
