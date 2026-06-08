---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/tts_registry.py

Symbols in `agent/tts_registry.py`.

- L66 `register_provider(provider: TTSProvider)` (function) — Register a TTS provider.
- L111 `list_providers()` (function) — Return all registered providers, sorted by name.
- L118 `get_provider(name: str)` (function) — Return the provider registered under *name*, or None.
- L130 `_reset_for_tests()` (function) — Clear the registry. **Test-only.**
