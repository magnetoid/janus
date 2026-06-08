---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/disk-cleanup/__init__.py

Symbols in `plugins/disk-cleanup/__init__.py`.

- L52 `_tracker_key(task_id: str, session_id: str)` (function)
- L56 `_record_track(task_id: str, session_id: str, path: Path, category: str)` (function) — Record that we tracked *path* as *category* during this turn.
- L65 `_drain(task_id: str, session_id: str)` (function) — Pop the set of test paths tracked during this turn.
- L72 `_attempt_track(path_str: str, task_id: str, session_id: str)` (function) — Best-effort auto-track. Never raises.
- L88 `_extract_paths_from_write_file(args: Dict[str, Any])` (function)
- L93 `_extract_paths_from_patch(args: Dict[str, Any])` (function)
- L103 `_extract_paths_from_terminal(args: Dict[str, Any], result: str)` (function) — Best-effort: pull candidate filesystem paths from a terminal command
- L128 `_on_post_tool_call(tool_name: str='', args: Optional[Dict[str, Any]]=None, result: Any=None, task_id: str='', session_id: str='', tool_call_id: str='', **_: Any)` (function) — Auto-track ephemeral files created by recent tool calls.
- L155 `_on_session_end(session_id: str='', completed: bool=True, interrupted: bool=False, **_: Any)` (function) — Run quick cleanup if any test files were tracked during this turn.
- L213 `_fmt_summary(summary: Dict[str, Any])` (function)
- L223 `_handle_slash(raw_args: str)` (function)
- L309 `register(ctx)` (function)
