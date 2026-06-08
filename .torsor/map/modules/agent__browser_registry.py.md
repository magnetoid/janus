---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/browser_registry.py

Symbols in `agent/browser_registry.py`.

- L52 `register_provider(provider: BrowserProvider)` (function) — Register a cloud browser provider.
- L82 `list_providers()` (function) — Return all registered providers, sorted by name.
- L89 `get_provider(name: str)` (function) — Return the provider registered under *name*, or None.
- L113 `_resolve(configured: Optional[str])` (function) — Resolve the active browser provider.
- L189 `_reset_for_tests()` (function) — Clear the registry. **Test-only.**
