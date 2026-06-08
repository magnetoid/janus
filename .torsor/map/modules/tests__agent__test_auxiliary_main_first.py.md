---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_main_first.py

Symbols in `tests/agent/test_auxiliary_main_first.py`.

- L23 `TestResolveAutoMainFirst` (class) — _resolve_auto() must prefer main provider + main model for every user.
- L26 `test_openrouter_main_uses_main_model_for_aux(self, monkeypatch)` (method) — OpenRouter main user → aux uses their picked OR model, not Gemini Flash.
- L54 `test_nous_main_uses_main_model_for_aux(self, monkeypatch)` (method) — Nous Portal main user → aux uses their picked Nous model, not free-tier MiMo.
- L76 `test_non_aggregator_main_still_uses_main(self, monkeypatch)` (method) — Non-aggregator main (DeepSeek) → unchanged behavior, main model used.
- L98 `test_main_unavailable_falls_through_to_chain(self, monkeypatch)` (method) — Main provider with no working client → fall back to aux chain.
- L121 `test_no_main_config_uses_chain_directly(self)` (method) — No main provider configured → skip step 1, use chain (no regression).
- L138 `test_runtime_override_wins_over_config(self, monkeypatch)` (method) — main_runtime kwarg overrides config-read main provider/model.
- L168 `TestResolveVisionMainFirst` (class) — Vision auto-detection prefers the main provider first.
- L171 `test_openrouter_main_vision_uses_main_model(self, monkeypatch)` (method) — OpenRouter main with vision-capable model → aux vision uses main model.
- L203 `test_nous_main_vision_uses_paid_nous_vision_backend(self)` (method) — Paid Nous main → aux vision uses the dedicated Nous vision backend.
- L225 `test_nous_main_vision_uses_free_tier_nous_vision_backend(self)` (method) — Free-tier Nous main → aux vision uses MiMo omni, not the text main model.
- L247 `test_exotic_provider_with_vision_override_preserved(self)` (method) — xiaomi → mimo-v2.5 override still wins over main_model.
- L271 `test_copilot_vision_sets_vision_header(self, monkeypatch)` (method) — Copilot vision requests include the header required for vision routing.
- L315 `test_text_copilot_does_not_set_vision_header(self, monkeypatch)` (method) — Text Copilot requests keep the vision-only header off.
- L351 `test_main_unavailable_vision_falls_through_to_aggregators(self)` (method) — Main provider fails → fall back to OpenRouter/Nous strict backends.
- L375 `test_explicit_provider_override_still_wins(self)` (method) — Explicit config override bypasses main-first policy.
- L402 `test_aggregator_providers_constant_removed()` (function) — The dead _AGGREGATOR_PROVIDERS constant should no longer live in the module.
