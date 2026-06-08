---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# providers/__init__.py

Symbols in `providers/__init__.py`.

- L53 `register_provider(profile: ProviderProfile)` (function) — Register a provider profile by name and aliases.
- L65 `get_provider_profile(name: str)` (function) — Look up a provider profile by name or alias.
- L76 `list_providers()` (function) — Return all registered provider profiles (one per canonical name).
- L91 `_user_plugins_dir()` (function) — Return ``$HERMES_HOME/plugins/model-providers/`` if it exists.
- L102 `_import_plugin_dir(plugin_dir: Path, source: str)` (function) — Import a single plugin directory so it self-registers.
- L140 `_discover_providers()` (function) — Populate the registry by importing every provider plugin.
