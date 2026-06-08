---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_compress_plugin_engine.py

Symbols in `tests/gateway/test_compress_plugin_engine.py`.

- L29 `_FakePluginEngine` (class) — Minimal ContextEngine that only implements the ABC — no private helpers.
- L38 `name(self)` (method)
- L41 `update_from_response(self, usage: Dict[str, Any])` (method)
- L44 `should_compress(self, prompt_tokens: int=None)` (method)
- L47 `compress(self, messages: List[Dict[str, Any]], current_tokens: int=None, focus_topic: str=None)` (method)
- L60 `_make_source()` (function)
- L70 `_make_event(text: str='/compress')` (function)
- L74 `_make_history()` (function)
- L83 `_make_runner(history: list[dict[str, str]])` (function)
- L108 `test_compress_works_with_plugin_context_engine()` (function) — /compress must not call ContextCompressor-only private helpers.
- L147 `test_compress_respects_plugin_has_content_to_compress_false()` (function) — If a plugin reports no compressible content, gateway skips the LLM call.
