---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/curator.py

Symbols in `hermes_cli/curator.py`.

- L19 `_fmt_ts(ts: Optional[str])` (function)
- L39 `_cmd_status(args)` (function)
- L168 `_cmd_run(args)` (function)
- L220 `_cmd_pause(args)` (function)
- L227 `_cmd_resume(args)` (function)
- L234 `_cmd_pin(args)` (function)
- L247 `_cmd_unpin(args)` (function)
- L260 `_cmd_restore(args)` (function)
- L267 `_cmd_archive(args)` (function) — Manually archive an agent-created skill. Refuses if pinned.
- L285 `_idle_days(record: dict)` (function) — Days since the skill's last activity (view / use / patch).
- L304 `_cmd_prune(args)` (function) — Bulk-archive agent-created skills idle for >= N days.
- L372 `_cmd_backup(args)` (function) — Take a manual snapshot of the skills tree. Same mechanism as the
- L391 `_cmd_rollback(args)` (function) — Restore the skills tree from a snapshot. Defaults to newest.
- L464 `_cmd_list_archived(args)` (function) — List archived (recoverable) skills.
- L480 `register_cli(parent: argparse.ArgumentParser)` (function) — Attach `curator` subcommands to *parent*.
- L585 `cli_main(argv=None)` (function) — Standalone entry (also usable by hermes_cli.main fallthrough).
