---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_plugin_platform_interface.py

Symbols in `tests/gateway/test_plugin_platform_interface.py`.

- L21 `_discover_platform_plugins()` (function) — Return names of all bundled platform plugins.
- L37 `clean_registry()` (function) — Yield with a clean platform registry, restoring state afterwards.
- L48 `_MockPluginContext` (class) — Minimal mock of hermes_cli.plugins.PluginContext.
- L55 `__init__(self)` (method)
- L58 `register_platform(self, *, name: str, label: str, adapter_factory: Any, check_fn: Any, **kwargs: Any)` (method)
- L80 `_import_platform_module(name: str)` (function) — Import plugins.platforms.<name> in a test-safe way.
- L90 `test_plugin_exposes_register_function(platform_name: str)` (function) — Every platform plugin must expose a callable register function.
- L98 `test_plugin_registers_valid_platform_entry(platform_name: str, clean_registry)` (function) — Calling register() must create a valid PlatformEntry.
- L116 `test_platform_entry_has_required_fields(platform_name: str, clean_registry)` (function) — PlatformEntry must have the mandatory metadata fields.
- L142 `test_adapter_factory_produces_valid_adapter(platform_name: str, clean_registry)` (function) — The adapter factory must return an object with the base interface.
- L179 `test_check_fn_returns_bool(platform_name: str, clean_registry)` (function) — check_fn() must return a boolean.
- L194 `test_validate_config_if_present(platform_name: str, clean_registry)` (function) — If validate_config is provided, it must accept a config object.
- L214 `test_is_connected_if_present(platform_name: str, clean_registry)` (function) — If is_connected is provided, it must accept a config object.
