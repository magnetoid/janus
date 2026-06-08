---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gemini_free_tier_setup_block.py

Symbols in `tests/hermes_cli/test_gemini_free_tier_setup_block.py`.

- L10 `config_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with an empty config.
- L30 `TestGeminiSetupFreeTierBlock` (class) — _model_flow_api_key_provider should refuse to wire up a free-tier Gemini key.
- L33 `test_free_tier_key_is_blocked(self, config_home, monkeypatch, capsys)` (method) — Free-tier probe result -> provider is NOT saved, message is printed.
- L67 `test_paid_tier_key_proceeds(self, config_home, monkeypatch, capsys)` (method) — Paid-tier probe result -> provider IS saved normally.
- L96 `test_unknown_tier_proceeds_with_warning(self, config_home, monkeypatch, capsys)` (method) — Probe returning 'unknown' (network/auth error) -> proceed without blocking.
- L124 `test_non_gemini_provider_skips_probe(self, config_home, monkeypatch)` (method) — Probe must only run for provider_id == 'gemini', not for other providers.
