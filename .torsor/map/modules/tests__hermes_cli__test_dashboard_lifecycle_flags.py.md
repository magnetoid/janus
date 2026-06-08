---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_lifecycle_flags.py

Symbols in `tests/hermes_cli/test_dashboard_lifecycle_flags.py`.

- L21 `_ns(**kw)` (function) — Build an argparse.Namespace with dashboard defaults plus overrides.
- L31 `TestDashboardStatus` (class)
- L32 `test_status_no_processes(self, capsys)` (method)
- L41 `test_status_with_processes(self, capsys)` (method)
- L53 `test_status_does_not_try_to_import_fastapi(self)` (method) — `--status` must not require dashboard runtime deps — it's a
- L71 `TestDashboardStop` (class)
- L72 `test_stop_when_nothing_running(self, capsys)` (method)
- L81 `test_stop_kills_and_exits_zero_when_all_killed(self, capsys)` (method) — After the kill, if the second scan returns empty we exit 0.
- L99 `test_stop_exits_nonzero_if_kill_leaves_survivors(self)` (method) — If the second scan still finds PIDs, we exit 1 so scripts can
- L110 `test_stop_does_not_try_to_import_fastapi(self)` (method) — Like --status, --stop must work without dashboard runtime deps.
- L126 `TestLifecycleFlagsTakePrecedence` (class) — If both --stop and --status are set, --status wins (it's listed
- L133 `test_status_wins_over_stop(self, capsys)` (method)
- L142 `test_stop_does_not_fall_through_to_server_start(self)` (method) — Covers the worst-case regression: if --stop ever stopped exiting
- L161 `TestArgparseWiring` (class) — Confirm the flags are exposed via the real argparse tree so
- L165 `test_flags_are_registered(self)` (method)
