---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_caption_merge.py

Symbols in `tests/gateway/test_telegram_caption_merge.py`.

- L9 `TestMergeCaptionBasic` (class)
- L10 `test_no_existing_text(self)` (method)
- L13 `test_empty_existing_text(self)` (method)
- L16 `test_exact_duplicate_dropped(self)` (method)
- L19 `test_different_captions_merged(self)` (method)
- L24 `TestMergeCaptionSubstringBug` (class) — These are the exact scenarios that the old substring check got wrong.
- L27 `test_shorter_caption_not_dropped_when_substring(self)` (method)
- L32 `test_longer_caption_not_dropped_when_contains_existing(self)` (method)
- L37 `test_prefix_caption_not_dropped(self)` (method)
- L42 `TestMergeCaptionWhitespace` (class)
- L43 `test_trailing_space_treated_as_duplicate(self)` (method)
- L46 `test_leading_space_treated_as_duplicate(self)` (method)
- L49 `test_whitespace_only_new_text_not_added(self)` (method)
- L58 `TestMergeCaptionMultipleItems` (class)
- L59 `test_three_unique_captions_all_present(self)` (method)
- L65 `test_duplicate_in_middle_dropped(self)` (method)
- L71 `test_album_scenario_revenue_profit(self)` (method)
