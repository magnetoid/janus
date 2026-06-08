---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/kanban_tools.py

Symbols in `tools/kanban_tools.py`.

- L49 `_profile_has_kanban_toolset()` (function)
- L62 `_check_kanban_mode()` (function) — Task-lifecycle tools are available when:
- L79 `_check_kanban_orchestrator_mode()` (function) — Board-routing tools (kanban_list, kanban_unblock) are intentionally
- L97 `_default_task_id(arg: Optional[str])` (function) — Resolve ``task_id`` arg or fall back to the env var the dispatcher set.
- L105 `_worker_run_id(task_id: str)` (function) — Return this worker's dispatcher run id when it is scoped to task_id.
- L118 `_stamp_worker_session_metadata(task_id: str, metadata: Optional[dict])` (function) — Add trusted worker session id metadata for this worker's own task.
- L132 `_enforce_worker_task_ownership(tid: str)` (function) — Reject worker-driven destructive calls on foreign task IDs.
- L164 `_connect(board: Optional[str]=None)` (function) — Import + connect lazily so the module imports cleanly in non-kanban
- L204 `heartbeat_current_worker_from_env()` (function) — Best-effort: extend the kanban claim + bump board heartbeat for the
- L263 `_ok(**fields: Any)` (function)
- L267 `_normalize_profile(value: Any)` (function) — Normalize CLI-compatible assignee sentinels for the tool surface.
- L277 `_parse_bool_arg(args: dict, name: str, *, default: bool=False)` (function)
- L291 `_require_orchestrator_tool(tool_name: str)` (function) — Belt-and-suspenders runtime guard for orchestrator-only handlers.
- L309 `_task_summary_dict(kb, conn, task)` (function) — Compact task shape for board-listing tools.
- L339 `_handle_show(args: dict, **kw)` (function) — Read a task's full state: task row, parents, children, comments,
- L415 `_handle_list(args: dict, **kw)` (function) — List task summaries with the same core filters as the CLI.
- L476 `_handle_complete(args: dict, **kw)` (function) — Mark the current task done with a structured handoff.
- L598 `_handle_block(args: dict, **kw)` (function) — Transition the task to blocked with a reason a human will read.
- L636 `_handle_heartbeat(args: dict, **kw)` (function) — Signal that the worker is still alive during a long operation.
- L687 `_handle_comment(args: dict, **kw)` (function) — Append a comment to a task's thread.
- L723 `_handle_create(args: dict, **kw)` (function) — Create a child task. Orchestrator workers use this to fan out.
- L834 `_handle_unblock(args: dict, **kw)` (function) — Transition a blocked task back to ready.
- L862 `_handle_link(args: dict, **kw)` (function) — Add a parent→child dependency edge after the fact.
- L903 `_board_schema_prop()` (function) — Schema fragment for the optional ``board`` parameter.
