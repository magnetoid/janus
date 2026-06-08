---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_hooks.py

Symbols in `tests/gateway/test_hooks.py`.

- L10 `_create_hook(hooks_dir, hook_name, events, handler_code)` (function) — Helper to create a hook directory with HOOK.yaml and handler.py.
- L23 `TestHookRegistryInit` (class)
- L24 `test_empty_registry(self)` (method)
- L30 `_patch_no_builtins(reg)` (function) — Suppress built-in hook registration so tests only exercise user-hook discovery.
- L35 `TestDiscoverAndLoad` (class)
- L36 `test_loads_valid_hook(self, tmp_path)` (method)
- L48 `test_skips_missing_hook_yaml(self, tmp_path)` (method)
- L59 `test_skips_missing_handler_py(self, tmp_path)` (method)
- L70 `test_skips_no_events(self, tmp_path)` (method)
- L82 `test_skips_no_handle_function(self, tmp_path)` (method)
- L94 `test_nonexistent_hooks_dir(self, tmp_path)` (method)
- L101 `test_multiple_hooks(self, tmp_path)` (method)
- L114 `TestEmit` (class)
- L116 `test_emit_calls_sync_handler(self, tmp_path)` (method)
- L136 `test_emit_calls_async_handler(self, tmp_path)` (method)
- L162 `test_wildcard_matching(self, tmp_path)` (method)
- L181 `test_no_handlers_for_event(self, tmp_path)` (method)
- L189 `test_handler_error_does_not_propagate(self, tmp_path)` (method)
- L204 `test_emit_default_context(self, tmp_path)` (method)
- L223 `TestEmitCollect` (class) — Tests for emit_collect() — returns handler return values for decision-style hooks.
- L227 `test_collects_sync_return_values(self)` (method)
- L242 `test_collects_async_return_values(self)` (method)
- L255 `test_drops_none_return_values(self)` (method)
- L268 `test_handler_exception_does_not_abort_chain(self)` (method)
- L285 `test_wildcard_match_also_collected(self)` (method)
- L296 `test_no_handlers_returns_empty_list(self)` (method)
- L304 `test_default_context(self)` (method)
