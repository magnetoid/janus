---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_ssh_environment.py

Symbols in `tests/tools/test_ssh_environment.py`.

- L26 `_run(command, task_id='ssh_test', **kwargs)` (function)
- L31 `_cleanup(task_id='ssh_test')` (function)
- L36 `TestBuildSSHCommand` (class)
- L39 `_mock_connection(self, monkeypatch)` (method)
- L48 `test_base_flags(self)` (method)
- L55 `test_custom_port(self)` (method)
- L60 `test_key_path(self)` (method)
- L65 `test_user_host_suffix(self)` (method)
- L70 `TestControlSocketPath` (class) — Regression tests for issue #11840.
- L81 `_mock_connection(self, monkeypatch)` (method)
- L96 `test_fits_under_macos_socket_limit_with_ipv6_host(self, monkeypatch)` (method) — A realistic macOS $TMPDIR + IPv6 host must still produce a
- L123 `test_path_is_deterministic_across_instances(self)` (method) — Same (user, host, port) must yield the same control socket so
- L130 `test_path_differs_for_different_targets(self)` (method) — Different (user, host, port) triples must produce different paths.
- L138 `TestTerminalToolConfig` (class)
- L139 `test_ssh_persistent_default_true(self, monkeypatch)` (method) — SSH persistent defaults to True (via TERMINAL_PERSISTENT_SHELL).
- L146 `test_ssh_persistent_explicit_false(self, monkeypatch)` (method) — Per-backend env var overrides the global default.
- L152 `test_ssh_persistent_explicit_true(self, monkeypatch)` (method)
- L157 `test_ssh_persistent_respects_config(self, monkeypatch)` (method) — TERMINAL_PERSISTENT_SHELL=false disables SSH persistent by default.
- L165 `TestSSHPreflight` (class)
- L166 `test_ensure_ssh_available_raises_clear_error_when_missing(self, monkeypatch)` (method)
- L172 `test_ssh_environment_checks_availability_before_connect(self, monkeypatch)` (method)
- L183 `test_ssh_environment_connects_when_ssh_exists(self, monkeypatch)` (method)
- L204 `_setup_ssh_env(monkeypatch, persistent: bool)` (function)
- L216 `TestOneShotSSH` (class)
- L219 `_setup(self, monkeypatch)` (method)
- L224 `test_echo(self)` (method)
- L229 `test_exit_code(self)` (method)
- L233 `test_state_does_not_persist(self)` (method)
- L240 `TestPersistentSSH` (class)
- L243 `_setup(self, monkeypatch)` (method)
- L248 `test_echo(self)` (method)
- L253 `test_env_var_persists(self)` (method)
- L258 `test_cwd_persists(self)` (method)
- L263 `test_exit_code(self)` (method)
- L267 `test_stderr(self)` (method)
- L272 `test_multiline_output(self)` (method)
- L277 `test_timeout_then_recovery(self)` (method)
- L284 `test_large_output(self)` (method)
