---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/claw.py

Symbols in `hermes_cli/claw.py`.

- L58 `_detect_openclaw_processes()` (function) — Detect running OpenClaw processes and services.
- L119 `_warn_if_openclaw_running(auto_yes: bool)` (function) — Warn if OpenClaw is still running before migration.
- L151 `_warn_if_gateway_running(auto_yes: bool)` (function) — Check if a Hermes gateway is running with connected platforms.
- L196 `_find_migration_script()` (function) — Find the openclaw_to_hermes.py script in known locations.
- L204 `_load_migration_module(script_path: Path)` (function) — Dynamically load the migration script as a module.
- L221 `_find_openclaw_dirs()` (function) — Find all OpenClaw directories on disk.
- L231 `_scan_workspace_state(source_dir: Path)` (function) — Scan an OpenClaw directory for workspace state files.
- L268 `_archive_directory(source_dir: Path, dry_run: bool=False)` (function) — Rename an OpenClaw directory to .pre-migration.
- L295 `claw_command(args)` (function) — Route hermes claw subcommands.
- L313 `_cmd_migrate(args)` (function) — Run the OpenClaw → Hermes migration.
- L558 `_cmd_cleanup(args)` (function) — Archive leftover OpenClaw directories after migration.
- L703 `_print_migration_report(report: dict, dry_run: bool)` (function) — Print a formatted migration report.
