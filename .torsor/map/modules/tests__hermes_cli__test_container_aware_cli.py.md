---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_container_aware_cli.py

Symbols in `tests/hermes_cli/test_container_aware_cli.py`.

- L25 `container_env(tmp_path, monkeypatch)` (function) — Set up a fake HERMES_HOME with .container-mode file.
- L43 `test_get_container_exec_info_returns_metadata(container_env)` (function) — Reads .container-mode and returns all fields including exec_user.
- L55 `test_get_container_exec_info_none_inside_container(container_env)` (function) — Returns None when we're already inside a container.
- L63 `test_get_container_exec_info_none_without_file(tmp_path, monkeypatch)` (function) — Returns None when .container-mode doesn't exist (native mode).
- L76 `test_get_container_exec_info_skipped_when_hermes_dev(container_env, monkeypatch)` (function) — Returns None when HERMES_DEV=1 is set (dev mode bypass).
- L86 `test_get_container_exec_info_not_skipped_when_hermes_dev_zero(container_env, monkeypatch)` (function) — HERMES_DEV=0 does NOT trigger bypass — only '1' does.
- L96 `test_get_container_exec_info_defaults()` (function) — Falls back to defaults for missing keys.
- L120 `test_get_container_exec_info_docker_backend(container_env)` (function) — Correctly reads docker backend with custom exec_user.
- L138 `test_get_container_exec_info_crashes_on_permission_error(container_env)` (function) — PermissionError propagates instead of being silently swallowed.
- L152 `docker_container_info()` (function)
- L162 `podman_container_info()` (function)
- L171 `test_exec_in_container_calls_execvp(docker_container_info)` (function) — Verifies os.execvp is called with correct args: runtime, tty flags,
- L203 `test_exec_in_container_non_tty_uses_i_only(docker_container_info)` (function) — Non-TTY mode uses -i instead of -it.
- L221 `test_exec_in_container_no_runtime_hard_fails(podman_container_info)` (function) — Hard fails when runtime not found (no fallback).
- L236 `test_exec_in_container_sudo_probe_sets_prefix(podman_container_info)` (function) — When first probe fails and sudo probe succeeds, execvp is called
- L268 `test_exec_in_container_probe_timeout_prints_message(docker_container_info)` (function) — TimeoutExpired from probe produces a human-readable error, not a
- L284 `test_exec_in_container_container_not_running_no_sudo(docker_container_info)` (function) — When runtime exists but container not found and no sudo available,
