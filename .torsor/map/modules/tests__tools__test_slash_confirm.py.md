---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_slash_confirm.py

Symbols in `tests/tools/test_slash_confirm.py`.

- L16 `_clean_pending()` (function) — Every test gets a clean primitive state.
- L23 `TestRegisterAndGetPending` (class)
- L24 `test_register_stores_entry(self)` (method)
- L37 `test_get_pending_missing_returns_none(self)` (method)
- L40 `test_register_supersedes_prior_entry(self)` (method)
- L54 `test_get_pending_returns_copy_not_reference(self)` (method)
- L67 `TestResolve` (class)
- L69 `test_resolve_runs_handler_and_pops_entry(self)` (method)
- L86 `test_resolve_no_pending_returns_none(self)` (method)
- L91 `test_resolve_confirm_id_mismatch_returns_none(self)` (method)
- L104 `test_resolve_stale_entry_returns_none(self)` (method)
- L116 `test_resolve_handler_exception_returns_error_string(self)` (method)
- L129 `test_resolve_non_string_return_becomes_none(self)` (method)
- L138 `test_resolve_double_click_only_runs_handler_once(self)` (method)
- L157 `TestClear` (class)
- L158 `test_clear_removes_entry(self)` (method)
- L168 `test_clear_missing_is_noop(self)` (method)
- L173 `TestClearIfStale` (class)
- L174 `test_clears_stale_entry(self)` (method)
- L185 `test_preserves_fresh_entry(self)` (method)
- L195 `test_returns_false_for_missing_entry(self)` (method)
