---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway_proc_fallback.py

Symbols in `tests/hermes_cli/test_gateway_proc_fallback.py`.

- L23 `_fake_proc_dir(entries: dict)` (function) — Return side_effects that simulate /proc: isdir → True, listdir → pids,
- L54 `TestProcFallback` (class) — _scan_gateway_pids reads /proc when available, skips ps.
- L57 `test_detects_gateway_pid_via_proc(self)` (method)
- L80 `test_excludes_own_pid_from_proc_scan(self)` (method)
- L97 `test_falls_back_to_ps_when_proc_absent(self)` (method)
- L114 `test_proc_permission_error_skips_pid(self)` (method)
