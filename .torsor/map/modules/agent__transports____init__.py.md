---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/__init__.py

Symbols in `agent/transports/__init__.py`.

- L21 `register_transport(api_mode: str, transport_cls: type)` (function) — Register a transport class for an api_mode string.
- L26 `get_transport(api_mode: str)` (function) — Get a transport instance for the given api_mode.
- L49 `_discover_transports()` (function) — Import all transport modules to trigger auto-registration.
