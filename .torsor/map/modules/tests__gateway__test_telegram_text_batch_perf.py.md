---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_text_batch_perf.py

Symbols in `tests/gateway/test_telegram_text_batch_perf.py`.

- L23 `adapter()` (function) — Build a TelegramAdapter shell without going through __init__'s
- L30 `TestEnvFloatClamped` (class) — _env_float_clamped is the fence around every float env var the
- L34 `test_default_when_unset(self, monkeypatch)` (method)
- L38 `test_parses_valid_value(self, monkeypatch)` (method)
- L42 `test_falls_back_to_default_on_garbage(self, monkeypatch)` (method)
- L46 `test_rejects_nan(self, monkeypatch)` (method)
- L52 `test_rejects_inf(self, monkeypatch)` (method)
- L58 `test_clamps_below_min(self, monkeypatch)` (method)
- L64 `test_clamps_above_max(self, monkeypatch)` (method)
- L71 `TestAdaptiveTextBatchTiers` (class) — The fast-path tiers cap delay for short / medium messages.  Tier
- L76 `test_class_constants_are_sensible(self)` (method) — Sanity check that the tier constants form a non-overlapping
- L84 `test_fast_tier_uses_min_with_configured_cap(self, adapter)` (method) — A short message picks the lower of the fast-tier delay and
- L103 `test_short_tier_uses_min_with_configured_cap(self, adapter)` (method) — Same composition rule for the medium tier.
- L112 `test_long_message_uses_full_cap(self, adapter)` (method) — Messages above the medium threshold use the configured cap
- L120 `test_split_threshold_takes_priority_over_fast_tier(self, adapter)` (method) — If the latest chunk hits the platform split threshold a
