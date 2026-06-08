---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_copilot_context.py

Symbols in `tests/hermes_cli/test_copilot_context.py`.

- L51 `_clear_cache()` (function) — Reset module-level cache before each test.
- L62 `TestGetCopilotModelContext` (class) — Tests for get_copilot_model_context().
- L66 `test_returns_max_prompt_tokens(self, mock_fetch)` (method)
- L71 `test_returns_none_for_unknown_model(self, mock_fetch)` (method)
- L75 `test_skips_models_without_limits(self, mock_fetch)` (method)
- L79 `test_skips_zero_limit(self, mock_fetch)` (method)
- L83 `test_caches_results(self, mock_fetch)` (method)
- L90 `test_cache_expires(self, mock_fetch)` (method)
- L102 `test_returns_none_when_catalog_unavailable(self, mock_fetch)` (method)
- L106 `test_returns_none_for_empty_catalog(self, mock_fetch)` (method)
- L110 `TestModelMetadataCopilotIntegration` (class) — Test that get_model_context_length() uses Copilot live API for copilot provider.
- L114 `test_copilot_provider_uses_live_api(self, mock_fetch)` (method)
- L121 `test_copilot_acp_provider_uses_live_api(self, mock_fetch)` (method)
- L128 `test_falls_through_when_catalog_unavailable(self, mock_fetch)` (method)
