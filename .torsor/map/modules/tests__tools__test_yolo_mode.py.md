---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_yolo_mode.py

Symbols in `tests/tools/test_yolo_mode.py`.

- L22 `_clear_approval_state()` (function)
- L36 `TestYoloMode` (class) — When HERMES_YOLO_MODE is set, all dangerous commands are auto-approved.
- L39 `test_dangerous_command_blocked_normally(self, monkeypatch)` (method) — Without yolo mode, dangerous commands in interactive mode require approval.
- L57 `test_dangerous_command_approved_in_yolo_mode(self, monkeypatch)` (method) — With HERMES_YOLO_MODE, dangerous commands are auto-approved.
- L70 `test_yolo_mode_works_for_all_patterns(self, monkeypatch)` (method) — Yolo mode bypasses all dangerous patterns, not just some.
- L91 `test_combined_guard_bypasses_yolo_mode(self, monkeypatch)` (method) — The new combined guard should preserve yolo bypass semantics.
- L110 `test_yolo_mode_not_set_by_default(self)` (method) — HERMES_YOLO_MODE should not be set by default.
- L116 `test_yolo_mode_empty_string_does_not_bypass(self, monkeypatch)` (method) — Empty string for HERMES_YOLO_MODE should not trigger bypass.
- L129 `test_false_like_yolo_values_do_not_bypass_dangerous_command(self, monkeypatch, value)` (method) — False-like env strings must not silently enable YOLO bypass.
- L143 `test_false_like_yolo_values_do_not_bypass_combined_guard(self, monkeypatch, value)` (method) — Combined guard must treat false-like YOLO env strings as disabled.
- L155 `test_session_scoped_yolo_only_bypasses_current_session(self, monkeypatch)` (method) — Gateway /yolo should only bypass approvals for the active session.
- L186 `test_session_scoped_yolo_bypasses_combined_guard_only_for_current_session(self, monkeypatch)` (method) — Combined guard should honor session-scoped YOLO without affecting others.
- L211 `test_clear_session_removes_session_yolo_state(self)` (method) — Session cleanup must remove YOLO bypass state.
