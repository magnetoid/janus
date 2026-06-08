---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_model_command_flat_string_config.py

Symbols in `tests/gateway/test_model_command_flat_string_config.py`.

- L23 `_make_runner()` (function)
- L32 `_make_event(text)` (function)
- L40 `_fake_switch_result()` (function) — Build a successful ModelSwitchResult that bypasses real provider resolution.
- L57 `_setup_isolated_home(tmp_path, monkeypatch, model_yaml_value)` (function) — Write a config.yaml with the given ``model:`` value and stub the heavy bits.
- L82 `test_model_global_persists_when_config_has_flat_string_model(tmp_path, monkeypatch)` (function) — Regression: ``model: deepseek-v4-flash`` (flat string) used to crash
- L109 `test_model_global_persists_when_config_has_missing_model(tmp_path, monkeypatch)` (function) — Companion case: ``model:`` key absent entirely. setdefault would have
- L141 `test_model_global_persists_when_config_has_proper_dict_model(tmp_path, monkeypatch)` (function) — Already-correct nested dict must still work — no regression on the
