---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/kanban/dashboard/plugin_api.py

Symbols in `plugins/kanban/dashboard/plugin_api.py`.

- L64 `_ws_upgrade_authorized(ws: 'WebSocket')` (function) — Authorize a WebSocket upgrade by delegating to the dashboard's canonical
- L97 `_resolve_board(board: Optional[str])` (function) — Validate and normalise a board slug from a query param.
- L119 `_conn(board: Optional[str]=None)` (function) — Open a kanban_db connection, creating the schema on first use.
- L158 `_task_dict(task: kanban_db.Task, *, latest_summary: Optional[str]=None)` (function)
- L179 `_event_dict(event: kanban_db.Event)` (function)
- L190 `_comment_dict(c: kanban_db.Comment)` (function)
- L200 `_attachment_dict(a: kanban_db.Attachment)` (function) — Serialise an Attachment for the drawer. ``stored_path`` is the
- L215 `_run_dict(r: kanban_db.Run)` (function) — Serialise a Run for the drawer's Run history section.
- L248 `_compute_task_diagnostics(conn: sqlite3.Connection, task_ids: Optional[list[str]]=None)` (function) — Run the diagnostic rule engine against every task (or a subset)
- L316 `_warnings_summary_from_diagnostics(diagnostics: list[dict])` (function) — Compact summary for cards: {count, highest_severity, kinds,
- L355 `_links_for(conn: sqlite3.Connection, task_id: str)` (function) — Return {'parents': [...], 'children': [...]} for a task.
- L379 `get_board(tenant: Optional[str]=Query(None, description='Filter to a single tenant'), include_archived: bool=Query(False), board: Optional[str]=Query(None, description='Kanban board slug (omit for current)'), workflow_template_id: Optional[str]=Query(None, description='Restrict to tasks using this workflow template id'), current_step_key: Optional[str]=Query(None, description='Restrict to tasks at this workflow step key'))` (function) — Return the full board grouped by status column.
- L518 `get_task(task_id: str, board: Optional[str]=Query(None), run_state_type: Optional[str]=Query(None, description="With run_state_name: filter runs by column 'status' or 'outcome'"), run_state_name: Optional[str]=Query(None, description='With run_state_type: exact value for that run column'))` (function)
- L580 `CreateTaskBody` (class)
- L598 `create_task(payload: CreateTaskBody, board: Optional[str]=Query(None))` (function)
- L652 `_safe_attachment_name(raw: str)` (function) — Reduce a client-supplied filename to a safe basename.
- L672 `list_task_attachments(task_id: str, board: Optional[str]=Query(None))` (function)
- L688 `upload_task_attachment(task_id: str, file: UploadFile=File(...), board: Optional[str]=Query(None), uploaded_by: Optional[str]=Form(None))` (function) — Store an uploaded file for a task and record its metadata.
- L763 `download_attachment(attachment_id: int, board: Optional[str]=Query(None))` (function)
- L790 `remove_attachment(attachment_id: int, board: Optional[str]=Query(None))` (function)
- L806 `UpdateTaskBody` (class)
- L822 `update_task(task_id: str, payload: UpdateTaskBody, board: Optional[str]=Query(None))` (function)
- L945 `delete_task(task_id: str, board: Optional[str]=Query(None))` (function)
- L957 `_parents_blocking_ready(conn: sqlite3.Connection, task_id: str)` (function) — Return parent rows (``id``, ``title``, ``status``) that aren't ``done``
- L980 `_set_status_direct(conn: sqlite3.Connection, task_id: str, new_status: str)` (function) — Direct status write for drag-drop moves that aren't covered by the
- L1086 `CommentBody` (class)
- L1092 `add_comment(task_id: str, payload: CommentBody, board: Optional[str]=Query(None))` (function)
- L1112 `LinkBody` (class)
- L1118 `add_link(payload: LinkBody, board: Optional[str]=Query(None))` (function)
- L1131 `delete_link(parent_id: str=Query(...), child_id: str=Query(...), board: Optional[str]=Query(None))` (function)
- L1149 `BulkTaskBody` (class)
- L1162 `bulk_update(payload: BulkTaskBody, board: Optional[str]=Query(None))` (function) — Apply the same patch to every id in ``payload.ids``.
- L1265 `list_diagnostics(board: Optional[str]=Query(None, description='Kanban board slug (omit for current)'), severity: Optional[str]=Query(None, description='Filter by severity: warning|error|critical'))` (function) — Return ``[{task_id, task_title, task_status, task_assignee,
- L1353 `list_active_workers(board: Optional[str]=Query(None, description='Kanban board slug (omit for current)'))` (function) — Return every currently-running worker on the board.
- L1414 `get_run_endpoint(run_id: int, board: Optional[str]=Query(None, description='Kanban board slug (omit for current)'))` (function) — Direct lookup of a ``task_runs`` row by its integer id.
- L1436 `inspect_run_endpoint(run_id: int, board: Optional[str]=Query(None, description='Kanban board slug (omit for current)'))` (function) — Live PID stats for a run's worker process via psutil.
- L1503 `TerminateRunBody` (class)
- L1508 `terminate_run_endpoint(run_id: int, payload: TerminateRunBody, board: Optional[str]=Query(None, description='Kanban board slug (omit for current)'))` (function) — Terminate the worker process backing an in-flight run.
- L1559 `ReclaimBody` (class)
- L1564 `reclaim_task_endpoint(task_id: str, payload: ReclaimBody, board: Optional[str]=Query(None))` (function) — Release an active worker claim on a running task.
- L1593 `SpecifyBody` (class) — Optional author override. Nothing else is configurable from the
- L1602 `specify_task_endpoint(task_id: str, payload: SpecifyBody, board: Optional[str]=Query(None))` (function) — Flesh out a triage-column task via the auxiliary LLM and promote
- L1645 `ReassignBody` (class)
- L1652 `reassign_task_endpoint(task_id: str, payload: ReassignBody, board: Optional[str]=Query(None))` (function) — Reassign a task to a different profile, optionally reclaiming first.
- L1691 `get_config()` (function) — Return kanban dashboard preferences from ~/.hermes/config.yaml.
- L1730 `_configured_home_channels()` (function) — Return every platform that has a home_channel set, fully hydrated.
- L1761 `_active_profile_name()` (function) — Return the current Hermes profile name for notify-sub ownership.
- L1770 `_home_sub_matches(sub: dict, home: dict)` (function) — True if a notify_subs row corresponds to the given home channel.
- L1780 `get_home_channels(task_id: Optional[str]=Query(None), board: Optional[str]=Query(None))` (function) — List every platform with a home channel, plus whether *task_id*
- L1814 `subscribe_home(task_id: str, platform: str, board: Optional[str]=Query(None))` (function) — Subscribe *task_id* to notifications routed to *platform*'s home channel.
- L1849 `unsubscribe_home(task_id: str, platform: str, board: Optional[str]=Query(None))` (function) — Remove any notify subscription on *task_id* that matches *platform*'s home.
- L1878 `get_stats(board: Optional[str]=Query(None))` (function) — Per-status + per-assignee counts + oldest-ready age.
- L1894 `get_assignees(board: Optional[str]=Query(None))` (function) — Known profiles + per-profile task counts.
- L1915 `get_task_log(task_id: str, tail: Optional[int]=Query(None, ge=1, le=2000000), board: Optional[str]=Query(None))` (function) — Return the worker's stdout/stderr log.
- L1955 `dispatch(dry_run: bool=Query(False), max_n: int=Query(8, alias='max'), board: Optional[str]=Query(None))` (function)
- L1979 `CreateBoardBody` (class)
- L1988 `RenameBoardBody` (class)
- L1995 `_board_counts(slug: str)` (function) — Return ``{status: count}`` for a board. Safe on an empty DB.
- L2014 `list_boards(include_archived: bool=Query(False))` (function) — Return every board on disk with task counts and the active slug.
- L2026 `create_board_endpoint(payload: CreateBoardBody)` (function) — Create a new board. Idempotent — ``slug`` collision returns existing.
- L2047 `rename_board(slug: str, payload: RenameBoardBody)` (function) — Update a board's display metadata (slug is immutable — create a new one to rename the directory).
- L2066 `delete_board(slug: str, delete: bool=Query(False, description='Hard-delete instead of archive'))` (function) — Archive (default) or hard-delete a board.
- L2076 `switch_board(slug: str)` (function) — Persist ``slug`` as the active board for subsequent CLI / slash calls.
- L2107 `DescribeBody` (class)
- L2111 `DescribeAutoBody` (class)
- L2116 `list_profile_roster()` (function) — Return every installed profile with its description.
- L2146 `update_profile_description(profile_name: str, payload: DescribeBody)` (function) — Set or clear the description of a profile.
- L2179 `auto_describe_profile(profile_name: str, payload: DescribeAutoBody)` (function) — Generate a description for the named profile via the auxiliary
- L2210 `DecomposeBody` (class)
- L2215 `decompose_task_endpoint(task_id: str, payload: DecomposeBody, board: Optional[str]=Query(None))` (function) — Fan a triage-column task out into a graph of child tasks via the
- L2258 `OrchestrationSettingsBody` (class)
- L2266 `get_orchestration_settings()` (function) — Return the current kanban orchestration knobs from config.yaml
- L2309 `set_orchestration_settings(payload: OrchestrationSettingsBody)` (function) — Update the kanban orchestration knobs in ~/.hermes/config.yaml.
- L2380 `stream_events(ws: WebSocket)` (function)
