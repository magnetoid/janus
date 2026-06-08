---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/file_tools.py

Symbols in `tools/file_tools.py`.

- L39 `_get_max_read_chars()` (function) — Return the configured max characters per file read.
- L81 `_resolve_path(filepath: str, task_id: str='default')` (function) — Resolve a path relative to TERMINAL_CWD (the worktree base directory)
- L88 `_get_live_tracking_cwd(task_id: str='default')` (function) — Return the task's live terminal cwd for bookkeeping when available.
- L119 `_resolve_base_dir(task_id: str='default')` (function) — Return the ABSOLUTE base directory for resolving relative paths.
- L150 `_resolve_path_for_task(filepath: str, task_id: str='default')` (function) — Resolve *filepath* against the task's absolute base directory.
- L162 `_path_resolution_warning(filepath: str, resolved: Path, task_id: str='default')` (function) — Warn when a relative path resolved OUTSIDE the task's workspace root.
- L195 `_is_blocked_device_path(path: str)` (function) — Return True for concrete device/fd paths that can hang reads.
- L214 `_is_blocked_device(filepath: str)` (function) — Return True if the path would hang the process (infinite output or blocking input).
- L245 `_get_hermes_config_resolved()` (function) — Return the resolved absolute path of the Hermes config file (cached).
- L262 `_check_sensitive_path(filepath: str, task_id: str='default')` (function) — Return an error message if the path targets a sensitive system location.
- L292 `_get_container_mirror_prefix_for_task(task_id: str='default')` (function) — Return the container-side Hermes mirror prefix for Docker file tools.
- L326 `_check_cross_profile_path(filepath: str, task_id: str='default')` (function) — Return a soft-guard warning when ``filepath`` lands in another Hermes
- L386 `_is_expected_write_exception(exc: Exception)` (function) — Return True for expected write denials that should not hit error logs.
- L425 `_record_patch_failure(task_id: str, resolved_path: str)` (function) — Increment and return the consecutive-failure count for this path.
- L442 `_reset_patch_failures(task_id: str, resolved_paths: list)` (function) — Clear consecutive-failure counts for the given paths.
- L469 `_cap_read_tracker_data(task_data: dict)` (function) — Enforce size caps on the per-task read-tracker sub-containers.
- L520 `_is_internal_file_status_text(content: str)` (function) — Return True when content looks like an internal file-tool status, not real file bytes.
- L551 `_get_file_ops(task_id: str='default')` (function) — Get or create ShellFileOperations for a terminal environment.
- L683 `clear_file_ops_cache(task_id: str=None)` (function) — Clear the file operations cache.
- L692 `read_file_tool(path: str, offset: int=1, limit: int=500, task_id: str='default')` (function) — Read a file with pagination and line numbers.
- L911 `reset_file_dedup(task_id: str=None)` (function) — Clear the deduplication cache for file reads.
- L938 `notify_other_tool_call(task_id: str='default')` (function) — Reset consecutive read/search counter for a task.
- L958 `_invalidate_dedup_for_path(filepath: str, task_id: str)` (function) — Remove all dedup cache entries whose resolved path matches *filepath*.
- L988 `_update_read_timestamp(filepath: str, task_id: str)` (function) — Record the file's current modification time after a successful write.
- L1012 `_check_file_staleness(filepath: str, task_id: str)` (function) — Check whether a file was modified since the agent last read it.
- L1043 `write_file_tool(path: str, content: str, task_id: str='default', cross_profile: bool=False)` (function) — Write content to a file.
- L1121 `patch_tool(mode: str='replace', path: str=None, old_string: str=None, new_string: str=None, replace_all: bool=False, patch: str=None, task_id: str='default', cross_profile: bool=False)` (function) — Patch a file using replace mode or V4A patch format.
- L1292 `search_tool(pattern: str, target: str='content', path: str='.', file_glob: str=None, limit: int=50, offset: int=0, output_mode: str='content', context: int=0, task_id: str='default')` (function) — Search for content or files.
- L1370 `_check_file_reqs()` (function) — Lazy wrapper to avoid circular import with tools/__init__.py.
- L1478 `_handle_read_file(args, **kw)` (function)
- L1483 `_handle_write_file(args, **kw)` (function)
- L1509 `_handle_patch(args, **kw)` (function)
- L1519 `_handle_search_files(args, **kw)` (function)
