---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/__init__.py

Symbols in `plugins/memory/__init__.py`.

- L42 `_register_synthetic_package(name: str, search_locations: List[str])` (function) — Register an empty package shell in sys.modules.
- L64 `_get_user_plugins_dir()` (function) — Return ``$HERMES_HOME/plugins/`` or None if unavailable.
- L74 `_is_memory_provider_dir(path: Path)` (function) — Heuristic: does *path* look like a memory provider plugin?
- L90 `_iter_provider_dirs()` (function) — Yield ``(name, path)`` for all discovered provider directories.
- L124 `find_provider_dir(name: str)` (function) — Resolve a provider name to its directory.
- L146 `discover_memory_providers()` (function) — Scan bundled and user-installed directories for available providers.
- L183 `load_memory_provider(name: str)` (function) — Load and return a MemoryProvider instance by name.
- L208 `_load_provider_from_dir(provider_dir: Path)` (function) — Import a provider module and extract the MemoryProvider instance.
- L319 `_ProviderCollector` (class) — Fake plugin context that captures register_memory_provider calls.
- L322 `__init__(self)` (method)
- L325 `register_memory_provider(self, provider)` (method)
- L329 `register_tool(self, *args, **kwargs)` (method)
- L332 `register_hook(self, *args, **kwargs)` (method)
- L335 `register_cli_command(self, *args, **kwargs)` (method)
- L339 `_get_active_memory_provider()` (function) — Read the active memory provider name from config.yaml.
- L354 `discover_plugin_cli_commands()` (function) — Return CLI commands for the **active** memory plugin only.
