---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_compression_boundary_hook.py

Symbols in `tests/run_agent/test_compression_boundary_hook.py`.

- L21 `TestCompressionBoundaryHook` (class)
- L22 `_make_agent(self, session_db)` (method)
- L36 `test_on_session_start_called_with_compression_boundary(self)` (method)
- L93 `test_no_hook_when_no_session_db(self)` (method) — Without session_db, session_id does not rotate and the hook is not fired.
- L130 `test_hook_failure_does_not_break_compression(self)` (method) — If the context engine raises from on_session_start, compression still completes.
