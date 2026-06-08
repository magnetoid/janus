---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/skin_engine.py

Symbols in `hermes_cli/skin_engine.py`.

- L130 `SkinConfig` (class) — Complete skin configuration.
- L142 `get_color(self, key: str, fallback: str='')` (method) — Get a color value with fallback.
- L146 `get_spinner_wings(self)` (method) — Get spinner wing pairs, or empty list if none.
- L155 `get_branding(self, key: str, fallback: str='')` (method) — Get a branding value with fallback.
- L656 `_skins_dir()` (function) — User skins directory.
- L661 `_load_skin_from_yaml(path: Path)` (function) — Load a skin definition from a YAML file.
- L674 `_mapping_or_empty(value: Any, *, section: str, skin_name: str)` (function) — Return a mapping value or an empty dict when the section type is invalid.
- L689 `_build_skin_config(data: Dict[str, Any])` (function) — Build a SkinConfig from a raw dict (built-in or loaded from YAML).
- L719 `list_skins()` (function) — List all available skins (built-in + user-installed).
- L750 `load_skin(name: str)` (function) — Load a skin by name. Checks user skins first, then built-in.
- L769 `get_active_skin()` (function) — Get the currently active skin config (cached).
- L777 `set_active_skin(name: str)` (function) — Switch the active skin. Returns the new SkinConfig.
- L785 `get_active_skin_name()` (function) — Get the name of the currently active skin.
- L790 `init_skin_from_config(config: dict)` (function) — Initialize the active skin from CLI config at startup.
- L810 `get_active_prompt_symbol(fallback: str='❯')` (function) — Return the interactive prompt symbol with a single trailing space.
- L828 `get_active_help_header(fallback: str='(^_^)? Available Commands')` (function) — Get the /help header from the active skin.
- L837 `get_active_goodbye(fallback: str='Goodbye! ⚕')` (function) — Get the goodbye line from the active skin.
- L846 `get_prompt_toolkit_style_overrides()` (function) — Return prompt_toolkit style overrides derived from the active skin.
