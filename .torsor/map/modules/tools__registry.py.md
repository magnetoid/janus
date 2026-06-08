---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/registry.py

Symbols in `tools/registry.py`.

- L29 `_is_registry_register_call(node: ast.AST)` (function) — Return True when *node* is a ``registry.register(...)`` call expression.
- L42 `_module_registers_tools(module_path: Path)` (function) — Return True when the module contains a top-level ``registry.register(...)`` call.
- L57 `discover_builtin_tools(tools_dir: Optional[Path]=None)` (function) — Import built-in self-registering tool modules and return their module names.
- L77 `ToolEntry` (class) — Metadata for a single registered tool.
- L86 `__init__(self, name, toolset, schema, handler, check_fn, requires_env, is_async, description, emoji, max_result_size_chars=None, dynamic_schema_overrides=None)` (method)
- L126 `_check_fn_cached(fn: Callable)` (function) — Return bool(fn()), TTL-cached across calls. Swallows exceptions as False.
- L144 `invalidate_check_fn_cache()` (function) — Drop all cached ``check_fn`` results. Call after config changes that
- L151 `ToolRegistry` (class) — Singleton registry that collects tool schemas + handlers from tool files.
- L154 `__init__(self)` (method)
- L169 `_snapshot_state(self)` (method) — Return a coherent snapshot of registry entries and toolset checks.
- L174 `_snapshot_entries(self)` (method) — Return a stable snapshot of registered tool entries.
- L178 `_snapshot_toolset_checks(self)` (method) — Return a stable snapshot of toolset availability checks.
- L182 `_evaluate_toolset_check(self, toolset: str, check: Callable | None)` (method) — Run a toolset check, treating missing or failing checks as unavailable/available.
- L192 `get_entry(self, name: str)` (method) — Return a registered tool entry by name, or None.
- L197 `get_registered_toolset_names(self)` (method) — Return sorted unique toolset names present in the registry.
- L201 `get_tool_names_for_toolset(self, toolset: str)` (method) — Return sorted tool names registered under a given toolset.
- L208 `register_toolset_alias(self, alias: str, toolset: str)` (method) — Register an explicit alias for a canonical toolset name.
- L220 `get_registered_toolset_aliases(self)` (method) — Return a snapshot of ``{alias: canonical_toolset}`` mappings.
- L225 `get_toolset_alias_target(self, alias: str)` (method) — Return the canonical toolset name for an alias, or None.
- L234 `register(self, name: str, toolset: str, schema: dict, handler: Callable, check_fn: Callable=None, requires_env: list=None, is_async: bool=False, description: str='', emoji: str='', max_result_size_chars: int | float | None=None, dynamic_schema_overrides: Callable=None, override: bool=False)` (method) — Register a tool.  Called at module-import time by each tool file.
- L307 `deregister(self, name: str)` (method) — Remove a tool from the registry.
- L337 `get_definitions(self, tool_names: Set[str], quiet: bool=False)` (method) — Return OpenAI-format tool schemas for the requested tool names.
- L390 `dispatch(self, name: str, args: dict, **kwargs)` (method) — Execute a tool handler by name.
- L422 `get_max_result_size(self, name: str, default: int | float | None=None)` (method) — Return per-tool max result size, or *default* (or global default).
- L432 `get_all_tool_names(self)` (method) — Return sorted list of all registered tool names.
- L436 `get_schema(self, name: str)` (method) — Return a tool's raw schema dict, bypassing check_fn filtering.
- L445 `get_toolset_for_tool(self, name: str)` (method) — Return the toolset a tool belongs to, or None.
- L450 `get_emoji(self, name: str, default: str='⚡')` (method) — Return the emoji for a tool, or *default* if unset.
- L455 `get_tool_to_toolset_map(self)` (method) — Return ``{tool_name: toolset_name}`` for every registered tool.
- L459 `is_toolset_available(self, toolset: str)` (method) — Check if a toolset's requirements are met.
- L469 `check_toolset_requirements(self)` (method) — Return ``{toolset: available_bool}`` for every toolset.
- L478 `get_available_toolsets(self)` (method) — Return toolset metadata for UI display.
- L500 `get_toolset_requirements(self)` (method) — Build a TOOLSET_REQUIREMENTS-compatible dict for backward compat.
- L521 `check_tool_availability(self, quiet: bool=False)` (method) — Return (available_toolsets, unavailable_info) like the old function.
- L563 `tool_error(message, **extra)` (function) — Return a JSON error string for tool handlers.
- L577 `tool_result(data=None, **kwargs)` (function) — Return a JSON result string for tool handlers.
