---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_context_engine.py

Symbols in `tests/agent/test_context_engine.py`.

- L15 `StubEngine` (class) — Minimal engine that satisfies the ABC without doing real work.
- L18 `__init__(self, context_length=200000, threshold_pct=0.5)` (method)
- L25 `name(self)` (method)
- L28 `update_from_response(self, usage: Dict[str, Any])` (method)
- L33 `should_compress(self, prompt_tokens: int=None)` (method)
- L37 `compress(self, messages: List[Dict[str, Any]], current_tokens: int=None)` (method)
- L43 `get_tool_schemas(self)` (method)
- L52 `handle_tool_call(self, name: str, args: Dict[str, Any])` (method)
- L61 `TestContextEngineABC` (class) — Verify the ABC enforces the required interface.
- L64 `test_cannot_instantiate_abc_directly(self)` (method)
- L68 `test_missing_methods_raises(self)` (method) — A subclass missing required methods cannot be instantiated.
- L77 `test_stub_engine_satisfies_abc(self)` (method)
- L82 `test_compressor_is_context_engine(self)` (method)
- L92 `TestDefaults` (class) — Verify ABC default implementations work correctly.
- L95 `test_default_tool_schemas_empty(self)` (method)
- L100 `test_default_handle_tool_call_returns_error(self)` (method)
- L106 `test_default_get_status(self)` (method)
- L115 `test_on_session_reset(self)` (method)
- L123 `test_should_compress_preflight_default_false(self)` (method)
- L132 `TestStubEngine` (class)
- L134 `test_should_compress(self)` (method)
- L140 `test_compress_tracks_count(self)` (method)
- L148 `test_tool_schemas(self)` (method)
- L154 `test_handle_tool_call(self)` (method)
- L160 `test_update_from_response(self)` (method)
- L171 `TestCompressorSessionReset` (class) — Verify ContextCompressor.on_session_reset() clears all state.
- L174 `test_reset_clears_state(self)` (method)
- L197 `TestPluginContextEngineSlot` (class) — Test register_context_engine on PluginContext.
- L200 `test_register_engine(self)` (method)
- L212 `test_reject_second_engine(self)` (method)
- L225 `test_reject_non_engine(self)` (method)
- L234 `test_get_plugin_context_engine(self)` (method)
