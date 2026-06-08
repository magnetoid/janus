---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/kanban.py

Symbols in `hermes_cli/kanban.py`.

- L47 `_fmt_ts(ts: Optional[int])` (function)
- L53 `_fmt_task_line(t: kb.Task)` (function)
- L60 `_task_to_dict(t: kb.Task)` (function)
- L85 `_run_state_kwargs(args: argparse.Namespace)` (function)
- L95 `_parse_workspace_flag(value: str)` (function) — Parse ``--workspace`` into ``(kind, path|None)``.
- L120 `_parse_branch_flag(value: Optional[str])` (function) — Normalize an optional branch name from ``kanban create --branch``.
- L134 `_check_dispatcher_presence()` (function) — Return ``(running, message)``.
- L192 `build_parser(parent_subparsers: argparse._SubParsersAction)` (function) — Attach the ``kanban`` subcommand tree under an existing subparsers.
- L855 `kanban_command(args: argparse.Namespace)` (function) — Entry point from ``hermes kanban …`` argparse dispatch.
- L978 `_profile_author()` (function) — Best-effort author name for an interactive CLI call.
- L995 `_dispatch_boards(args: argparse.Namespace)` (function) — Handle ``hermes kanban boards <action>``.
- L1023 `_board_task_counts(slug: str)` (function) — Return ``{status: count}`` for a board. Safe to call on an empty DB.
- L1038 `_cmd_boards_list(args: argparse.Namespace)` (function)
- L1073 `_cmd_boards_create(args: argparse.Namespace)` (function)
- L1103 `_cmd_boards_rm(args: argparse.Namespace)` (function)
- L1123 `_cmd_boards_switch(args: argparse.Namespace)` (function)
- L1144 `_cmd_boards_show(args: argparse.Namespace)` (function)
- L1160 `_cmd_boards_rename(args: argparse.Namespace)` (function)
- L1175 `_cmd_boards_set_default_workdir(args: argparse.Namespace)` (function)
- L1197 `_parse_duration(val)` (function) — Parse ``30s`` / ``5m`` / ``2h`` / ``1d`` or a raw integer → seconds.
- L1222 `_cmd_init(args: argparse.Namespace)` (function)
- L1271 `_cmd_heartbeat(args: argparse.Namespace)` (function)
- L1286 `_cmd_assignees(args: argparse.Namespace)` (function)
- L1305 `_cmd_create(args: argparse.Namespace)` (function)
- L1370 `_cmd_swarm(args: argparse.Namespace)` (function)
- L1401 `_cmd_list(args: argparse.Namespace)` (function)
- L1446 `_cmd_show(args: argparse.Namespace)` (function)
- L1618 `_cmd_assign(args: argparse.Namespace)` (function)
- L1629 `_cmd_reclaim(args: argparse.Namespace)` (function)
- L1645 `_cmd_reassign(args: argparse.Namespace)` (function)
- L1668 `_cmd_diagnostics(args: argparse.Namespace)` (function) — List active diagnostics on the board. Wraps the same rule engine
- L1799 `_cmd_link(args: argparse.Namespace)` (function)
- L1806 `_cmd_unlink(args: argparse.Namespace)` (function)
- L1816 `_cmd_claim(args: argparse.Namespace)` (function)
- L1838 `_cmd_comment(args: argparse.Namespace)` (function)
- L1854 `_worker_run_id_for(task_id: str)` (function)
- L1866 `_cmd_complete(args: argparse.Namespace)` (function) — Mark one or more tasks done. Supports a single id or a list.
- L1911 `_cmd_edit(args: argparse.Namespace)` (function)
- L1939 `_cmd_block(args: argparse.Namespace)` (function)
- L1961 `_cmd_schedule(args: argparse.Namespace)` (function)
- L1983 `_cmd_unblock(args: argparse.Namespace)` (function)
- L2005 `_cmd_promote(args: argparse.Namespace)` (function)
- L2056 `_cmd_archive(args: argparse.Namespace)` (function)
- L2084 `_cmd_tail(args: argparse.Namespace)` (function)
- L2102 `_cmd_dispatch(args: argparse.Namespace)` (function)
- L2209 `_cmd_daemon(args: argparse.Namespace)` (function) — Deprecated — the dispatcher now runs inside the gateway.
- L2350 `_cmd_watch(args: argparse.Namespace)` (function) — Live-stream task_events to the terminal.
- L2399 `_cmd_stats(args: argparse.Namespace)` (function)
- L2419 `_cmd_notify_subscribe(args: argparse.Namespace)` (function)
- L2436 `_cmd_notify_list(args: argparse.Namespace)` (function)
- L2453 `_cmd_notify_unsubscribe(args: argparse.Namespace)` (function)
- L2467 `_cmd_log(args: argparse.Namespace)` (function)
- L2479 `_cmd_runs(args: argparse.Namespace)` (function) — Show attempt history for a task.
- L2526 `_cmd_context(args: argparse.Namespace)` (function)
- L2533 `_cmd_specify(args: argparse.Namespace)` (function) — Flesh out a triage task (or all of them) via auxiliary LLM,
- L2606 `_cmd_decompose(args: argparse.Namespace)` (function) — Fan a triage task (or all of them) out into a graph of child
- L2687 `_cmd_gc(args: argparse.Namespace)` (function) — Remove scratch workspaces of archived tasks, prune old events, and
- L2755 `run_slash(rest: str)` (function) — Execute a ``/kanban …`` string and return captured stdout/stderr.
