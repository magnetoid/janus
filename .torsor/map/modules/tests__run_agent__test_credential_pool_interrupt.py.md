---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_credential_pool_interrupt.py

Symbols in `tests/run_agent/test_credential_pool_interrupt.py`.

- L12 `_make_entry(idx, **overrides)` (function)
- L26 `_make_pool(entries)` (function)
- L33 `test_rotate_immediately_when_credential_already_exhausted()` (function) — If current credential has last_status='exhausted', rotate on first 429
- L58 `test_normal_retry_when_credential_not_exhausted()` (function) — When credential is active, first 429 should still retry (existing behavior).
- L79 `test_rotate_on_second_429_when_not_exhausted()` (function) — When credential is active and this is the second 429, rotate (existing behavior).
