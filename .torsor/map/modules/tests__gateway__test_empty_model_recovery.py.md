---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_empty_model_recovery.py

Symbols in `tests/gateway/test_empty_model_recovery.py`.

- L21 `_make_runner()` (function)
- L31 `_patch_resolution(monkeypatch, *, model_from_config: str, provider: str='openrouter')` (function) — Stub gateway model + runtime resolution to a known state.
- L46 `test_normal_turn_caches_last_resolved_model(monkeypatch)` (function)
- L59 `test_empty_model_recovers_session_last_good(monkeypatch)` (function)
- L74 `test_empty_model_new_session_recovers_global_last_good(monkeypatch)` (function)
- L88 `test_cold_start_empty_model_does_not_crash(monkeypatch)` (function) — No last-good anywhere + empty config → returns '' gracefully (no exception).
- L98 `test_bare_runner_without_cache_attr_does_not_crash(monkeypatch)` (function) — object.__new__ runners (test helpers / pitfall #17) lack _last_resolved_model.
- L117 `_bare_agent()` (function)
- L123 `test_has_pending_fallback_empty_chain()` (function)
- L130 `test_has_pending_fallback_with_chain()` (function)
- L137 `test_has_pending_fallback_exhausted_chain()` (function)
- L144 `test_has_pending_fallback_missing_attrs()` (function) — Bare agent with no fallback attributes set must default to False, not crash.
