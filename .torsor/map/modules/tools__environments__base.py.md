---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/base.py

Symbols in `tools/environments/base.py`.

- L46 `set_activity_callback(cb: Callable[[str], None] | None)` (function) — Register a callback that _wait_for_process fires periodically.
- L51 `_get_activity_callback()` (function)
- L55 `touch_activity_if_due(state: dict, label: str)` (function) — Fire the activity callback at most once every ``state['interval']`` seconds.
- L81 `get_sandbox_dir()` (function) — Return the host-side root for all sandbox storage (Docker workspaces,
- L101 `_pipe_stdin(proc: subprocess.Popen, data: str)` (function) — Write *data* to proc.stdin on a daemon thread to avoid pipe-buffer deadlocks.
- L135 `_popen_bash(cmd: list[str], stdin_data: str | None=None, **kwargs)` (function) — Spawn a subprocess with standard stdout/stderr/stdin setup.
- L157 `_load_json_store(path: Path)` (function) — Load a JSON file as a dict, returning ``{}`` on any error.
- L167 `_save_json_store(path: Path, data: dict)` (function) — Write *data* as pretty-printed JSON to *path*.
- L173 `_file_mtime_key(host_path: str)` (function) — Return ``(mtime, size)`` for cache comparison, or ``None`` if unreadable.
- L187 `ProcessHandle` (class) — Duck type that every backend's _run_bash() must return.
- L194 `poll(self)` (method)
- L195 `kill(self)` (method)
- L196 `wait(self, timeout: float | None=None)` (method)
- L199 `stdout(self)` (method)
- L202 `returncode(self)` (method)
- L205 `_ThreadedProcessHandle` (class) — Adapter for SDK backends (Modal, Daytona) that have no real subprocess.
- L214 `__init__(self, exec_fn: Callable[[], tuple[str, int]], cancel_fn: Callable[[], None] | None=None)` (method)
- L252 `stdout(self)` (method)
- L256 `returncode(self)` (method)
- L259 `poll(self)` (method)
- L262 `kill(self)` (method)
- L269 `wait(self, timeout: float | None=None)` (method)
- L279 `_cwd_marker(session_id: str)` (function)
- L288 `BaseEnvironment` (class) — Common interface and unified execution flow for all Hermes backends.
- L302 `get_temp_dir(self)` (method) — Return the backend temp directory used for session artifacts.
- L311 `__init__(self, cwd: str, timeout: int, env: dict=None)` (method)
- L327 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method) — Spawn a bash process to run *cmd_string*.
- L343 `cleanup(self)` (method) — Release backend resources (container, instance, connection).
- L351 `init_session(self)` (method) — Capture login shell environment into a snapshot file.
- L407 `_quote_cwd_for_cd(cwd: str)` (method) — Quote a ``cd`` target while preserving ``~`` expansion.
- L417 `_wrap_command(self, command: str, cwd: str)` (method) — Build the full bash script that sources snapshot, cd's, runs command,
- L474 `_embed_stdin_heredoc(command: str, stdin_data: str)` (method) — Append stdin_data as a shell heredoc to the command string.
- L483 `_wait_for_process(self, proc: ProcessHandle, timeout: int=120)` (method) — Poll-based wait with interrupt checking and stdout draining.
- L762 `_kill_process(self, proc: ProcessHandle)` (method) — Terminate a process. Subclasses may override for process-group kill.
- L773 `_update_cwd(self, result: dict)` (method) — Extract CWD from command output. Override for local file-based read.
- L777 `_extract_cwd_from_output(self, result: dict)` (method) — Parse the __HERMES_CWD_{session}__ marker from stdout output.
- L815 `_before_execute(self)` (method) — Hook called before each command execution.
- L829 `execute(self, command: str, cwd: str='', *, timeout: int | None=None, stdin_data: str | None=None, rewrite_compound_background: bool=True)` (method) — Execute a command, return {"output": str, "returncode": int}.
- L881 `stop(self)` (method) — Alias for cleanup (compat with older callers).
- L885 `__del__(self)` (method)
- L891 `_prepare_command(self, command: str)` (method) — Transform sudo commands if SUDO_PASSWORD is available.
