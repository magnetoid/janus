---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platform_registry.py

Symbols in `gateway/platform_registry.py`.

- L39 `PlatformEntry` (class) — Metadata and factory for a single platform adapter.
- L162 `PlatformRegistry` (class) — Central registry of platform adapters.
- L169 `__init__(self)` (method)
- L172 `register(self, entry: PlatformEntry)` (method) — Register a platform adapter entry.
- L189 `unregister(self, name: str)` (method) — Remove a platform entry.  Returns True if it existed.
- L193 `get(self, name: str)` (method) — Look up a platform entry by name.
- L197 `all_entries(self)` (method) — Return all registered platform entries.
- L201 `plugin_entries(self)` (method) — Return only plugin-registered platform entries.
- L205 `is_registered(self, name: str)` (method)
- L208 `create_adapter(self, name: str, config: Any)` (method) — Create an adapter instance for the given platform name.
