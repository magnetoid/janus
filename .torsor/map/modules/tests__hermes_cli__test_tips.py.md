---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tips.py

Symbols in `tests/hermes_cli/test_tips.py`.

- L6 `TestTipsCorpus` (class) — Validate the tip corpus itself.
- L9 `test_has_at_least_200_tips(self)` (method)
- L12 `test_no_duplicates(self)` (method)
- L15 `test_all_tips_are_strings(self)` (method)
- L19 `test_no_empty_tips(self)` (method)
- L23 `test_max_length_reasonable(self)` (method) — Tips should fit on a single terminal line (~120 chars max).
- L30 `test_no_leading_trailing_whitespace(self)` (method)
- L35 `TestGetRandomTip` (class) — Validate the get_random_tip() function.
- L38 `test_returns_string(self)` (method)
- L43 `test_returns_tip_from_corpus(self)` (method)
- L47 `test_randomness(self)` (method) — Multiple calls should eventually return different tips.
- L56 `TestTipIntegrationInCLI` (class) — Test that the tip display code in cli.py works correctly.
- L59 `test_tip_import_works(self)` (method) — The import used in cli.py must succeed.
- L64 `test_tip_display_format(self)` (method) — Verify the Rich markup format doesn't break.
