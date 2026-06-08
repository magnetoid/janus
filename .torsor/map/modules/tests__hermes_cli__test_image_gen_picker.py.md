---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_image_gen_picker.py

Symbols in `tests/hermes_cli/test_image_gen_picker.py`.

- L17 `_FakeProvider` (class)
- L18 `__init__(self, name: str, available: bool=True, schema=None, models=None)` (method)
- L33 `name(self)` (method)
- L36 `is_available(self)` (method)
- L39 `list_models(self)` (method)
- L42 `default_model(self)` (method)
- L45 `get_setup_schema(self)` (method)
- L48 `generate(self, prompt, aspect_ratio='landscape', **kw)` (method)
- L53 `_reset_registry()` (function)
- L59 `TestPluginPickerInjection` (class)
- L60 `test_plugin_providers_returns_registered(self, monkeypatch)` (method)
- L72 `test_fal_surfaced_alongside_other_plugins(self, monkeypatch)` (method)
- L87 `test_visible_providers_includes_plugins_for_image_gen(self, monkeypatch)` (method)
- L97 `test_visible_providers_does_not_inject_into_other_categories(self, monkeypatch)` (method)
- L107 `test_post_setup_propagated_when_declared(self, monkeypatch)` (method)
- L125 `test_post_setup_omitted_when_not_declared(self, monkeypatch)` (method)
- L135 `TestPluginCatalog` (class)
- L136 `test_plugin_catalog_returns_models(self)` (method)
- L145 `test_plugin_catalog_empty_for_unknown(self)` (method)
- L153 `TestConfigPrompt` (class)
- L154 `test_image_gen_satisfied_by_plugin_provider(self, monkeypatch, tmp_path)` (method) — When a plugin provider reports is_available(), the picker should
- L166 `test_image_gen_still_prompts_when_nothing_available(self, monkeypatch, tmp_path)` (method)
- L177 `TestConfigWriting` (class)
- L178 `test_picking_plugin_provider_writes_provider_and_model(self, monkeypatch, tmp_path)` (method) — When a user picks a plugin-backed image_gen provider with no
- L206 `test_reconfiguring_plugin_provider_writes_provider_and_model(self, monkeypatch, tmp_path)` (method) — The reconfigure path should switch image_gen away from managed FAL
- L234 `test_plugin_provider_active_overrides_managed_nous_active_label(self, monkeypatch)` (method)
- L258 `test_reconfiguring_fal_clears_plugin_provider(self, monkeypatch)` (method)
