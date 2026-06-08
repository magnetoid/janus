---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_vision_memory_leak.py

Symbols in `tests/gateway/test_vision_memory_leak.py`.

- L20 `gateway_runner()` (function) — Minimal GatewayRunner stub with just the method under test bound.
- L30 `_run(coro)` (function)
- L34 `TestEnrichMessageWithVision` (class)
- L35 `test_clean_description_passes_through(self, gateway_runner)` (method) — Vision output without leaked memory is embedded unchanged.
- L45 `test_memory_context_fence_stripped(self, gateway_runner)` (method) — <memory-context>...</memory-context> fenced block is scrubbed.
- L63 `test_fenced_leak_stripped_plugin_header_preserved(self, gateway_runner)` (method) — The fenced wrapper is stripped; plugin-specific text outside the
