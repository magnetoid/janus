---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_max_tokens_propagation.py

Symbols in `tests/gateway/test_max_tokens_propagation.py`.

- L22 `isolated_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with a writable config.yaml and a clean module cache.
- L61 `test_top_level_max_tokens_propagates(isolated_home)` (function) — model.max_tokens is read into the gateway runtime kwargs (#20741).
- L77 `test_per_provider_max_output_tokens_fallback(isolated_home)` (function) — A custom provider's max_output_tokens fills in when no global is set.
- L98 `test_global_max_tokens_beats_per_provider(isolated_home)` (function) — The documented global model.max_tokens wins over a provider cap.
- L120 `test_env_override_beats_everything(isolated_home, monkeypatch)` (function) — HERMES_MAX_TOKENS is the internal override mechanism (highest priority).
- L143 `test_no_config_leaves_max_tokens_none(isolated_home)` (function) — No cap configured anywhere -> max_tokens is None (no spurious limit).
- L158 `test_lift_helper_accepts_alias_and_rejects_garbage(isolated_home)` (function) — _lift_max_output_tokens accepts both keys, ignores non-positive/non-int.
