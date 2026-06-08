---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/gateway_windows.py

Symbols in `hermes_cli/gateway_windows.py`.

- L56 `_schtasks_encoding()` (function) — Best-effort console encoding for decoding ``schtasks.exe`` output.
- L74 `_assert_windows()` (function)
- L83 `_quote_cmd_script_arg(value: str)` (function) — Quote a single argument for use INSIDE a .cmd file, for cmd.exe parsing.
- L99 `_quote_schtasks_arg(value: str)` (function) — Quote a single argument for schtasks.exe's /TR parser.
- L115 `_exec_schtasks(args: list[str])` (function) — Run ``schtasks.exe`` with a hard timeout. Return (code, stdout, stderr).
- L149 `_should_fall_back(code: int, detail: str)` (function)
- L153 `_is_access_denied(detail: str)` (function)
- L157 `_is_running_as_admin()` (function) — Return True when the current Windows process is elevated.
- L166 `_current_profile_cli_args()` (function) — Return CLI args that preserve the current Hermes profile.
- L174 `_launch_elevated_gateway_command(command: str, extra_args: list[str] | None=None)` (function) — Launch an elevated gateway subcommand via UAC and return True on handoff.
- L206 `_launch_elevated_install(force: bool=False, *, start_now: bool | None=None, start_on_login: bool | None=None)` (function) — Launch an elevated gateway install via UAC and return True on handoff.
- L242 `_launch_elevated_uninstall()` (function) — Launch an elevated gateway uninstall via UAC and return True on handoff.
- L251 `get_task_name()` (function) — Scheduled Task name, scoped per profile.
- L267 `_sanitize_filename(value: str)` (function) — Remove characters illegal in Windows filenames.
- L272 `get_task_script_path()` (function) — The generated ``gateway.cmd`` wrapper that the schtasks entry invokes.
- L287 `_startup_dir()` (function)
- L306 `get_startup_entry_path()` (function)
- L315 `_stable_gateway_working_dir(project_root: Path)` (function) — Return a stable cwd for detached/startup gateway runs.
- L338 `_build_gateway_cmd_script(python_path: str, working_dir: str, hermes_home: str, profile_arg: str)` (function) — Build the ``gateway.cmd`` wrapper content (CRLF-terminated).
- L382 `_build_startup_launcher(script_path: Path)` (function) — The tiny .cmd that goes in the Startup folder. Just minimizes and chains.
- L407 `_write_task_script()` (function) — Generate and write the gateway.cmd wrapper. Return its absolute path.
- L435 `_resolve_task_user()` (function) — Return ``DOMAIN\USER`` if available, else bare USERNAME, else None.
- L446 `_install_scheduled_task(task_name: str, script_path: Path)` (function) — Create or replace the Scheduled Task. Returns (success, detail).
- L496 `_install_startup_entry(script_path: Path)` (function) — Write the Startup-folder fallback launcher. Returns its path.
- L506 `_derive_venv_pythonw(python_exe: str)` (function) — Given a ``python.exe`` path, return the sibling ``pythonw.exe`` if present.
- L522 `_read_pyvenv_cfg(venv_dir: Path)` (function)
- L537 `_resolve_detached_python(python_exe: str)` (function) — Return (windowed_python, venv_dir, extra_pythonpath) for detached runs.
- L562 `_prepend_pythonpath(env_overlay: dict[str, str], entries: list[str])` (function)
- L572 `_build_gateway_argv()` (function) — Build (argv, working_dir, env_overlay) for the gateway subprocess.
- L608 `_spawn_detached(script_path: Path | None=None)` (function) — Launch the gateway as a fully detached background process.
- L684 `_install_choice_from_env(name: str)` (function)
- L696 `_prompt_install_choices(start_now: bool | None=None, start_on_login: bool | None=None)` (function) — Return (start_now, start_on_login), asking before any UAC escalation.
- L722 `_install_startup_fallback(script_path: Path, start_now: bool, detail: str)` (function) — Install the Startup-folder fallback and optionally start once.
- L749 `install(force: bool=False, *, start_now: bool | None=None, start_on_login: bool | None=None, elevated_handoff: bool=False)` (function) — Install the gateway as a Windows Scheduled Task (with Startup fallback).
- L875 `_wait_for_gateway_ready(timeout_s: float=6.0, interval_s: float=0.4)` (function) — Poll for a live gateway process for up to ``timeout_s`` seconds.
- L892 `_report_gateway_start(via: str)` (function)
- L904 `_print_next_steps()` (function)
- L914 `uninstall()` (function) — Remove both the Scheduled Task and the Startup-folder fallback, if present.
- L962 `is_task_registered()` (function)
- L967 `is_startup_entry_installed()` (function)
- L971 `is_installed()` (function) — True when either the schtasks entry or the Startup fallback is present.
- L976 `query_task_status()` (function) — Parse ``schtasks /Query /V /FO LIST`` and pull the interesting keys.
- L998 `_gateway_pids()` (function) — Reuse the cross-platform PID scanner in gateway.py.
- L1005 `_print_deep_probes()` (function) — Print PASS/FAIL per individual probe of gateway liveness.
- L1138 `status(deep: bool=False)` (function) — Print a status report for the Windows gateway service.
- L1178 `start()` (function) — Start the gateway. Prefers /Run on the scheduled task if present.
- L1216 `_drain_gateway_pid(pid: int, drain_timeout: float)` (function) — Write the planned-stop marker and wait for the gateway PID to exit.
- L1252 `stop()` (function) — Stop the gateway.
- L1305 `restart()` (function) — Stop the gateway then start it again.
