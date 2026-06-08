---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_memory_provider_init.py

Symbols in `tests/run_agent/test_memory_provider_init.py`.

- L7 `RecordingMemoryProvider` (class)
- L10 `__init__(self)` (method)
- L14 `is_available(self)` (method)
- L17 `initialize(self, session_id, **kwargs)` (method)
- L21 `get_tool_schemas(self)` (method)
- L24 `shutdown(self)` (method)
- L28 `test_blank_memory_provider_does_not_auto_enable_honcho()` (function) — Blank memory.provider should remain opt-out even if Honcho fallback looks configured.
- L62 `test_aiagent_forwards_user_id_alt_to_memory_provider()` (function)
- L95 `CoreShadowProvider` (class) — Provider that tries to register tools shadowing built-in core tools.
- L100 `get_tool_schemas(self)` (method)
- L108 `test_core_tool_names_rejected_from_memory_routing_table()` (function) — Memory tools shadowing core tool names are rejected at registration (#40466).
