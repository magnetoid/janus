---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/providers/test_plugin_discovery.py

Symbols in `tests/providers/test_plugin_discovery.py`.

- L19 `_clear_provider_caches()` (function) — Force providers/__init__.py to re-discover on next list_providers().
- L34 `test_bundled_plugins_discovered()` (function) — Every plugins/model-providers/<name>/ should contain a plugin.yaml + __init__.py.
- L47 `test_all_profiles_register()` (function) — After discovery, the registry must contain every bundled provider directory.
- L76 `test_user_plugin_overrides_bundled(tmp_path, monkeypatch)` (function) — A user plugin with the same name must override the bundled profile.
- L122 `test_general_plugin_manager_skips_model_provider_kind(tmp_path, monkeypatch)` (function) — The general PluginManager must NOT import model-provider plugins
