---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_lazy_install_views.py

Symbols in `tests/gateway/test_discord_lazy_install_views.py`.

- L30 `TestDefineDiscordViewClasses` (class) — _define_discord_view_classes() registers all UI view classes in module globals.
- L33 `test_registers_all_five_view_classes(self, monkeypatch)` (method) — Calling _define_discord_view_classes() must (re)define all 5 view classes.
- L52 `test_check_discord_requirements_calls_define_on_lazy_install(self, monkeypatch)` (method) — check_discord_requirements() must call _define_discord_view_classes() on
