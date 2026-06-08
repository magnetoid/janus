---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_boundary_security_state.py

Symbols in `tests/gateway/test_session_boundary_security_state.py`.

- L23 `_clear_approval_state()` (function)
- L41 `_make_source()` (function)
- L51 `_make_event(text: str)` (function)
- L55 `_make_entry(session_id: str, source: SessionSource | None=None)` (function)
- L68 `_make_resume_runner()` (function)
- L95 `_make_branch_runner()` (function)
- L126 `test_resume_clears_session_scoped_approval_and_yolo_state()` (function)
- L159 `test_branch_clears_session_scoped_approval_and_yolo_state()` (function)
- L192 `test_branch_preserves_persisted_assistant_metadata()` (function)
- L223 `test_clear_session_boundary_security_state_is_scoped()` (function) — The helper must wipe only the target session's approval/yolo state.
- L289 `test_clear_session_boundary_security_state_wakes_blocked_approvals()` (function) — Boundary cleanup must cancel blocked approval waiters immediately.
