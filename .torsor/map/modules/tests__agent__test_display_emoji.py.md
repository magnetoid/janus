---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_display_emoji.py

Symbols in `tests/agent/test_display_emoji.py`.

- L8 `TestGetToolEmoji` (class) — Verify the skin → registry → fallback resolution chain.
- L11 `test_returns_registry_emoji_when_no_skin(self)` (method) — Registry-registered emoji is used when no skin is active.
- L33 `test_skin_override_takes_precedence(self)` (method) — Skin tool_emojis override registry defaults.
- L41 `test_skin_empty_dict_falls_through(self)` (method) — Empty skin tool_emojis falls through to registry.
- L55 `test_fallback_default(self)` (method) — When neither skin nor registry has an emoji, use the default.
- L69 `test_custom_default(self)` (method) — Custom default is returned when nothing matches.
- L81 `test_skin_override_only_for_matching_tool(self)` (method) — Skin override for one tool doesn't affect others.
- L96 `TestSkinConfigToolEmojis` (class) — Verify SkinConfig handles tool_emojis field correctly.
- L99 `test_skin_config_has_tool_emojis_field(self)` (method)
- L104 `test_skin_config_accepts_tool_emojis(self)` (method)
- L110 `test_build_skin_config_includes_tool_emojis(self)` (method)
- L119 `test_build_skin_config_empty_tool_emojis_default(self)` (method)
