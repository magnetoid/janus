---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway_wsl.py

Symbols in `tests/hermes_cli/test_gateway_wsl.py`.

- L17 `TestIsWsl` (class) — Test the shared is_wsl() utility.
- L20 `setup_method(self)` (method)
- L24 `test_detects_wsl2(self)` (method)
- L32 `test_detects_wsl1(self)` (method)
- L40 `test_native_linux(self)` (method)
- L48 `test_no_proc_version(self)` (method)
- L52 `test_result_is_cached(self)` (method) — After first detection, subsequent calls return the cached value.
- L64 `TestWslSystemdOperational` (class) — Test the WSL systemd check.
- L67 `test_running(self, monkeypatch)` (method)
- L76 `test_degraded(self, monkeypatch)` (method)
- L85 `test_starting(self, monkeypatch)` (method)
- L94 `test_offline_no_systemd(self, monkeypatch)` (method)
- L103 `test_systemctl_not_found(self, monkeypatch)` (method)
- L110 `test_timeout(self, monkeypatch)` (method)
- L122 `TestSupportsSystemdServicesWSL` (class) — Test that supports_systemd_services() handles WSL correctly.
- L125 `test_wsl_with_systemd(self, monkeypatch)` (method) — WSL + working systemd → True.
- L133 `test_wsl_without_systemd(self, monkeypatch)` (method) — WSL + no systemd → False.
- L141 `test_native_linux(self, monkeypatch)` (method) — Native Linux (not WSL) → True without checking systemd.
- L148 `test_termux_still_excluded(self, monkeypatch)` (method) — Termux → False regardless of WSL status.
- L159 `TestGatewayCommandWSLMessages` (class) — Test that WSL users see appropriate guidance.
- L162 `test_install_wsl_no_systemd(self, monkeypatch, capsys)` (method) — hermes gateway install on WSL without systemd shows guidance.
- L193 `test_start_wsl_no_systemd(self, monkeypatch, capsys)` (method) — hermes gateway start on WSL without systemd shows guidance.
- L215 `test_status_wsl_running_manual(self, monkeypatch, capsys)` (method) — hermes gateway status on WSL with manual process shows WSL note.
- L243 `test_status_wsl_not_running(self, monkeypatch, capsys)` (method) — hermes gateway status on WSL with no process shows WSL start advice.
