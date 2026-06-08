---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_loopback_ssh_hint.py

Symbols in `tests/hermes_cli/test_auth_loopback_ssh_hint.py`.

- L18 `_cap(fn)` (function)
- L25 `test_loopback_ssh_hint_silent_when_not_remote(monkeypatch)` (function)
- L33 `test_loopback_ssh_hint_prints_tunnel_command_on_ssh(monkeypatch)` (function)
- L46 `test_loopback_ssh_hint_uses_actual_bound_port(monkeypatch)` (function) — When the preferred port is busy, _xai_start_callback_server falls back to
- L58 `test_loopback_ssh_hint_silent_for_non_loopback_uri(monkeypatch)` (function) — Defense in depth: if a future caller passes a non-loopback redirect URI
- L68 `test_loopback_ssh_hint_silent_for_malformed_uri(monkeypatch)` (function)
- L76 `test_loopback_ssh_hint_works_without_provider_docs_url(monkeypatch)` (function)
- L88 `test_loopback_ssh_hint_accepts_localhost_hostname(monkeypatch)` (function) — The constant is 127.0.0.1, but parsing tolerates `localhost` too in case
- L98 `test_loopback_ssh_hint_includes_user_at_host(monkeypatch)` (function) — The SSH command should include a detected user@host so the user can
- L109 `test_loopback_ssh_hint_has_visual_header(monkeypatch)` (function) — The hint should print a divider and header so it stands out in noisy output.
- L119 `TestSshUserAtHost` (class)
- L120 `test_resolves_user_and_hostname(self, monkeypatch)` (method)
- L126 `test_falls_back_to_logname(self, monkeypatch)` (method)
- L132 `test_placeholder_when_no_env_vars(self, monkeypatch)` (method)
- L138 `test_placeholder_when_socket_raises(self, monkeypatch)` (method)
- L145 `test_placeholder_when_empty_hostname(self, monkeypatch)` (method)
