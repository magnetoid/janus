---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_models_dev_preferred_merge.py

Symbols in `tests/hermes_cli/test_models_dev_preferred_merge.py`.

- L30 `TestMergeHelper` (class)
- L31 `test_merge_empty_mdev_returns_curated(self)` (method) — When models.dev returns nothing, curated list is preserved verbatim.
- L37 `test_merge_mdev_raises_returns_curated(self)` (method) — Offline / broken models.dev must not break the catalog path.
- L46 `test_merge_mdev_first_then_curated_extras(self)` (method) — models.dev entries come first; curated-only entries are appended.
- L55 `test_merge_case_insensitive_dedup(self)` (method) — Dedup is case-insensitive but preserves the first occurrence's casing.
- L65 `TestProviderModelIdsPreferred` (class)
- L66 `test_opencode_go_is_preferred(self)` (method)
- L69 `test_opencode_go_includes_fresh_models_dev_entries(self)` (method) — provider_model_ids('opencode-go') adds models.dev entries on top.
- L82 `test_opencode_go_offline_falls_back_to_curated(self)` (method) — Offline models.dev → curated-only list, no crash.
- L90 `test_opencode_zen_includes_fresh_models(self)` (method) — opencode-zen follows the same pattern as opencode-go.
- L100 `TestOpenRouterAndNousUnchanged` (class) — Per Teknium: openrouter and nous are NEVER merged with models.dev.
- L103 `test_openrouter_not_in_preferred_set(self)` (method)
- L106 `test_nous_not_in_preferred_set(self)` (method)
- L109 `test_openrouter_does_not_call_merge(self)` (method) — openrouter takes its own live path — merge helper must NOT run.
