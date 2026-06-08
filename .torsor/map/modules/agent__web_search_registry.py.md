---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/web_search_registry.py

Symbols in `agent/web_search_registry.py`.

- L48 `register_provider(provider: WebSearchProvider)` (function) — Register a web search/extract provider.
- L78 `list_providers()` (function) — Return all registered providers, sorted by name.
- L85 `get_provider(name: str)` (function) — Return the provider registered under *name*, or None.
- L98 `_read_config_key(*path: str)` (function) — Resolve a dotted config key from ``config.yaml``. Returns None on miss.
- L133 `_resolve(configured: Optional[str], *, capability: str)` (function) — Resolve the active provider for a capability ("search" | "extract").
- L222 `get_active_search_provider()` (function) — Resolve the currently-active web search provider.
- L232 `get_active_extract_provider()` (function) — Resolve the currently-active web extract provider.
- L242 `_reset_for_tests()` (function) — Clear the registry. **Test-only.**
