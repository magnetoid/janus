---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/model_providers/test_minimax_profile.py

Symbols in `tests/plugins/model_providers/test_minimax_profile.py`.

- L27 `minimax_profile(request)` (function) — Resolve each registered MiniMax profile.
- L42 `TestMinimaxAuxModelM3` (class) — MiniMax profile aux model is the new frontier M3, not the stale M2.7.
- L69 `test_profile_advertises_expected_aux_model(self, provider_id, expected)` (method)
- L82 `test_consumer_api_returns_non_empty_for_each_provider(self, minimax_profile)` (method)
- L100 `TestMinimaxAuxModelNotHighspeed` (class) — Regression guard against re-introducing the M2.7-highspeed aux default.
- L110 `test_default_aux_model_is_not_highspeed(self, provider_id)` (method)
