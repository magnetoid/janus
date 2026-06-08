---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway.py

Symbols in `tests/hermes_cli/test_gateway.py`.

- L11 `_install_fake_gateway_run(monkeypatch, start_gateway)` (function)
- L32 `test_run_gateway_exits_cleanly_on_keyboard_interrupt(monkeypatch, capsys)` (function)
- L53 `test_run_gateway_exits_nonzero_when_start_gateway_reports_failure(monkeypatch)` (function)
- L70 `test_run_gateway_refuses_root_in_official_docker(monkeypatch, tmp_path, capsys)` (function)
- L89 `test_run_gateway_root_guard_has_escape_hatch(monkeypatch)` (function)
- L107 `test_run_gateway_windows_foreground_keeps_ctrl_c_enabled(monkeypatch)` (function)
- L137 `test_run_gateway_windows_detached_absorbs_console_controls(monkeypatch)` (function)
- L167 `TestSystemdLingerStatus` (class)
- L168 `test_reports_enabled(self, monkeypatch)` (method)
- L181 `test_reports_disabled(self, monkeypatch)` (method)
- L194 `test_reports_termux_as_not_supported(self, monkeypatch)` (method)
- L200 `TestContainerSystemdSupport` (class)
- L201 `test_supports_systemd_services_in_container_with_user_manager(self, monkeypatch)` (method)
- L211 `test_supports_systemd_services_in_container_with_system_manager(self, monkeypatch)` (method)
- L221 `test_supports_systemd_services_in_container_without_systemd(self, monkeypatch)` (method)
- L232 `test_gateway_install_in_container_with_operational_systemd_uses_systemd(monkeypatch)` (function)
- L263 `test_gateway_start_in_container_with_operational_systemd_uses_systemd(monkeypatch)` (function)
- L277 `test_gateway_restart_on_windows_without_service_uses_detached_backend(monkeypatch)` (function) — Windows manual restart must not fall back to foreground run_gateway().
- L313 `test_gateway_restart_on_windows_preserves_failure_fallback(monkeypatch)` (function) — If the Windows backend cannot launch, keep the existing fallback.
- L338 `test_systemd_status_warns_when_linger_disabled(monkeypatch, tmp_path, capsys)` (function)
- L368 `test_systemd_install_checks_linger_status(monkeypatch, tmp_path, capsys)` (function)
- L395 `test_systemd_install_can_skip_enable_on_startup(monkeypatch, tmp_path, capsys)` (function)
- L423 `test_systemd_install_system_scope_skips_linger_and_uses_systemctl(monkeypatch, tmp_path, capsys)` (function)
- L458 `test_conflicting_systemd_units_warning(monkeypatch, tmp_path, capsys)` (function)
- L480 `test_install_linux_gateway_from_setup_system_choice_without_root_prints_followup(monkeypatch, capsys)` (function)
- L494 `test_install_linux_gateway_from_setup_system_choice_as_root_installs(monkeypatch)` (function)
- L512 `test_install_linux_gateway_from_setup_passes_startup_choice(monkeypatch)` (function)
- L528 `test_gateway_install_can_decline_start_now_and_startup(monkeypatch)` (function)
- L554 `test_find_gateway_pids_falls_back_to_pid_file_when_process_scan_fails(monkeypatch)` (function)
- L582 `test_scan_gateway_pids_detects_windows_hermes_exe_case_variants(monkeypatch)` (function)
- L609 `TestWaitForGatewayExit` (class) — PID-based wait with force-kill on timeout.
- L612 `test_returns_immediately_when_no_pid(self, monkeypatch)` (method) — If get_running_pid returns None, exit instantly.
- L618 `test_returns_when_process_exits_gracefully(self, monkeypatch)` (method) — Process exits after a couple of polls — no SIGKILL needed.
- L634 `test_force_kills_after_grace_period(self, monkeypatch)` (method) — When the process doesn't exit, force-kill the saved PID.
- L662 `test_handles_process_already_gone_on_kill(self, monkeypatch)` (method) — ProcessLookupError during force-kill is not fatal.
- L682 `test_kill_gateway_processes_force_uses_helper(self, monkeypatch)` (method)
- L694 `TestStopProfileGateway` (class)
- L695 `test_stop_profile_gateway_keeps_pid_file_when_process_still_running(self, monkeypatch)` (method)
- L723 `test_module_has_logger()` (function) — Verify module has a logger instance (regression guard for #27154).
