---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_live_system_guard_self_test.py

Symbols in `tests/test_live_system_guard_self_test.py`.

- L34 `test_os_kill_blocks_foreign_pid()` (function)
- L39 `test_os_kill_blocks_negative_one()` (function) — ``os.kill(-1, sig)`` signals every process we can reach. Must be blocked.
- L46 `test_os_killpg_blocks_foreign_pgid()` (function)
- L54 `test_subprocess_run_systemctl_restart_blocked()` (function)
- L59 `test_subprocess_run_full_path_systemctl_blocked()` (function) — ``/usr/bin/systemctl`` (full path) must be blocked too.
- L65 `test_subprocess_run_sudo_systemctl_blocked()` (function) — ``sudo systemctl ...`` defeated the old head==systemctl check.
- L71 `test_subprocess_run_env_systemctl_blocked()` (function) — ``env systemctl ...`` similarly defeated the old head check.
- L77 `test_subprocess_run_bash_c_systemctl_blocked()` (function) — ``bash -c "systemctl ..."`` must also be caught.
- L83 `test_subprocess_run_sh_c_systemctl_blocked()` (function)
- L88 `test_subprocess_run_setsid_systemctl_blocked()` (function)
- L93 `test_subprocess_run_string_shell_true_blocked()` (function)
- L101 `test_subprocess_popen_systemctl_blocked()` (function)
- L106 `test_subprocess_call_systemctl_blocked()` (function)
- L111 `test_subprocess_check_call_systemctl_blocked()` (function)
- L116 `test_subprocess_check_output_systemctl_blocked()` (function)
- L121 `test_subprocess_getoutput_systemctl_blocked()` (function)
- L126 `test_subprocess_getstatusoutput_systemctl_blocked()` (function)
- L134 `test_os_system_systemctl_blocked()` (function)
- L139 `test_os_popen_systemctl_blocked()` (function)
- L147 `test_pty_spawn_systemctl_blocked()` (function)
- L156 `test_asyncio_create_subprocess_exec_systemctl_blocked()` (function)
- L168 `test_asyncio_create_subprocess_shell_systemctl_blocked()` (function)
- L183 `test_subprocess_pkill_hermes_blocked()` (function)
- L188 `test_subprocess_pkill_hermes_gateway_blocked()` (function)
- L193 `test_subprocess_pkill_python_dash_f_blocked()` (function) — ``pkill -f python`` matches the gateway's "python -m hermes_cli.main".
- L199 `test_subprocess_killall_hermes_blocked()` (function)
- L207 `test_systemctl_status_passes_through()` (function) — Read-only systemctl probes (status/show/list-units) are fine.
- L219 `test_systemctl_show_passes_through()` (function)
- L229 `test_systemctl_list_units_passes_through()` (function)
- L239 `test_systemctl_unrelated_unit_passes_through()` (function) — systemctl restart of a non-hermes unit is allowed (we only protect hermes).
- L254 `test_kill_own_subtree_passes_through()` (function) — We CAN kill our own children — guard recognizes them via psutil.
- L265 `test_subprocess_pkill_with_unrelated_pattern_passes_through()` (function) — ``pkill -f some-unrelated-pattern`` (no hermes/python) is fine.
- L275 `test_normal_subprocess_run_passes_through()` (function) — Plain non-systemctl subprocess.run should work normally.
- L285 `test_bypass_marker_disables_guard()` (function) — The bypass marker exists for tests that genuinely need real signal delivery
