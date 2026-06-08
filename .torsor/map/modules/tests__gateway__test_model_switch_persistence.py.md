---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_model_switch_persistence.py

Symbols in `tests/gateway/test_model_switch_persistence.py`.

- L28 `_make_source()` (function)
- L38 `_make_runner()` (function) — Create a minimal GatewayRunner with stubbed internals.
- L82 `TestApplySessionModelOverride` (class) — Verify _apply_session_model_override replaces config defaults.
- L85 `test_override_replaces_all_fields(self)` (method)
- L109 `test_no_override_returns_originals(self)` (method)
- L121 `test_none_values_do_not_overwrite(self)` (method) — Override with None api_key/base_url should preserve config defaults.
- L146 `test_empty_string_overwrites(self)` (method) — Empty string is not None — it should overwrite the config value.
- L167 `test_different_session_key_not_affected(self)` (method)
- L194 `TestIsIntentionalModelSwitch` (class) — Verify fallback detection respects intentional /model overrides.
- L197 `test_matches_override(self)` (method)
- L211 `test_no_override_returns_false(self)` (method)
- L217 `test_different_model_returns_false(self)` (method) — Agent fell back to a different model than the override.
- L232 `test_wrong_session_key(self)` (method)
