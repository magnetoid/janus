---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_signal_handler_kanban_worker.py

Symbols in `tests/hermes_cli/test_signal_handler_kanban_worker.py`.

- L34 `_synthetic_worker_script()` (function) — A standalone script that mirrors cli.py's single-query SIGTERM handler.
- L81 `_is_alive_like_dispatcher(pid: int)` (function) — Mirrors hermes_cli/kanban_db.py:_pid_alive on Linux.
- L109 `_spawn_synthetic(env_overrides: dict)` (function)
- L130 `_cleanup(proc: subprocess.Popen)` (function)
- L145 `test_sigterm_with_kanban_task_env_terminates_quickly()` (function) — With HERMES_KANBAN_TASK set, SIGTERM should kill the process in <2s
- L174 `test_sigterm_without_kanban_task_env_uses_keyboard_interrupt_path()` (function) — Without HERMES_KANBAN_TASK, the original KeyboardInterrupt path runs.
- L203 `test_real_handler_uses_os_exit_for_kanban_workers()` (function) — Source-level invariant: cli.py's _signal_handler_q must call
