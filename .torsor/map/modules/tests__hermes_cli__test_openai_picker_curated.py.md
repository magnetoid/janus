---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_openai_picker_curated.py

Symbols in `tests/hermes_cli/test_openai_picker_curated.py`.

- L32 `test_openrouter_overlay_does_not_list_openai_api_key()` (function)
- L39 `test_default_openai_endpoint_filters_to_curated(monkeypatch)` (function) — The 126-model /v1/models dump is intersected with the curated list.
- L59 `test_default_openai_endpoint_intersects_account_access(monkeypatch)` (function) — Curated models the account can't access are dropped (intersection).
- L73 `test_default_openai_endpoint_falls_back_when_no_curated_access(monkeypatch)` (function) — If the account serves none of the curated models, fall back to curated.
- L87 `test_custom_openai_compatible_endpoint_keeps_live_list(monkeypatch)` (function) — Custom OPENAI_BASE_URL endpoints keep the live catalog verbatim.
