---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_sync_perf.py

Symbols in `tests/tools/test_file_sync_perf.py`.

- L20 `local_env()` (function)
- L28 `ssh_env()` (function)
- L44 `_time_executions(env, command: str, n: int=10)` (function) — Run *command* n times and return per-call wall-clock durations.
- L57 `_report(label: str, durations: list[float])` (function) — Print timing stats.
- L72 `TestLocalPerf` (class) — Local baseline — no file sync, no network. Sets the floor.
- L75 `test_echo_latency(self, local_env)` (method)
- L83 `TestSSHPerf` (class) — SSH with FileSyncManager — mtime skip should make sync ~0ms.
- L86 `test_echo_latency(self, ssh_env)` (method) — Sequential echo commands — measures per-command overhead including sync check.
- L93 `test_sync_overhead_after_interval(self, ssh_env)` (method) — Measure sync cost when the rate-limit window has expired.
- L117 `test_no_sync_within_interval(self, ssh_env)` (method) — Rapid sequential commands within 5s window — no sync at all.
