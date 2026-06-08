---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_clear_stale_base_url.py

Symbols in `tests/hermes_cli/test_clear_stale_base_url.py`.

- L9 `_write_provider(provider: str, model: str='test-model')` (function) — Helper: write a provider + model to config.yaml.
- L21 `TestClearStaleOpenaiBaseUrl` (class) — _clear_stale_openai_base_url() removes OPENAI_BASE_URL when provider is not custom.
- L24 `test_clears_when_provider_is_named(self, monkeypatch)` (method) — OPENAI_BASE_URL is cleared when config provider is a named provider.
- L36 `test_preserves_when_provider_is_custom(self, monkeypatch)` (method) — OPENAI_BASE_URL is NOT cleared when config provider is 'custom'.
- L49 `test_noop_when_no_openai_base_url(self, monkeypatch)` (method) — No error when OPENAI_BASE_URL is not set.
- L61 `test_noop_when_provider_empty(self, monkeypatch)` (method) — No cleanup when provider is not set in config.
