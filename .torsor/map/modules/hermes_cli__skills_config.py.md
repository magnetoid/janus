---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/skills_config.py

Symbols in `hermes_cli/skills_config.py`.

- L27 `get_disabled_skills(config: dict, platform: Optional[str]=None)` (function) — Return disabled skill names. Platform-specific list falls back to global.
- L39 `save_disabled_skills(config: dict, disabled: Set[str], platform: Optional[str]=None)` (function) — Persist disabled skill names to config.
- L52 `_list_all_skills()` (function) — Return all installed skills (ignoring disabled state).
- L61 `_get_categories(skills: List[dict])` (function) — Return sorted unique category names (None -> 'uncategorized').
- L68 `_select_platform()` (function) — Ask user which platform to configure, or global.
- L94 `_toggle_by_category(skills: List[dict], disabled: Set[str])` (function) — Toggle all skills in a category at once.
- L125 `skills_command(args=None)` (function) — Entry point for `hermes skills`.
