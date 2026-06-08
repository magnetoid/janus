---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_kanban_worker_runs.py

Symbols in `tests/plugins/test_kanban_worker_runs.py`.

- L30 `_load_plugin_router()` (function) — Dynamically load plugins/kanban/dashboard/plugin_api.py and return its router.
- L50 `kanban_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with an empty kanban DB.
- L61 `client(kanban_home)` (function)
- L67 `_insert_run(conn, task_id, *, worker_pid=None, ended_at=None)` (function) — Insert a task_runs row directly (bypassing claim machinery) and return run_id.
- L85 `test_workers_active_empty_board(client)` (function) — Board with no running tasks returns an empty workers list.
- L95 `test_workers_active_with_running_task(client)` (function) — A running task with an open run row and worker_pid appears in the list.
- L119 `test_workers_active_excludes_ended_runs(client)` (function) — Runs with ended_at set are excluded even if task is running.
- L134 `test_workers_active_excludes_runs_without_pid(client)` (function) — Runs with no worker_pid are not considered active workers.
- L153 `test_get_run_404_unknown_id(client)` (function) — Non-existent run_id returns 404.
- L160 `test_get_run_ok(client)` (function) — Existing run row returns 200 with expected shape.
- L184 `test_inspect_run_404(client)` (function) — Non-existent run_id returns 404.
- L190 `test_inspect_run_already_ended(client)` (function) — Run with ended_at set returns alive=false with reason.
- L206 `test_inspect_run_no_pid(client)` (function) — Run with no worker_pid returns alive=false with reason.
- L222 `test_inspect_run_dead_pid(client, monkeypatch)` (function) — Run with a non-existent PID returns alive=false via psutil.NoSuchProcess.
- L257 `test_inspect_run_live_pid(client, monkeypatch)` (function) — Run with a live PID returns alive=true with psutil fields.
- L309 `_setup_running_task_with_run(conn, *, title, assignee, worker_pid)` (function) — Create a task in 'running' state with a matching open task_runs row.
- L334 `test_terminate_run_404_unknown_id(client)` (function) — POST to unknown run_id returns 404.
- L344 `test_terminate_run_409_already_ended(client)` (function) — POST against a run with ended_at set returns 409.
- L363 `test_terminate_run_ok(client, monkeypatch)` (function) — Happy path: live run is terminated, signal fn invoked, reason recorded.
- L406 `test_terminate_run_409_task_not_reclaimable(client, monkeypatch)` (function) — Open run row whose task is no longer claimable returns 409.
- L432 `test_terminate_run_accepts_empty_body(client)` (function) — Empty JSON body (no reason) is still accepted; falls through to 404.
