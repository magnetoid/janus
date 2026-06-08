---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway_windows.py

Symbols in `tests/hermes_cli/test_gateway_windows.py`.

- L22 `test_schtasks_fallback_patterns_cover_localized_access_denied(detail)` (function) — Localized schtasks access-denied errors should use Startup fallback.
- L28 `test_schtasks_fallback_does_not_hide_unknown_errors()` (function)
- L32 `test_schtasks_encoding_falls_back_to_utf8(monkeypatch)` (function) — A broken/empty locale must not leave us without a decoder (issue #38172).
- L45 `test_exec_schtasks_decodes_with_replace_errors(monkeypatch)` (function) — schtasks output must be decoded with errors='replace' so localized
- L75 `test_build_gateway_argv_uses_base_pythonw_for_uv_venv_launcher(monkeypatch, tmp_path)` (function) — Avoid uv's venv pythonw launcher because it respawns console python.exe.
- L115 `TestStableWindowsGatewayWorkingDir` (class)
- L116 `test_stable_gateway_working_dir_uses_hermes_home(self, tmp_path, monkeypatch)` (method)
- L122 `test_stable_gateway_working_dir_falls_back_to_project_root(self, tmp_path, monkeypatch)` (method)
- L129 `test_write_task_script_anchors_cmd_cd_at_hermes_home(monkeypatch, tmp_path)` (function)
- L153 `_arrange_startup_fallback(monkeypatch, tmp_path, running_pids)` (function)
- L191 `test_gateway_cmd_script_uses_pythonw_without_replace_or_start_churn(monkeypatch)` (function) — Scheduled Task wrapper should launch pythonw once and avoid replace loops.
- L209 `test_elevated_gateway_command_uses_pythonw_hidden_console(monkeypatch)` (function) — UAC handoff should not leave a second elevated cmd.exe window open.
- L238 `test_install_scheduled_task_recreates_instead_of_change(monkeypatch, tmp_path)` (function) — Install must delete+create so stale minute-repeat task settings are not preserved.
- L264 `test_install_scheduled_task_success_start_now_uses_direct_spawn_not_task_run(monkeypatch, tmp_path, capsys)` (function) — Install start-now should not /Run the task; that preserved old restart loops.
- L294 `test_install_scheduled_task_success_does_not_auto_start(monkeypatch, tmp_path, capsys)` (function) — Install should register/update the task only; start is explicit.
- L324 `test_install_access_denied_launches_elevated_install_before_startup_fallback(monkeypatch, tmp_path, capsys)` (function) — Non-admin Scheduled Task access denied should hand off to UAC elevation.
- L360 `test_install_prompts_start_choices_before_uac(monkeypatch, tmp_path, capsys)` (function) — Windows install asks start-now and auto-start before any UAC handoff.
- L397 `test_install_start_now_without_login_autostart_never_escalates(monkeypatch, capsys)` (function) — If auto-start is declined, install can start directly without touching schtasks/UAC.
- L417 `test_start_noops_when_gateway_already_running(monkeypatch, capsys)` (function) — Repeated start should not invoke schtasks /Run or spawn another process.
- L435 `test_install_startup_fallback_does_not_spawn_when_gateway_already_running(monkeypatch, tmp_path, capsys)` (function) — Repeated Windows fallback installs should not spawn duplicate gateways.
- L450 `test_install_startup_fallback_does_not_auto_spawn_when_gateway_stopped(monkeypatch, tmp_path, capsys)` (function) — Startup fallback install should only install login item, not launch pythonw.
- L465 `test_install_access_denied_declined_elevation_uses_startup_fallback(monkeypatch, tmp_path, capsys)` (function) — Install should ask before UAC; declining keeps the non-jarring fallback path.
- L504 `test_uninstall_access_denied_prompts_before_elevating(monkeypatch, tmp_path, capsys)` (function) — Uninstall should hand off to an elevated uninstall only after user consent.
- L535 `test_uninstall_access_denied_declined_keeps_task_and_cleans_files(monkeypatch, tmp_path, capsys)` (function) — Declining UAC should not surprise the user, but should still remove user-writable artifacts.
- L582 `test_stop_writes_planned_stop_marker_before_killing(monkeypatch)` (function) — stop() must write the planned-stop marker BEFORE any kill signal.
- L628 `test_stop_waits_for_graceful_drain_before_force_kill(monkeypatch)` (function) — When drain succeeds, stop() should NOT force-kill the gateway.
- L667 `test_stop_escalates_to_force_kill_when_drain_times_out(monkeypatch)` (function) — When drain times out, stop() MUST escalate to force=True.
- L702 `test_stop_no_running_gateway_skips_drain(monkeypatch)` (function) — When no gateway is running, skip the drain wait entirely.
- L736 `test_drain_helper_handles_invalid_pid(monkeypatch)` (function) — _drain_gateway_pid returns False for invalid PIDs without crashing.
- L742 `test_drain_helper_returns_true_when_pid_exits_quickly(monkeypatch)` (function) — _drain_gateway_pid polls _pid_exists until it returns False.
- L758 `test_drain_helper_returns_false_on_timeout(monkeypatch)` (function) — _drain_gateway_pid returns False when the PID never exits.
- L767 `test_drain_helper_still_waits_if_marker_write_fails(monkeypatch)` (function) — Marker-write failures are swallowed; drain still polls for PID exit.
