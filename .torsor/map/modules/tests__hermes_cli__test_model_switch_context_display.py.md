---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_switch_context_display.py

Symbols in `tests/hermes_cli/test_model_switch_context_display.py`.

- L20 `_FakeModelInfo` (class)
- L21 `__init__(self, ctx)` (method)
- L25 `TestResolveDisplayContextLength` (class)
- L26 `test_codex_oauth_overrides_models_dev(self)` (method) — gpt-5.5 on openai-codex must show Codex's 272K cap, not models.dev's 1.05M.
- L44 `test_falls_back_to_model_info_when_resolver_returns_none(self)` (method)
- L56 `test_returns_none_when_both_sources_empty(self)` (method)
- L67 `test_resolver_exception_falls_back_to_model_info(self)` (method)
- L78 `test_prefers_resolver_even_when_model_info_has_larger_value(self)` (method) — Invariant: provider-aware resolver is authoritative, even if models.dev
- L92 `test_custom_providers_override_honored(self)` (method) — Regression for #15779: /model switch onto a custom provider must
- L125 `test_custom_providers_trailing_slash_insensitive(self)` (method) — Base URL comparison must tolerate trailing-slash differences
