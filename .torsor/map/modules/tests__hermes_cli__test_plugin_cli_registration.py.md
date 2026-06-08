---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_plugin_cli_registration.py

Symbols in `tests/hermes_cli/test_plugin_cli_registration.py`.

- L25 `TestRegisterCliCommand` (class)
- L26 `_make_ctx(self)` (method)
- L31 `test_registers_command(self)` (method)
- L50 `test_overwrites_on_duplicate(self)` (method)
- L56 `test_handler_optional(self)` (method)
- L65 `TestMemoryPluginCliDiscovery` (class)
- L66 `test_discovers_active_plugin_with_register_cli(self, tmp_path, monkeypatch)` (method) — Only the active memory provider's CLI commands are discovered.
- L112 `test_returns_nothing_when_no_active_provider(self, tmp_path, monkeypatch)` (method) — No commands when memory.provider is not set in config.
- L132 `test_skips_plugin_without_register_cli(self, tmp_path, monkeypatch)` (method) — An active plugin with cli.py but no register_cli returns nothing.
- L151 `test_skips_plugin_without_cli_py(self, tmp_path, monkeypatch)` (method) — An active provider without cli.py returns nothing.
- L175 `TestProviderCollectorCliNoop` (class)
- L176 `test_register_cli_command_is_noop(self)` (method) — _ProviderCollector.register_cli_command is a no-op (doesn't crash).
