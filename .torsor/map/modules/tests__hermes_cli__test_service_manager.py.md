---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_service_manager.py

Symbols in `tests/hermes_cli/test_service_manager.py`.

- L30 `test_validate_profile_name_accepts_valid_names()` (function)
- L54 `test_validate_profile_name_rejects_invalid(bad: str)` (function)
- L64 `test_detect_service_manager_returns_known_value()` (function) — Without mocking, the function must still return one of the
- L77 `_patch_s6_paths(monkeypatch: pytest.MonkeyPatch, *, comm: str | OSError | None, basedir_is_dir: bool)` (function) — Stub /proc/1/comm and /run/s6/basedir for _s6_running tests.
- L107 `test_s6_running_true_when_comm_and_basedir_match(monkeypatch: pytest.MonkeyPatch)` (function)
- L116 `test_s6_running_false_when_comm_is_wrong(monkeypatch: pytest.MonkeyPatch)` (function)
- L126 `test_s6_running_false_when_basedir_missing(monkeypatch: pytest.MonkeyPatch)` (function)
- L137 `test_s6_running_false_when_comm_unreadable(monkeypatch: pytest.MonkeyPatch)` (function) — Regression: /proc/1/exe was unreadable to UID 10000 and
- L156 `test_s6_running_handles_missing_proc(monkeypatch: pytest.MonkeyPatch)` (function) — On macOS / Windows / WSL-without-procfs, /proc/1/comm doesn't
- L172 `test_systemd_manager_kind_and_registration_unsupported()` (function)
- L185 `test_launchd_manager_kind_and_registration_unsupported()` (function)
- L195 `test_windows_manager_kind_and_registration_unsupported()` (function)
- L209 `test_systemd_manager_lifecycle_delegates(monkeypatch: pytest.MonkeyPatch)` (function)
- L232 `test_launchd_manager_lifecycle_delegates(monkeypatch: pytest.MonkeyPatch)` (function)
- L254 `test_windows_manager_lifecycle_delegates(monkeypatch: pytest.MonkeyPatch)` (function)
- L284 `test_windows_manager_is_running_false_when_not_installed(monkeypatch: pytest.MonkeyPatch)` (function)
- L301 `test_windows_manager_install_forwards_kwargs(monkeypatch: pytest.MonkeyPatch)` (function)
- L338 `test_get_service_manager_returns_correct_backend(monkeypatch: pytest.MonkeyPatch, kind: ServiceManagerKind, cls: type)` (function)
- L349 `test_get_service_manager_raises_when_unsupported(monkeypatch: pytest.MonkeyPatch)` (function)
- L359 `test_get_service_manager_returns_s6_instance(monkeypatch: pytest.MonkeyPatch)` (function) — The s6 backend ships in Phase 3 — the factory must return an
- L376 `s6_scandir(tmp_path)` (function) — Empty scandir for the S6ServiceManager tests.
- L384 `fake_subprocess_run(monkeypatch: pytest.MonkeyPatch)` (function) — Capture subprocess.run calls + always return success. Lets the
- L407 `test_s6_manager_kind_and_supports_registration()` (function)
- L425 `test_seed_supervise_skeleton_creates_expected_layout(tmp_path)` (function) — Verifies the dirs + FIFO + modes the helper lays down.
- L462 `test_seed_supervise_skeleton_handles_log_subservice(tmp_path)` (function) — When a log/ subdir exists, its supervise tree also gets seeded.
- L492 `test_seed_supervise_skeleton_skips_when_no_log_subservice(tmp_path)` (function) — If log/ isn't present, no logger skeleton is created.
- L506 `test_seed_supervise_skeleton_is_idempotent(tmp_path)` (function) — Calling the helper twice on the same dir is a no-op the second time.
- L522 `test_s6_register_creates_service_dir_and_triggers_scan(s6_scandir, fake_subprocess_run)` (function)
- L575 `test_s6_register_extra_env_is_quoted(s6_scandir, fake_subprocess_run)` (function)
- L586 `test_render_run_script_resets_home_before_exec()` (function)
- L594 `test_s6_register_rejects_invalid_profile_name(s6_scandir)` (function)
- L600 `test_s6_register_rejects_duplicate(s6_scandir, fake_subprocess_run)` (function)
- L607 `test_s6_register_rolls_back_on_svscanctl_failure(s6_scandir, monkeypatch: pytest.MonkeyPatch)` (function) — If s6-svscanctl fails the service dir must be cleaned up so the
- L627 `test_s6_unregister_removes_service_dir(s6_scandir, fake_subprocess_run)` (function)
- L648 `test_s6_unregister_absent_profile_is_noop(s6_scandir)` (function)
- L653 `test_s6_list_profile_gateways(s6_scandir)` (function)
- L665 `test_s6_list_profile_gateways_empty_when_scandir_missing(tmp_path)` (function)
- L670 `test_s6_lifecycle_dispatches_to_s6_svc(s6_scandir, fake_subprocess_run)` (function)
- L691 `test_lifecycle_raises_gateway_not_registered_for_missing_slot(s6_scandir, fake_subprocess_run)` (function) — When the service slot doesn't exist, the lifecycle methods
- L720 `test_all_lifecycle_methods_check_for_missing_slot(s6_scandir, fake_subprocess_run, action: str, method_name: str)` (function) — start/stop/restart all check for missing slots the same way.
- L736 `test_gateway_not_registered_unprefixed_service_name(s6_scandir)` (function) — If the caller passes a name without the 'gateway-' prefix (the
- L751 `test_lifecycle_raises_s6_command_error_on_subprocess_failure(s6_scandir, monkeypatch: pytest.MonkeyPatch)` (function) — When s6-svc itself fails (non-zero exit) — e.g. EACCES on the
- L784 `test_s6_is_running_parses_svstat(s6_scandir, monkeypatch: pytest.MonkeyPatch)` (function)
