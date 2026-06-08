---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/terminal_tool.py

Symbols in `tools/terminal_tool.py`.

- L79 `_safe_parse_import_env(name: str, default: Any, converter, type_label: str)` (function) — Parse module-level numeric env vars without breaking import.
- L123 `_check_disk_usage_warning()` (function) — Check if total disk usage exceeds warning threshold.
- L176 `_get_sudo_password_callback()` (function)
- L180 `_get_approval_callback()` (function)
- L184 `set_sudo_password_callback(cb)` (function) — Register a callback for sudo password prompts (used by CLI).
- L193 `set_approval_callback(cb)` (function) — Register a callback for dangerous command approval prompts.
- L203 `_get_sudo_password_cache_scope()` (function) — Return the cache scope for interactive sudo passwords.
- L225 `_get_cached_sudo_password()` (function) — Return the cached sudo password for the current scope.
- L232 `_set_cached_sudo_password(password: str)` (function) — Persist a sudo password for the current scope.
- L242 `_reset_cached_sudo_passwords()` (function) — Clear all cached sudo passwords.
- L260 `_check_all_guards(command: str, env_type: str)` (function) — Delegate to consolidated guard (tirith + dangerous cmd) with CLI callback.
- L273 `_validate_workdir(workdir: str)` (function) — Reject workdir values that don't look like a filesystem path.
- L295 `_handle_sudo_failure(output: str, env_type: str)` (function) — Check for sudo failure and add helpful message for messaging contexts.
- L321 `_prompt_for_sudo_password(timeout_seconds: int=45)` (function) — Prompt user for sudo password with timeout.
- L445 `_safe_command_preview(command: Any, limit: int=200)` (function) — Return a log-safe preview for possibly-invalid command values.
- L456 `_looks_like_env_assignment(token: str)` (function) — Return True when *token* is a leading shell environment assignment.
- L464 `_read_shell_token(command: str, start: int)` (function) — Read one shell token, preserving quotes/escapes, starting at *start*.
- L500 `_rewrite_real_sudo_invocations(command: str)` (function) — Rewrite only real unquoted sudo command words, not plain text mentions.
- L561 `_sudo_nopasswd_works()` (function) — Return True when local sudo currently works without prompting.
- L587 `_rewrite_compound_background(command: str)` (function) — Wrap `A && B &` (or `A || B &`) to `A && { B & }` at depth 0.
- L752 `_transform_sudo_command(command: str | None)` (function) — Transform sudo commands to use -S flag if SUDO_PASSWORD is available.
- L870 `_maybe_reap_docker_orphans(container_config: Dict[str, Any])` (function) — Run the docker orphan reaper once per process, if enabled.
- L946 `register_task_env_overrides(task_id: str, overrides: Dict[str, Any])` (function) — Register environment overrides for a specific task/rollout.
- L982 `clear_task_env_overrides(task_id: str)` (function) — Clear environment overrides for a task after rollout completes.
- L991 `_resolve_container_task_id(task_id: Optional[str])` (function) — Map a tool-call ``task_id`` to the container/sandbox key used by
- L1017 `_parse_env_var(name: str, default: str, converter=int, type_label: str='integer')` (function) — Parse an environment variable with *converter*, raising a clear error on bad values.
- L1033 `_safe_getcwd()` (function) — Return the current working directory, tolerating a deleted CWD.
- L1047 `_get_env_config()` (function) — Get terminal environment configuration from environment variables.
- L1148 `_get_modal_backend_state(modal_mode: object | None)` (function) — Resolve direct vs managed Modal backend selection.
- L1157 `_create_environment(env_type: str, image: str, cwd: str, timeout: int, ssh_config: dict=None, container_config: dict=None, local_config: dict=None, task_id: str='default', host_cwd: str=None)` (function) — Create an execution environment for sandboxed command execution.
- L1307 `_cleanup_inactive_envs(lifetime_seconds: int=300)` (function) — Clean up environments that have been inactive for longer than lifetime_seconds.
- L1369 `_cleanup_thread_worker()` (function) — Background thread worker that periodically cleans up inactive environments.
- L1384 `_start_cleanup_thread()` (function) — Start the background cleanup thread if not already running.
- L1395 `_stop_cleanup_thread()` (function) — Stop the background cleanup thread.
- L1406 `get_active_env(task_id: str)` (function) — Return the active BaseEnvironment for *task_id*, or None.
- L1413 `is_persistent_env(task_id: str)` (function) — Return True if the active environment for task_id is configured for
- L1432 `cleanup_all_environments()` (function) — Clean up ALL active environments. Use with caution.
- L1459 `cleanup_vm(task_id: str, *, force_remove: bool=False)` (function) — Manually clean up a specific environment by task_id.
- L1527 `_atexit_cleanup()` (function) — Stop cleanup thread and shut down all remaining sandboxes on exit.
- L1562 `_interpret_exit_code(command: str, exit_code: int)` (function) — Return a human-readable note when a non-zero exit code is non-erroneous.
- L1626 `_command_requires_pipe_stdin(command: str)` (function) — Return True when PTY mode would break stdin-driven commands.
- L1648 `_strip_quotes(command: str)` (function) — Remove single- and double-quoted content so regex checks don't match inside strings.
- L1676 `_looks_like_help_or_version_command(command: str)` (function) — Return True for informational invocations that should never be blocked.
- L1687 `_foreground_background_guidance(command: str)` (function) — Suggest background mode when a foreground command looks long-lived.
- L1724 `_resolve_notification_flag_conflict(*, notify_on_complete: bool, watch_patterns, background: bool)` (function) — Decide what to do when both notify_on_complete and watch_patterns are set.
- L1751 `_resolve_command_cwd(*, workdir: Optional[str], env: Any, default_cwd: str)` (function) — Return the cwd for a command, preferring the live session cwd.
- L1775 `terminal_tool(command: str, background: bool=False, timeout: Optional[int]=None, task_id: Optional[str]=None, force: bool=False, workdir: Optional[str]=None, pty: bool=False, notify_on_complete: bool=False, watch_patterns: Optional[List[str]]=None)` (function) — Execute a command in the configured terminal environment.
- L2383 `check_terminal_requirements()` (function) — Check if all requirements for the terminal tool are met.
- L2590 `_handle_terminal(args, **kw)` (function)
