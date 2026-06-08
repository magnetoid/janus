---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_inventory_pricing.py

Symbols in `tests/hermes_cli/test_inventory_pricing.py`.

- L12 `_patch_pricing(monkeypatch, *, free_tier, pricing, unavailable=None)` (function)
- L24 `test_apply_pricing_formats_per_model_prices(monkeypatch)` (function) — Each model gets formatted input/output/cache + a free flag.
- L45 `test_apply_pricing_nous_free_tier_gates_paid_models(monkeypatch)` (function) — A free-tier Nous account marks paid models unavailable and sets the flag.
- L66 `test_apply_pricing_nous_paid_tier_no_gating(monkeypatch)` (function) — A paid Nous account gates nothing.
- L80 `test_apply_pricing_skips_providers_without_pricing(monkeypatch)` (function) — A provider with no live pricing simply gets no pricing key.
- L89 `test_apply_pricing_failure_is_swallowed(monkeypatch)` (function) — A pricing fetch that raises must not break the whole payload.
