---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_patch_failure_tracking.py

Symbols in `tests/tools/test_patch_failure_tracking.py`.

- L18 `hermes_home(monkeypatch, tmp_path)` (function) — Isolate HERMES_HOME and clear module-level caches afterward so the
- L42 `fresh_tracker()` (function) — Reset the module-level tracker before each test so the count starts
- L54 `TestPatchFailureEscalation` (class)
- L55 `test_first_two_failures_use_normal_hint(self, hermes_home, tmp_path, fresh_tracker)` (method)
- L77 `test_third_consecutive_failure_escalates(self, hermes_home, tmp_path, fresh_tracker)` (method)
- L103 `test_success_clears_failure_counter(self, hermes_home, tmp_path, fresh_tracker)` (method)
- L150 `test_different_paths_have_independent_counters(self, hermes_home, tmp_path, fresh_tracker)` (method)
- L188 `test_different_tasks_have_independent_counters(self, hermes_home, tmp_path, fresh_tracker)` (method)
