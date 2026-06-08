---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_skin_engine.py

Symbols in `tests/hermes_cli/test_skin_engine.py`.

- L7 `reset_skin_state()` (function) — Reset skin engine state between tests.
- L17 `TestSkinConfig` (class)
- L18 `test_default_skin_has_required_fields(self)` (method)
- L27 `test_get_color_with_fallback(self)` (method)
- L33 `test_get_branding_with_fallback(self)` (method)
- L39 `test_get_spinner_wings_empty_for_default(self)` (method)
- L45 `TestBuiltinSkins` (class)
- L46 `test_ares_skin_loads(self)` (method)
- L57 `test_ares_has_spinner_customization(self)` (method)
- L65 `test_mono_skin_loads(self)` (method)
- L71 `test_slate_skin_loads(self)` (method)
- L77 `test_daylight_skin_loads(self)` (method)
- L91 `test_warm_lightmode_skin_loads(self)` (method)
- L99 `test_charizard_skin_has_dark_ember_completion_menu(self)` (method)
- L111 `test_unknown_skin_falls_back_to_default(self)` (method)
- L116 `test_all_builtin_skins_have_complete_colors(self)` (method)
- L126 `TestSkinManagement` (class)
- L127 `test_set_active_skin(self)` (method)
- L134 `test_get_active_skin_defaults(self)` (method)
- L139 `test_list_skins_includes_builtins(self)` (method)
- L153 `test_init_skin_from_config(self)` (method)
- L158 `test_init_skin_from_empty_config(self)` (method)
- L163 `test_init_skin_from_null_display(self)` (method) — display: null should fall back to default, not crash.
- L169 `test_init_skin_from_non_dict_display(self)` (method) — display: <non-dict> should fall back to default.
- L182 `TestUserSkins` (class)
- L183 `test_load_user_skin_from_yaml(self, tmp_path, monkeypatch)` (method)
- L210 `test_load_user_skin_invalid_section_types_fall_back_to_defaults(self, tmp_path, monkeypatch)` (method)
- L241 `test_list_skins_includes_user_skins(self, tmp_path, monkeypatch)` (method)
- L259 `TestDisplayIntegration` (class)
- L260 `test_get_skin_tool_prefix_default(self)` (method)
- L264 `test_get_skin_tool_prefix_custom(self)` (method)
- L270 `test_tool_message_uses_skin_prefix(self)` (method)
- L278 `test_tool_message_default_prefix(self)` (method)
- L284 `TestCliBrandingHelpers` (class)
- L285 `test_active_prompt_symbol_default(self)` (method)
- L290 `test_active_prompt_symbol_ares(self)` (method)
- L296 `test_active_help_header_ares(self)` (method)
- L302 `test_active_goodbye_ares(self)` (method)
- L308 `test_prompt_toolkit_style_overrides_cover_tui_classes(self)` (method)
- L361 `test_prompt_toolkit_style_overrides_use_skin_colors(self)` (method)
