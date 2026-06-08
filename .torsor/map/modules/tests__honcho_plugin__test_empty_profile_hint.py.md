---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/honcho_plugin/test_empty_profile_hint.py

Symbols in `tests/honcho_plugin/test_empty_profile_hint.py`.

- L11 `_make_provider(**cfg_overrides)` (function)
- L33 `TestEmptyProfileHint` (class)
- L34 `test_returns_hint_not_bare_error_message(self)` (method)
- L42 `test_hint_mentions_warmup_when_turn_count_below_cadence(self)` (method)
- L49 `test_hint_mentions_observation_when_fully_disabled_for_user(self)` (method)
- L55 `test_hint_mentions_observation_when_fully_disabled_for_ai(self)` (method)
- L62 `test_hint_falls_back_to_generic_reason_when_no_specific_cause(self)` (method) — Mature session with observation on + enough turns = generic hint.
- L71 `test_hint_suggests_alternative_tools(self)` (method)
- L78 `test_populated_card_returns_card_without_hint(self)` (method) — Regression: a populated card should NOT trigger the hint path.
