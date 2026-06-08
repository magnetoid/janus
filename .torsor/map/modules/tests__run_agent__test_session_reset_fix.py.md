---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_session_reset_fix.py

Symbols in `tests/run_agent/test_session_reset_fix.py`.

- L26 `_make_minimal_agent()` (function) — Return an AIAgent constructed with the absolute minimum args.
- L56 `TestResetSessionState` (class) — reset_session_state() must clear ALL session-scoped state.
- L59 `test_previous_summary_cleared_on_reset(self)` (method) — Compression summary from old session must not leak into new session.
- L80 `test_user_turn_count_cleared_on_reset(self)` (method) — Turn counter must reset to 0 on new session.
- L92 `test_both_fields_cleared_together(self)` (method) — Both stale fields are cleared in a single reset_session_state() call.
- L111 `test_reset_without_compressor_does_not_raise(self)` (method) — reset_session_state() must not raise when context_compressor is None.
