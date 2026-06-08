---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_opencode_go_validation_fallback.py

Symbols in `tests/hermes_cli/test_opencode_go_validation_fallback.py`.

- L29 `_patched(func)` (function) — Decorator: force fetch_api_models / probe_api_models to simulate an
- L46 `test_opencode_go_known_model_accepted()` (function) — A model present in the opencode-go curated catalog must be accepted
- L57 `test_opencode_go_known_model_case_insensitive()` (function) — Catalog lookup is case-insensitive.
- L65 `test_opencode_go_typo_auto_corrected()` (function) — A close typo (>= 0.9 similarity) is auto-corrected to the catalog
- L76 `test_opencode_go_unknown_model_accepted_with_suggestion()` (function) — An unknown model that has a medium-similarity match (>= 0.5 but < 0.9)
- L91 `test_opencode_go_totally_unknown_model_still_accepted()` (function) — A model with zero similarity to the catalog is still accepted (no
- L110 `test_opencode_zen_known_model_accepted()` (function) — opencode-zen also uses _PROVIDER_MODELS; kimi-k2 is in its catalog.
- L123 `test_provider_without_catalog_accepts_with_warning()` (function) — When a provider has no entry in _PROVIDER_MODELS and /models is
