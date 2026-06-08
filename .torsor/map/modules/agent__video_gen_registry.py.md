---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/video_gen_registry.py

Symbols in `agent/video_gen_registry.py`.

- L37 `register_provider(provider: VideoGenProvider)` (function) — Register a video generation provider.
- L61 `list_providers()` (function) — Return all registered providers, sorted by name.
- L68 `get_provider(name: str)` (function) — Return the provider registered under *name*, or None.
- L76 `get_active_provider()` (function) — Resolve the currently-active provider.
- L114 `_reset_for_tests()` (function) — Clear the registry. **Test-only.**
