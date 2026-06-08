---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_video_gen_registry.py

Symbols in `tests/agent/test_video_gen_registry.py`.

- L11 `_FakeProvider` (class)
- L12 `__init__(self, name: str, available: bool=True)` (method)
- L17 `name(self)` (method)
- L20 `is_available(self)` (method)
- L23 `generate(self, prompt, **kw)` (method)
- L28 `_reset_registry()` (function)
- L34 `TestRegisterProvider` (class)
- L35 `test_register_and_lookup(self)` (method)
- L40 `test_rejects_non_provider(self)` (method)
- L44 `test_rejects_empty_name(self)` (method)
- L56 `test_reregister_overwrites(self)` (method)
- L63 `test_list_is_sorted(self)` (method)
- L70 `TestGetActiveProvider` (class)
- L71 `test_single_provider_autoresolves(self, tmp_path, monkeypatch)` (method)
- L77 `test_no_provider_returns_none(self, tmp_path, monkeypatch)` (method)
- L81 `test_multi_without_config_returns_none(self, tmp_path, monkeypatch)` (method) — Unlike image_gen (which falls back to 'fal'), video_gen has no
- L91 `test_config_selects_provider(self, tmp_path, monkeypatch)` (method)
- L103 `test_unknown_config_falls_back(self, tmp_path, monkeypatch)` (method) — If video_gen.provider names a provider that isn't registered,
