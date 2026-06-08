---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_vision_routing_31179.py

Symbols in `tests/agent/test_vision_routing_31179.py`.

- L42 `isolated_home(monkeypatch)` (function) — Temp HERMES_HOME with config + clean credential env vars.
- L58 `_write_config(home: str, text: str)` (function)
- L63 `_fresh_modules()` (function) — Drop cached hermes modules so each test reloads against current env.
- L77 `TestOpenAiAliasForAuxiliary` (class) — ``auxiliary.<task>.provider: openai`` should produce a working client.
- L80 `test_provider_openai_routes_to_openai_dot_com(self, isolated_home, monkeypatch)` (method)
- L96 `test_provider_openai_with_explicit_base_url_preserves_user_endpoint(self, isolated_home, monkeypatch)` (method) — User-supplied base_url wins; alias still normalizes provider name
- L116 `test_provider_openai_resolves_to_working_client(self, isolated_home, monkeypatch)` (method) — End-to-end: the resolved client points at api.openai.com.
- L143 `TestTextOnlyMainSkippedForVision` (class) — Vision auto-detect must not return a text-only main-provider client.
- L146 `test_text_only_main_skipped_when_no_aggregator(self, isolated_home, monkeypatch)` (method) — DeepSeek main + no aggregator credentials → no client built.
- L168 `test_vision_capable_main_used(self, isolated_home, monkeypatch)` (method) — Vision-capable main provider should be returned by auto chain.
- L183 `test_unknown_capability_does_not_block(self, isolated_home, monkeypatch)` (method) — When models.dev has no entry, fall back to permissive (attempt the call).
- L200 `TestVisionToolGating` (class) — Tool visibility must match runtime capability.
- L203 `test_check_vision_succeeds_for_aliased_openai(self, isolated_home, monkeypatch)` (method) — The user's exact reported scenario: provider=openai unhides
- L218 `test_check_vision_falls_back_to_auto(self, isolated_home, monkeypatch)` (method) — Bad explicit provider doesn't hide the tool when auto fallback works.
- L237 `test_check_vision_false_with_text_only_main_and_no_aggregator(self, isolated_home, monkeypatch)` (method)
- L251 `test_browser_vision_requires_both_browser_and_vision(self, isolated_home, monkeypatch)` (method) — ``browser_vision`` must not be advertised when vision is unavailable.
- L268 `test_browser_vision_false_when_browser_missing(self, isolated_home, monkeypatch)` (method)
- L284 `test_browser_vision_true_when_both_available(self, isolated_home, monkeypatch)` (method)
