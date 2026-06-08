---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/process_registry.py

Symbols in `tools/process_registry.py`.

- L78 `format_uptime_short(seconds: int)` (function)
- L90 `ProcessSession` (class) — A tracked background process with output buffering.
- L137 `ProcessRegistry` (class) — In-memory registry of running and finished background processes.
- L155 `__init__(self)` (method)
- L184 `_clean_shell_noise(text: str)` (method) — Strip shell startup warnings from the beginning of output.
- L191 `_check_watch_patterns(self, session: ProcessSession, new_text: str)` (method) — Scan new output for watch patterns and queue notifications.
- L319 `_global_watch_admit(self, now: float)` (method) — Return True if this watch_match event is allowed through the global breaker.
- L407 `_is_host_pid_alive(pid: Optional[int])` (method) — Best-effort liveness check for host-visible PIDs.
- L416 `_refresh_detached_session(self, session: Optional[ProcessSession])` (method) — Update recovered host-PID sessions when the underlying process has exited.
- L436 `_terminate_host_pid(pid: int)` (method) — Terminate a host-visible PID and its descendants.
- L503 `_env_temp_dir(env: Any)` (method) — Return the writable sandbox temp dir for env-backed background tasks.
- L515 `spawn_local(self, command: str, cwd: str=None, task_id: str='', session_key: str='', env_vars: dict=None, use_pty: bool=False)` (method) — Spawn a background process locally.
- L652 `spawn_via_env(self, env: Any, command: str, cwd: str=None, task_id: str='', session_key: str='', timeout: int=10)` (method) — Spawn a background process through a non-local environment backend.
- L750 `_reader_loop(self, session: ProcessSession)` (method) — Background thread: read stdout from a local Popen process.
- L778 `_env_poller_loop(self, session: ProcessSession, env: Any, log_path: str, pid_path: str, exit_path: str)` (method) — Background thread: poll a sandbox log file for non-local backends.
- L831 `_pty_reader_loop(self, session: ProcessSession)` (method) — Background thread: read output from a PTY process.
- L862 `_move_to_finished(self, session: ProcessSession)` (method) — Move a session from running to finished.
- L891 `is_completion_consumed(self, session_id: str)` (method) — Check if a completion notification was already consumed via wait/poll/log.
- L895 `drain_notifications(self)` (method) — Pop all pending notification events and return formatted pairs.
- L915 `get(self, session_id: str)` (method) — Get a session by ID (running or finished).
- L921 `_reconcile_local_exit(self, session: 'ProcessSession')` (method) — Reconcile session.exited against the real child process state.
- L993 `poll(self, session_id: str)` (method) — Check status and get new output for a background process.
- L1024 `read_log(self, session_id: str, offset: int=0, limit: int=200)` (method) — Read the full output log with optional pagination by lines.
- L1055 `wait(self, session_id: str, timeout: int=None)` (method) — Block until a process exits, timeout, or interrupt.
- L1132 `kill_process(self, session_id: str)` (method) — Kill a background process.
- L1202 `write_stdin(self, session_id: str, data: str)` (method) — Send raw data to a running process's stdin (no newline appended).
- L1229 `submit_stdin(self, session_id: str, data: str='')` (method) — Send data + newline to a running process's stdin (like pressing Enter).
- L1233 `close_stdin(self, session_id: str)` (method) — Close a running process's stdin / send EOF without killing the process.
- L1256 `count_running(self)` (method) — Return the count of currently-running background processes.
- L1269 `list_sessions(self, task_id: str=None)` (method) — List all running and recently-finished processes.
- L1300 `has_active_processes(self, task_id: str)` (method) — Check if there are active (running) processes for a task_id.
- L1314 `has_active_for_session(self, session_key: str)` (method) — Check if there are active processes for a gateway session key.
- L1328 `kill_all(self, task_id: str=None)` (method) — Kill all running processes, optionally filtered by task_id. Returns count killed.
- L1345 `_prune_if_needed(self)` (method) — Remove oldest finished sessions if over MAX_PROCESSES. Must hold _lock.
- L1374 `_write_checkpoint(self)` (method) — Write running process metadata to checkpoint file atomically.
- L1407 `recover_from_checkpoint(self)` (method) — On gateway startup, probe PIDs from checkpoint file.
- L1493 `format_process_notification(evt: dict)` (function) — Format a process notification event into a [IMPORTANT: ...] message.
- L1581 `_handle_process(args, **kw)` (function)
