---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_empty_model_fallback.py

Symbols in `tests/test_empty_model_fallback.py`.

- L6 `TestGetDefaultModelForProvider` (class) — Unit tests for hermes_cli.models.get_default_model_for_provider.
- L9 `test_known_provider_returns_first_model(self)` (method)
- L16 `test_openrouter_returns_empty(self)` (method) — OpenRouter uses dynamic model fetch, no static catalog entry.
- L23 `test_unknown_provider_returns_empty(self)` (method)
- L27 `test_custom_provider_returns_empty(self)` (method) — Custom provider has no model catalog — should return empty.
- L33 `test_nous_silent_default_is_not_the_expensive_flagship(self)` (method) — Nous Portal is a metered aggregator whose curated list is ordered
- L58 `test_override_falls_back_to_catalog_when_missing(self)` (method) — If an override model is no longer in the catalog, fall back to [0]
- L74 `TestGatewayEmptyModelFallback` (class) — Test that _resolve_session_agent_runtime fills in empty model from provider catalog.
- L77 `test_empty_model_filled_from_provider(self)` (method) — When config has no model but provider is openai-codex, use first codex model.
- L100 `test_nonempty_model_not_overridden(self)` (method) — When config has a model set, don't override it.
- L118 `test_empty_model_no_provider_stays_empty(self)` (method) — When both model and provider are empty, model stays empty.
- L138 `TestResolveGatewayModel` (class) — Test _resolve_gateway_model reads model from config correctly.
- L141 `test_returns_default_key(self)` (method)
- L145 `test_returns_model_key_fallback(self)` (method)
- L149 `test_returns_empty_when_missing(self)` (method)
- L153 `test_returns_empty_when_no_model_section(self)` (method)
- L157 `test_string_model_config(self)` (method)
