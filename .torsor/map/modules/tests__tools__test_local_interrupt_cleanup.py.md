---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_local_interrupt_cleanup.py

Symbols in `tests/tools/test_local_interrupt_cleanup.py`.

- L27 `_isolate_hermes_home(tmp_path, monkeypatch)` (function)
- L32 `_pgid_still_alive(pgid: int)` (function) — Return True if any process in the given process group is still alive.
- L41 `_process_group_snapshot(pgid: int)` (function) — Return a process-table snapshot for diagnostics.
- L51 `_wait_for_pgid_exit(pgid: int, timeout: float=30.0)` (function) — Wait for a process group to disappear under loaded xdist hosts.
- L67 `test_kill_process_uses_cached_pgid_if_wrapper_already_exited(monkeypatch)` (function) — If the shell wrapper exits before cleanup, still kill its process group.
- L99 `test_wait_for_process_kills_subprocess_on_keyboardinterrupt()` (function) — When KeyboardInterrupt arrives mid-poll, the subprocess group must be
