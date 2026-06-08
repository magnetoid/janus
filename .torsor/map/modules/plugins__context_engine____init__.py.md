---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/context_engine/__init__.py

Symbols in `plugins/context_engine/__init__.py`.

- L33 `discover_context_engines()` (function) — Scan plugins/context_engine/ for available engines.
- L79 `load_context_engine(name: str)` (function) — Load and return a ContextEngine instance by name.
- L100 `_load_engine_from_dir(engine_dir: Path)` (function) — Import an engine module and extract the ContextEngine instance.
- L199 `_EngineCollector` (class) — Fake plugin context that captures register_context_engine calls.
- L208 `__init__(self, engine_name: str='')` (method)
- L213 `register_context_engine(self, engine)` (method)
- L216 `register_command(self, name: str, handler, description: str='', args_hint: str='')` (method) — Forward to the global plugin command registry.
- L275 `register_tool(self, *args, **kwargs)` (method)
- L278 `register_hook(self, *args, **kwargs)` (method)
- L281 `register_cli_command(self, *args, **kwargs)` (method)
- L284 `register_memory_provider(self, *args, **kwargs)` (method)
