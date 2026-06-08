---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/code_execution_tool.py

Symbols in `tools/code_execution_tool.py`.

- L136 `_scrub_child_env(source_env, is_passthrough=None, is_windows=None)` (function) — Produce the scrubbed child-process env for execute_code.
- L200 `check_sandbox_requirements()` (function) — Code execution sandbox requires a POSIX OS for Unix domain sockets.
- L259 `generate_hermes_tools_module(enabled_tools: List[str], transport: str='uds')` (function) — Build the source code for the hermes_tools.py stub module.
- L468 `_rpc_server_loop(server_sock: socket.socket, task_id: str, tool_call_log: list, tool_call_counter: list, max_tool_calls: int, allowed_tools: frozenset)` (function) — Accept one client connection and dispatch tool-call requests until
- L592 `_get_or_create_env(task_id: str)` (function) — Get or create the terminal environment for *task_id*.
- L694 `_ship_file_to_remote(env, remote_path: str, content: str)` (function) — Write *content* to *remote_path* on the remote environment.
- L711 `_env_temp_dir(env: Any)` (function) — Return a writable temp dir for env-backed execute_code sandboxes.
- L727 `_rpc_poll_loop(env, rpc_dir: str, task_id: str, tool_call_log: list, tool_call_counter: list, max_tool_calls: int, allowed_tools: frozenset, stop_event: threading.Event)` (function) — Poll the remote filesystem for tool call requests and dispatch them.
- L869 `_execute_remote(code: str, task_id: Optional[str], enabled_tools: Optional[List[str]])` (function) — Run a script on the remote terminal backend via file-based RPC.
- L1066 `execute_code(code: str, task_id: Optional[str]=None, enabled_tools: Optional[List[str]]=None)` (function) — Run a Python script in a sandboxed child process with RPC access
- L1501 `_kill_process_group(proc, escalate: bool=False)` (function) — Kill the child and its entire process tree (cross-platform via psutil).
- L1551 `_load_config()` (function) — Load code_execution config without importing the interactive CLI.
- L1580 `_get_execution_mode()` (function) — Return the active execute_code mode — 'project' or 'strict'.
- L1608 `_is_usable_python(python_path: str)` (function) — Check whether a candidate Python interpreter is usable for execute_code.
- L1627 `_resolve_child_python(mode: str)` (function) — Pick the Python interpreter for the execute_code subprocess.
- L1670 `_resolve_child_cwd(mode: str, staging_dir: str)` (function) — Resolve the working directory for the execute_code subprocess.
- L1723 `build_execute_code_schema(enabled_sandbox_tools: set=None, mode: str=None)` (function) — Build the execute_code schema with description listing only enabled tools.
