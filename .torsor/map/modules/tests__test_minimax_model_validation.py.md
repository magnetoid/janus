---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_minimax_model_validation.py

Symbols in `tests/test_minimax_model_validation.py`.

- L14 `TestMiniMaxModelValidation` (class) — Test that validate_requested_model handles MiniMax providers correctly.
- L18 `_isolate_minimax(self)` (method) — Ensure MiniMax catalog is used even if a live /v1/models endpoint exists.
- L36 `test_valid_minimax_model_accepted(self)` (method)
- L46 `test_valid_minimax_model_case_insensitive(self)` (method)
- L53 `test_valid_minimax_model_uppercase(self)` (method)
- L61 `test_near_match_minimax_cn_suggests_similar(self)` (method)
- L77 `test_unknown_minimax_model_accepted_with_warning(self)` (method)
- L92 `test_minimax_uses_catalog_not_api_probe(self)` (method) — Ensure that when fetch_api_models returns None, the catalog is still checked.
- L102 `TestMiniMaxCatalogPathRequired` (class) — Prove the catalog path is necessary: without it, MiniMax would fail.
- L110 `test_minimax_without_fix_would_reach_api_probe(self)` (method) — Without the catalog block, minimax falls through to fetch_api_models.
