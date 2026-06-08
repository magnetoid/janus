---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_video_gen_picker.py

Symbols in `tests/hermes_cli/test_video_gen_picker.py`.

- L19 `_FakeVideoProvider` (class)
- L20 `__init__(self, name: str, available: bool=True, schema: Optional[Dict[str, Any]]=None, models: Optional[List[Dict[str, Any]]]=None)` (method)
- L46 `name(self)` (method)
- L49 `is_available(self)` (method)
- L52 `list_models(self)` (method)
- L55 `default_model(self)` (method)
- L58 `get_setup_schema(self)` (method)
- L61 `generate(self, prompt, **kw)` (method)
- L66 `_reset_registry()` (function)
- L72 `TestReconfigureWritesProvider` (class) — Regression tests for the video_gen reconfigure path.
- L83 `test_reconfigure_with_env_vars_already_set_writes_provider(self, monkeypatch, tmp_path)` (method) — Env vars present and user accepts current value → still writes
- L118 `test_reconfigure_with_no_env_vars_writes_provider(self, monkeypatch, tmp_path)` (method) — No env vars at all (managed-style plugin) → writes
- L151 `TestPluginVideoProvidersRow` (class) — Tests for _plugin_video_gen_providers row contents.
- L154 `test_post_setup_propagated_when_declared(self, monkeypatch)` (method)
- L172 `test_post_setup_omitted_when_not_declared(self, monkeypatch)` (method)
- L182 `TestVideoPluginProviderActive` (class) — Tests for _is_provider_active recognizing video_gen_plugin_name.
- L185 `test_active_when_video_gen_provider_matches(self)` (method)
- L193 `test_inactive_when_video_gen_provider_differs(self)` (method)
- L201 `test_inactive_when_video_gen_section_missing(self)` (method)
- L207 `test_detect_active_index_picks_video_plugin_match(self, monkeypatch)` (method) — When xAI is the configured video_gen provider, the picker should
