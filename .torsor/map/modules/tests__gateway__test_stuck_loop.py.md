---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_stuck_loop.py

Symbols in `tests/gateway/test_stuck_loop.py`.

- L17 `runner_with_home(tmp_path, monkeypatch)` (function) — Create a runner with a writable HERMES_HOME.
- L24 `TestStuckLoopDetection` (class)
- L26 `test_increment_creates_file(self, runner_with_home)` (method)
- L35 `test_increment_accumulates(self, runner_with_home)` (method)
- L43 `test_increment_drops_inactive_sessions(self, runner_with_home)` (method)
- L51 `test_suspend_at_threshold(self, runner_with_home)` (method)
- L67 `test_no_suspend_below_threshold(self, runner_with_home)` (method)
- L81 `test_clear_on_success(self, runner_with_home)` (method)
- L91 `test_clear_removes_file_when_empty(self, runner_with_home)` (method)
- L97 `test_suspend_clears_file(self, runner_with_home)` (method)
- L110 `test_no_file_no_crash(self, runner_with_home)` (method)
