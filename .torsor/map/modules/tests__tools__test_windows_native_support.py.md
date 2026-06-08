---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_windows_native_support.py

Symbols in `tests/tools/test_windows_native_support.py`.

- L28 `TestConfigureWindowsStdio` (class) — ``hermes_cli.stdio.configure_windows_stdio`` wiring.
- L41 `_reset_configured(self, monkeypatch)` (method) — Reload the module before each test so the _CONFIGURED flag resets.
- L52 `test_no_op_on_posix(self)` (method)
- L59 `test_idempotent(self)` (method)
- L66 `test_windows_path_sets_env_and_reconfigures_streams(self, monkeypatch)` (method)
- L104 `test_respects_existing_editor_var(self, monkeypatch)` (method) — User's explicit EDITOR wins over our default.
- L117 `test_respects_existing_visual_var(self, monkeypatch)` (method) — VISUAL takes precedence over our EDITOR default too.
- L134 `test_respects_existing_env_var(self, monkeypatch)` (method) — User's explicit PYTHONIOENCODING wins over our default.
- L147 `test_disable_flag_short_circuits(self, monkeypatch, optout)` (method)
- L164 `test_reconfigure_stream_handles_missing_method(self, monkeypatch)` (method) — StringIO-like objects without .reconfigure() must not blow up.
- L179 `TestTerminatePidRoutingOnWindows` (class) — ``gateway.status.terminate_pid`` must use taskkill /T /F on Windows.
- L188 `test_force_uses_taskkill_on_windows(self, monkeypatch)` (method)
- L211 `test_force_taskkill_failure_raises_oserror(self, monkeypatch)` (method)
- L226 `test_graceful_on_windows_uses_os_kill_sigterm(self, monkeypatch)` (method) — Non-force path calls os.kill with SIGTERM (Windows has no SIGKILL).
- L247 `test_taskkill_not_found_falls_back_to_os_kill(self, monkeypatch)` (method) — On Windows without taskkill (WinPE, containers), fall back gracefully.
- L274 `TestSigkillFallback` (class) — Modules that want SIGKILL must fall back to SIGTERM when absent.
- L277 `test_getattr_fallback_works_when_sigkill_missing(self, monkeypatch)` (method) — The `getattr(signal, "SIGKILL", signal.SIGTERM)` pattern.
- L287 `test_getattr_fallback_prefers_sigkill_when_present(self)` (method) — On POSIX the fallback is a no-op: real SIGKILL wins.
- L298 `test_module_uses_getattr_fallback(self, module_path, line_pattern)` (method) — Source-level check that our modules use the safe fallback.
- L320 `TestProcessRegistryOSErrorWidening` (class) — _is_host_pid_alive delegates to gateway.status._pid_exists.
- L323 `test_oserror_treated_as_not_alive(self, monkeypatch)` (method) — _pid_exists → False propagates as _is_host_pid_alive → False.
- L330 `test_permission_error_treated_as_alive(self, monkeypatch)` (method) — PermissionError is encoded by _pid_exists as alive=True; propagates as-is.
- L346 `test_zero_or_none_pid_returns_false_without_probing(self, monkeypatch)` (method) — No wasted syscall on falsy pids.
- L359 `test_alive_pid_returns_true(self, monkeypatch)` (method)
- L366 `TestPidExistsOSErrorWidening` (class) — gateway.status._pid_exists itself must widen Windows errors correctly.
- L375 `test_oserror_gone_pid_returns_false(self, monkeypatch)` (method) — Simulate Windows' OSError(WinError 87) for a gone PID via the POSIX fallback.
- L392 `test_permission_error_returns_true(self, monkeypatch)` (method) — POSIX fallback: PermissionError means alive (owned by another user).
- L414 `TestTzdataDependencyDeclared` (class) — Windows installs must pull tzdata for zoneinfo to work.
- L417 `test_pyproject_declares_tzdata_for_win32(self)` (method)
- L443 `TestReadmeNoLongerSaysWindowsUnsupported` (class) — The README shouldn't claim native Windows isn't supported.
- L446 `test_readme_does_not_say_not_supported(self)` (method)
- L455 `test_readme_mentions_powershell_installer(self)` (method)
- L468 `TestWebServerPtyBridgeGuard` (class) — The web server must not crash if pty_bridge can't import (Windows).
- L471 `test_import_guard_present_in_source(self)` (method)
- L479 `test_pty_handler_checks_availability_flag(self)` (method) — The /api/pty handler must short-circuit when the bridge is unavailable.
- L493 `TestEntryPointsConfigureStdio` (class) — cli.py, hermes_cli/main.py, gateway/run.py must call configure_windows_stdio.
- L500 `test_entry_point_calls_configure_stdio(self, relpath)` (method)
- L514 `TestSubprocessCompatHelpers` (class) — hermes_cli/_subprocess_compat.py POSIX + Windows behaviour.
- L517 `test_is_windows_matches_sys_platform(self)` (method)
- L521 `test_resolve_node_command_returns_absolute_on_posix(self)` (method) — On Linux, resolve_node_command('sh', ['-c','echo hi']) picks up /bin/sh.
- L532 `test_resolve_node_command_fallback_when_absent(self)` (method)
- L541 `test_windows_flags_zero_on_posix(self)` (method)
- L552 `test_windows_detach_popen_kwargs_is_posix_equivalent_on_posix(self)` (method)
- L569 `test_windows_detach_flags_has_expected_win32_bits(self, monkeypatch)` (method) — Simulate Windows to verify flag bundle.
- L581 `test_windows_detach_flags_includes_breakaway_from_job(self, monkeypatch)` (method) — CREATE_BREAKAWAY_FROM_JOB is load-bearing for the GUI-driven update path.
- L603 `test_windows_detach_flags_without_breakaway_drops_only_that_bit(self, monkeypatch)` (method) — Fallback retry payload for restrictive job objects.
- L632 `TestTuiGatewayEntrySignalGuards` (class) — Importing tui_gateway.entry must not crash when SIGPIPE/SIGHUP absent.
- L640 `test_source_guards_each_signal_installation(self)` (method)
- L653 `test_module_imports_cleanly(self)` (method) — Importing the module must not raise — verifies the guards work.
- L667 `TestKanbanWaitpidWindowsGuard` (class) — os.WNOHANG doesn't exist on Windows — the dispatcher tick reap loop
- L671 `test_source_gates_waitpid_loop(self)` (method)
- L700 `TestCodeExecutionTransportTcpFallback` (class) — The RPC transport must fall back to TCP on Windows.
- L708 `test_generated_client_handles_tcp_endpoint(self)` (method)
- L719 `test_server_side_branches_on_use_tcp_rpc(self)` (method)
- L731 `TestCronSchedulerBashResolution` (class) — cron.scheduler must NOT hardcode /bin/bash — .sh scripts need a
- L735 `test_source_uses_shutil_which_for_bash(self)` (method)
- L745 `test_error_message_when_bash_missing(self)` (method)
- L759 `TestNpmBareSpawnsResolved` (class) — Every spawn site that launches ``npm``/``npx`` must resolve via
- L773 `test_no_bare_npm_or_npx_in_popen_argv(self, relpath)` (method) — Reject ``subprocess.run(["npm", ...])`` / ``["npx", ...]`` patterns.
- L818 `TestLocalEnvironmentWindowsTempDir` (class) — LocalEnvironment.get_temp_dir must return a native Windows path on
- L822 `test_posix_path_preserved_on_linux(self)` (method) — Linux/macOS behaviour MUST be unchanged — return / tmp or
- L835 `test_source_has_windows_branch_using_hermes_home(self)` (method)
- L843 `TestLocalEnvironmentPathInjectionGated` (class) — The /usr/bin PATH injection in _make_run_env must be POSIX-only.
- L846 `test_source_gates_path_injection(self)` (method)
- L858 `TestGitBashPathNormalization` (class) — _normalize_git_bash_path should turn /c/Users/... into C:\Users\...
- L862 `test_posix_noop(self)` (method) — Must NOT mutate paths on Linux/macOS.
- L871 `test_empty_string_preserved(self)` (method)
- L875 `test_windows_translation(self, monkeypatch)` (method) — Simulate Windows and verify /c/Users/... becomes C:\Users\...
- L891 `TestWorktreeSymlinkFallback` (class) — .worktreeinclude directory symlinks must fall back to copytree on
- L895 `test_source_has_symlink_fallback(self)` (method)
- L911 `TestGatewayDetachedWatcherWindowsFlags` (class) — launch_detached_profile_gateway_restart and the in-gateway update
- L916 `test_hermes_cli_gateway_uses_compat_kwargs(self)` (method)
- L927 `test_gateway_run_update_has_windows_branch(self)` (method)
- L935 `test_launch_detached_profile_gateway_restart_inlined_watcher_uses_breakaway(self)` (method) — The inlined respawn script (stringified Python passed to ``python -c``)
- L966 `test_launch_detached_profile_gateway_restart_outer_popen_has_access_denied_fallback(self)` (method) — When the outer watcher Popen raises OSError (breakaway denied by
