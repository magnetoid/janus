---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_boundary_hooks.py

Symbols in `tests/gateway/test_session_boundary_hooks.py`.

- L13 `_make_source()` (function)
- L23 `_make_event(text: str)` (function)
- L27 `_make_runner()` (function)
- L78 `test_reset_fires_finalize_hook(mock_invoke_hook)` (function) — /new must fire on_session_finalize with the OLD session id.
- L96 `test_reset_fires_reset_hook(mock_invoke_hook)` (function) — /new must fire on_session_reset with the NEW session id.
- L114 `test_finalize_before_reset(mock_invoke_hook)` (function) — on_session_finalize must fire before on_session_reset.
- L128 `test_shutdown_fires_finalize_for_active_agents(mock_invoke_hook)` (function) — Gateway stop() must fire on_session_finalize for each active agent.
- L171 `test_hook_error_does_not_break_reset(mock_invoke_hook)` (function) — Plugin hook errors must not prevent /new from completing.
- L183 `test_idle_expiry_fires_finalize_hook(mock_invoke_hook)` (function) — Regression test for #14981.
