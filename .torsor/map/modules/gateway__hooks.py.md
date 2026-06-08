---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/hooks.py

Symbols in `gateway/hooks.py`.

- L35 `HookRegistry` (class) — Discovers, loads, and fires event hooks.
- L45 `__init__(self)` (method)
- L51 `loaded_hooks(self)` (method) — Return metadata about all loaded hooks.
- L55 `_register_builtin_hooks(self)` (method) — Register built-in hooks that are always active.
- L64 `discover_and_load(self)` (method) — Scan the hooks directory for hook directories and load their handlers.
- L145 `_resolve_handlers(self, event_type: str)` (method) — Return all handlers that should fire for ``event_type``.
- L158 `emit(self, event_type: str, context: Optional[Dict[str, Any]]=None)` (method) — Fire all handlers registered for an event, discarding return values.
- L183 `emit_collect(self, event_type: str, context: Optional[Dict[str, Any]]=None)` (method) — Fire handlers and return their non-None return values in order.
