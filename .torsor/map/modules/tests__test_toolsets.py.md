---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_toolsets.py

Symbols in `tests/test_toolsets.py`.

- L16 `_dummy_handler(args, **kwargs)` (function)
- L20 `_make_schema(name: str, description: str='test tool')` (function)
- L28 `TestGetToolset` (class)
- L29 `test_known_toolset(self)` (method)
- L34 `test_merges_registry_tools_into_builtin_toolset(self, monkeypatch)` (method)
- L49 `test_unknown_returns_none(self)` (method)
- L53 `TestResolveToolset` (class)
- L54 `test_leaf_toolset(self)` (method)
- L58 `test_composite_toolset(self)` (method)
- L64 `test_cycle_detection(self)` (method)
- L77 `test_unknown_toolset_returns_empty(self)` (method)
- L80 `test_plugin_toolset_uses_registry_snapshot(self, monkeypatch)` (method)
- L99 `test_all_alias(self)` (method)
- L103 `test_star_alias(self)` (method)
- L108 `TestResolveMultipleToolsets` (class)
- L109 `test_combines_and_deduplicates(self)` (method)
- L117 `test_empty_list(self)` (method)
- L121 `TestValidateToolset` (class)
- L122 `test_valid(self)` (method)
- L126 `test_all_alias_valid(self)` (method)
- L130 `test_invalid(self)` (method)
- L133 `test_mcp_alias_uses_live_registry(self, monkeypatch)` (method)
- L150 `TestGetToolsetInfo` (class)
- L151 `test_leaf(self)` (method)
- L157 `test_composite(self)` (method)
- L162 `test_unknown_returns_none(self)` (method)
- L166 `TestCreateCustomToolset` (class)
- L167 `test_runtime_creation(self)` (method)
- L183 `TestRegistryOwnedToolsets` (class)
- L184 `test_registry_membership_is_live(self, monkeypatch)` (method)
- L200 `TestToolsetConsistency` (class) — Verify structural integrity of the built-in TOOLSETS dict.
- L203 `test_all_toolsets_have_required_keys(self)` (method)
- L209 `test_all_includes_reference_existing_toolsets(self)` (method)
- L214 `test_hermes_platforms_share_core_tools(self)` (method) — All hermes-* platform toolsets share the same core tools.
- L233 `TestPluginToolsets` (class)
- L234 `test_get_all_toolsets_includes_plugin_toolset(self, monkeypatch)` (method)
- L250 `TestDefaultPlatformWebSearchCoverage` (class)
- L251 `test_hermes_whatsapp_toolset_includes_web_search(self)` (method)
- L254 `test_hermes_api_server_toolset_includes_web_search(self)` (method)
