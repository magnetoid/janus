---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tts_picker.py

Symbols in `tests/hermes_cli/test_tts_picker.py`.

- L18 `_FakeTTSProvider` (class)
- L19 `__init__(self, name: str, schema: dict | None=None)` (method)
- L24 `name(self)` (method)
- L27 `synthesize(self, text, output_path, **kw)` (method)
- L30 `get_setup_schema(self)` (method)
- L37 `_reset_registry()` (function)
- L43 `TestPluginTTSProviders` (class) — ``_plugin_tts_providers()`` returns picker-row dicts.
- L46 `test_empty_when_no_plugins(self)` (method)
- L49 `test_returns_row_for_registered_plugin(self)` (method)
- L76 `test_filters_builtin_shadow_defensively(self)` (method) — Even if a plugin slipped past the registry's built-in check
- L96 `test_skips_providers_with_no_name(self)` (method) — Defense in depth: a provider with no .name attribute is skipped
- L113 `test_skips_providers_whose_schema_raises(self)` (method)
- L123 `test_minimal_schema_uses_display_name(self)` (method) — A provider with no setup_schema override gets a row built from
- L133 `test_post_setup_passthrough(self)` (method)
- L148 `TestVisibleProvidersInjectsTTSPlugins` (class) — ``_visible_providers()`` injects plugin rows into the Text-to-Speech
- L152 `test_tts_category_includes_plugin_rows(self)` (method)
- L169 `test_other_categories_unaffected_by_tts_plugins(self)` (method) — Registering a TTS plugin must not leak into the Image Generation
- L179 `test_tts_category_without_plugins_only_hardcoded(self)` (method) — No plugins → picker shows exactly the hardcoded rows.
