---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_set_runtime_main_custom_provider.py

Symbols in `tests/agent/test_set_runtime_main_custom_provider.py`.

- L10 `_get_globals(mod)` (function) — Read runtime globals without triggering redaction.
- L21 `TestSetRuntimeMainCustomProvider` (class) — set_runtime_main must propagate base_url/api_key/api_mode for custom providers.
- L24 `test_globals_stored(self)` (method) — set_runtime_main stores all five fields in process-local globals.
- L46 `test_clear_resets_all_globals(self)` (method) — clear_runtime_main resets all five globals to empty.
- L61 `test_resolve_auto_uses_globals_for_custom_provider(self)` (method) — _resolve_auto reads base_url/api_key from globals when main_runtime is None.
- L86 `test_explicit_main_runtime_takes_precedence(self)` (method) — When main_runtime dict has values, globals are NOT used.
- L115 `test_backward_compatible_defaults(self)` (method) — Calling set_runtime_main with only positional args still works.
- L132 `TestResolveAutoCustomEndToEnd` (class) — End-to-end routing assertions — build a *real* client (no mock on
- L141 `_client_base_url(client)` (method)
- L152 `test_config_less_custom_endpoint_routes_via_global(self, tmp_path, monkeypatch)` (method) — custom:<name> with NO config entry: the live base_url carried by
- L191 `test_named_custom_with_config_entry_still_routes(self, tmp_path, monkeypatch)` (method) — Regression guard: custom:<name> WITH a custom_providers entry must
