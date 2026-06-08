---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_list_picker_providers.py

Symbols in `tests/hermes_cli/test_list_picker_providers.py`.

- L22 `_make_provider(slug, name=None, models=None, *, is_current=False, is_user_defined=False, source='built-in', api_url=None)` (function) — Build a dict shaped like ``list_authenticated_providers`` output.
- L39 `test_openrouter_models_replaced_with_live_catalog(monkeypatch)` (function) — OpenRouter row's ``models`` should come from fetch_openrouter_models.
- L60 `test_openrouter_falls_back_to_base_models_on_fetch_failure(monkeypatch)` (function) — If the live catalog fetch raises, keep whatever base provided.
- L78 `test_openrouter_empty_live_catalog_drops_row(monkeypatch)` (function) — If the live catalog returns nothing for OpenRouter, drop the row.
- L92 `test_non_openrouter_rows_passed_through_unchanged(monkeypatch)` (function) — Non-OpenRouter providers keep their curated ``models`` as-is.
- L112 `test_empty_models_row_dropped(monkeypatch)` (function) — Built-in provider with an empty ``models`` list is dropped.
- L129 `test_custom_endpoint_with_api_url_kept_when_models_empty(monkeypatch)` (function) — User-defined endpoints with an ``api_url`` survive even if models empty.
- L153 `test_user_defined_without_api_url_and_empty_models_dropped(monkeypatch)` (function) — An is_user_defined row WITHOUT api_url and no models is still dropped.
- L173 `test_max_models_caps_openrouter_live_output(monkeypatch)` (function) — ``max_models`` caps how many OpenRouter IDs land in the row.
- L192 `test_passthrough_kwargs_to_base(monkeypatch)` (function) — All kwargs must be forwarded to ``list_authenticated_providers`` unchanged.
- L226 `test_current_custom_endpoint_passthrough_marks_current_row(monkeypatch)` (function) — Interactive picker should preserve current custom endpoint semantics.
