---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_container_boot.py

Symbols in `tests/hermes_cli/test_container_boot.py`.

- L28 `_make_profile(hermes_home: Path, name: str, *, state: str | None, with_pid: bool=False, config: bool=True)` (function) — Create a fake profile directory under hermes_home/profiles/<name>/.
- L55 `_seed_default_root(hermes_home: Path, *, state: str | None=None, with_pid: bool=False)` (function) — Populate gateway_state.json / stale runtime files at the
- L74 `_named_actions(actions: list[ReconcileAction])` (function) — Drop the always-present default-profile action so tests that
- L85 `test_running_profile_is_registered_and_autostarted(tmp_path: Path)` (function)
- L104 `test_stopped_profile_is_registered_but_not_started(tmp_path: Path)` (function)
- L119 `test_startup_failed_does_not_autostart(tmp_path: Path)` (function) — Avoid crash-loop on restart when the gateway was failing to boot.
- L133 `test_starting_state_does_not_autostart(tmp_path: Path)` (function) — `starting` means the gateway died mid-boot last time; treat as
- L147 `test_stale_runtime_files_are_removed(tmp_path: Path)` (function)
- L161 `test_profile_without_state_file_is_registered_but_not_started(tmp_path: Path)` (function) — A freshly-created profile that's never been started: register
- L179 `test_directory_without_marker_file_is_skipped(tmp_path: Path)` (function) — A stray dir under profiles/ that isn't actually a profile (no
- L194 `test_corrupt_state_file_treated_as_no_prior_state(tmp_path: Path)` (function) — If gateway_state.json is malformed JSON, don't blow up the whole
- L210 `test_reconcile_log_is_written(tmp_path: Path)` (function)
- L226 `test_reconcile_log_rotates_when_size_exceeded(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — When container-boot.log exceeds _LOG_ROTATE_BYTES, the existing
- L257 `test_reconcile_log_does_not_rotate_below_threshold(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — A small existing log is appended to in place; no .1 is created.
- L282 `test_reconcile_log_rotation_overwrites_existing_dot1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Rotating again replaces the prior .1 — we keep at most one
- L308 `test_dry_run_makes_no_filesystem_changes(tmp_path: Path)` (function)
- L326 `test_missing_profiles_root_still_registers_default_slot(tmp_path: Path)` (function) — When $HERMES_HOME/profiles doesn't exist (fresh install), the
- L345 `test_invalid_profile_name_in_directory_raises(tmp_path: Path)` (function) — A profile dir whose name doesn't match validate_profile_name's
- L357 `test_register_service_publishes_atomically(tmp_path: Path)` (function) — The reconciler should build the new service dir in a sibling
- L385 `test_register_service_overwrites_existing_slot(tmp_path: Path)` (function) — A second reconciliation pass cleanly replaces an existing
- L414 `test_register_service_cleans_up_stale_tmp_dir(tmp_path: Path)` (function) — If a previous interrupted run left a .tmp sibling directory,
- L437 `test_default_slot_always_registered_on_empty_home(tmp_path: Path)` (function) — Bare HERMES_HOME with nothing under it still produces a
- L455 `test_default_slot_run_script_omits_profile_flag(tmp_path: Path)` (function) — The default slot's run script must NOT pass `-p default` —
- L471 `test_default_slot_autostarts_when_root_state_running(tmp_path: Path)` (function) — gateway_state.json at the HERMES_HOME root with state=running
- L494 `test_legacy_gateway_run_cmd_seeds_default_running_state(tmp_path: Path, container_argv: tuple[str, ...])` (function) — Pre-s6 Docker users often ran `gateway run` as the container
- L526 `test_legacy_gateway_run_no_supervise_does_not_seed_s6_state(tmp_path: Path, container_argv: tuple[str, ...])` (function) — `gateway run --no-supervise` is an explicit opt-out from s6 migration.
- L547 `test_legacy_gateway_run_env_no_supervise_does_not_seed_s6_state(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Env opt-out matches the CLI `--no-supervise` flag.
- L569 `test_default_slot_does_not_autostart_when_root_state_stopped(tmp_path: Path)` (function)
- L589 `test_default_slot_does_not_autostart_when_root_state_startup_failed(tmp_path: Path)` (function) — Crash-loop guard applies to the default slot too.
- L604 `test_default_slot_cleans_up_stale_runtime_files_at_root(tmp_path: Path)` (function) — gateway.pid and processes.json at the HERMES_HOME root (left
- L622 `test_default_slot_appears_before_named_profiles(tmp_path: Path)` (function) — The action list is ordered: default first, then named profiles
- L641 `test_profiles_default_subdir_is_skipped_with_warning(tmp_path: Path, caplog: pytest.LogCaptureFixture)` (function) — A user-created profiles/default/ collides with the reserved
