---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_insights_unicode_flags.py

Symbols in `tests/gateway/test_insights_unicode_flags.py`.

- L14 `_normalize_insights_args(raw: str)` (function) — Apply the same normalization as the /insights handler.
- L19 `TestInsightsUnicodeDashFlags` (class) — --days and --source must survive iOS Unicode dash conversion.
- L39 `test_unicode_dash_normalized(self, input_str, expected)` (method)
- L43 `test_regular_hyphens_unaffected(self)` (method) — Normal --days/--source must pass through unchanged.
- L47 `test_bare_number_still_works(self)` (method) — Shorthand /insights 7 (no flag) must not be mangled.
- L51 `test_no_flags_unchanged(self)` (method) — Input with no flags passes through as-is.
