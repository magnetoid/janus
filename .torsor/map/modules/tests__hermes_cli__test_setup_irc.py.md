---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_setup_irc.py

Symbols in `tests/hermes_cli/test_setup_irc.py`.

- L13 `_register_irc_platform(**overrides)` (function) — Manually register the IRC platform entry as if discover_plugins() found it.
- L51 `_unregister_irc_platform()` (function)
- L58 `TestIRCFreshInstallDiscovery` (class) — IRC appears in the setup menu on a brand-new Hermes install.
- L61 `test_irc_appears_in_all_platforms(self, monkeypatch)` (method) — When the IRC plugin is registered, _all_platforms() surfaces it.
- L81 `test_irc_status_not_configured_when_fresh(self, monkeypatch)` (method) — On a fresh install with no env vars, IRC shows 'not configured'.
- L95 `test_irc_status_configured_when_env_set(self, monkeypatch)` (method) — After the user sets IRC_SERVER and IRC_CHANNEL, status is 'configured'.
- L110 `test_irc_status_partial_when_only_server_set(self, monkeypatch)` (method) — If only IRC_SERVER is set, the platform is still not configured.
- L129 `TestIRCInteractiveSetup` (class) — The setup UI dispatches to IRC's interactive_setup() correctly.
- L132 `test_configure_platform_dispatches_to_irc_setup_fn(self, monkeypatch, capsys)` (method) — _configure_platform() calls the IRC plugin's setup_fn when selected.
- L153 `test_configure_platform_fallback_when_no_setup_fn(self, monkeypatch, capsys)` (method) — A plugin with no setup_fn falls back to env-var instructions.
- L171 `TestIRCGatewaySetupFreshInstall` (class) — Simulate the full `hermes setup gateway` experience with IRC present.
- L174 `test_setup_gateway_shows_irc_in_platform_menu(self, monkeypatch, capsys, tmp_path)` (method) — The gateway setup menu lists IRC among the available platforms.
- L220 `test_setup_gateway_irc_counts_as_messaging_platform(self, monkeypatch, capsys, tmp_path)` (method) — When IRC is configured, setup_gateway counts it as a messaging platform.
