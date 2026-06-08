---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/image_gen_registry.py

Symbols in `agent/image_gen_registry.py`.

- L36 `register_provider(provider: ImageGenProvider)` (function) — Register an image generation provider.
- L60 `list_providers()` (function) — Return all registered providers, sorted by name.
- L67 `get_provider(name: str)` (function) — Return the provider registered under *name*, or None.
- L75 `get_active_provider()` (function) — Resolve the currently-active provider.
- L142 `_reset_for_tests()` (function) — Clear the registry. **Test-only.**
