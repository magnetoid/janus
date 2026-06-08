---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_light_mode.py

Symbols in `tests/cli/test_cli_light_mode.py`.

- L16 `cli_mod(monkeypatch)` (function) — Import cli with the light-mode cache cleared each test.
- L27 `TestLightModeDetection` (class)
- L28 `test_hermes_light_env_true_forces_light(self, cli_mod, monkeypatch)` (method)
- L32 `test_hermes_light_env_false_forces_dark(self, cli_mod, monkeypatch)` (method)
- L41 `test_theme_hint_light(self, cli_mod, monkeypatch)` (method)
- L47 `test_background_hex_hint_light(self, cli_mod, monkeypatch)` (method)
- L54 `test_background_hex_hint_dark(self, cli_mod, monkeypatch)` (method)
- L62 `test_colorfgbg_light_bg_slot(self, cli_mod, monkeypatch)` (method)
- L70 `test_cache_is_sticky(self, cli_mod, monkeypatch)` (method)
- L78 `TestOsc11Probe` (class) — The OSC 11 background probe must never run where its reply can leak
- L86 `test_skips_over_ssh(self, cli_mod, monkeypatch, var)` (method)
- L94 `test_skips_when_not_a_tty(self, cli_mod, monkeypatch)` (method)
- L99 `TestLightModeRemap` (class)
- L100 `test_remap_no_op_in_dark_mode(self, cli_mod, monkeypatch)` (method)
- L105 `test_remap_known_dark_color(self, cli_mod, monkeypatch)` (method)
- L112 `test_remap_case_insensitive(self, cli_mod, monkeypatch)` (method)
- L117 `test_remap_unknown_color_passthrough(self, cli_mod, monkeypatch)` (method)
- L122 `test_remap_skips_statusbar_paired_colors(self, cli_mod, monkeypatch)` (method) — Colors that live on a dark bg (status bar fg) MUST NOT be
- L136 `TestSkinConfigHook` (class) — The salvage wraps SkinConfig.get_color at module import time so
- L142 `test_hook_installed(self, cli_mod)` (method)
- L147 `test_hook_is_idempotent(self, cli_mod)` (method)
- L157 `test_skin_color_remaps_through_wrapper_in_light_mode(self, cli_mod, monkeypatch)` (method)
- L171 `test_skin_color_passthrough_in_dark_mode(self, cli_mod, monkeypatch)` (method)
