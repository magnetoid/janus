---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# toolsets.py

Symbols in `toolsets.py`.

- L555 `get_toolset(name: str)` (function) — Get a toolset definition by name.
- L606 `resolve_toolset(name: str, visited: Set[str]=None)` (function) — Recursively resolve a toolset to get all tool names.
- L680 `resolve_multiple_toolsets(toolset_names: List[str])` (function) — Resolve multiple toolsets and combine their tools.
- L699 `_get_plugin_toolset_names()` (function) — Return toolset names registered by plugins (from the tool registry).
- L716 `_get_registry_toolset_aliases()` (function) — Return explicit toolset aliases registered in the live registry.
- L725 `get_all_toolsets()` (function) — Get all available toolsets with their definitions.
- L750 `get_toolset_names()` (function) — Get names of all available toolsets (excluding aliases).
- L773 `validate_toolset(name: str)` (function) — Check if a toolset name is valid.
- L793 `create_custom_toolset(name: str, description: str, tools: List[str]=None, includes: List[str]=None)` (function) — Create a custom toolset at runtime.
- L817 `get_toolset_info(name: str)` (function) — Get detailed information about a toolset including resolved tools.
