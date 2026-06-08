---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/container_boot.py

Symbols in `hermes_cli/container_boot.py`.

- L48 `ReconcileAction` (class) — One profile's outcome from a single reconciliation pass.
- L55 `reconcile_profile_gateways(*, hermes_home: Path, scandir: Path, dry_run: bool=False, container_argv: Sequence[str] | None=None)` (function) — Recreate s6 service registrations for every persistent profile.
- L160 `_maybe_migrate_legacy_gateway_run_state(hermes_home: Path, *, container_argv: Sequence[str] | None, dry_run: bool)` (function) — Seed root gateway_state for pre-s6 `gateway run` containers.
- L197 `_read_container_argv()` (function) — Best-effort read of the container PID 1 argv.
- L206 `_is_legacy_gateway_run_request(argv: Sequence[str])` (function) — Return True for Docker commands equivalent to `gateway run`.
- L220 `_read_prior_state(profile_dir: Path)` (function) — Read gateway_state.json's ``gateway_state`` field, or None if
- L236 `_cleanup_stale_runtime_files(profile_dir: Path)` (function) — Remove gateway.pid and processes.json — they reference PIDs in
- L244 `_register_service(scandir: Path, profile: str, *, start: bool)` (function) — Recreate the s6 service slot for one profile.
- L329 `_write_reconcile_log(hermes_home: Path, actions: list[ReconcileAction])` (function) — Append one line per profile to $HERMES_HOME/logs/container-boot.log.
- L379 `main()` (function) — Entry point invoked from /etc/cont-init.d/02-reconcile-profiles.
