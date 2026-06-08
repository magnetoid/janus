---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tool_search.py

Symbols in `tests/tools/test_tool_search.py`.

- L23 `_td(name: str, description: str='', properties: Dict[str, Any] | None=None)` (function)
- L42 `TestConfigParsing` (class)
- L43 `test_default_when_missing(self)` (method)
- L49 `test_bool_true_maps_to_auto(self)` (method)
- L54 `test_bool_false_maps_to_off(self)` (method)
- L59 `test_explicit_on(self)` (method)
- L64 `test_invalid_enabled_falls_back_to_auto(self)` (method)
- L69 `test_threshold_clamped(self)` (method)
- L76 `test_search_limits_clamped(self)` (method)
- L91 `TestClassification` (class)
- L92 `test_core_tools_never_defer(self)` (method) — The critical invariant from the OpenClaw report.
- L104 `test_bridge_tools_never_defer(self)` (method)
- L109 `test_unknown_tool_not_deferrable(self)` (method) — Defensive: a tool name we cannot resolve to a registry entry must
- L116 `test_classify_keeps_unknown_in_visible(self)` (method) — A tool we can't classify stays visible — never silently dropped.
- L136 `TestThresholdGate` (class)
- L137 `test_off_never_activates(self)` (method)
- L142 `test_zero_deferrable_never_activates(self)` (method)
- L147 `test_on_activates_with_any_deferrable(self)` (method)
- L152 `test_auto_below_threshold_does_not_activate(self)` (method)
- L158 `test_auto_at_or_above_threshold_activates(self)` (method)
- L164 `test_auto_without_context_length_uses_20k_cutoff(self)` (method) — Fallback cutoff used when the active model is unknown.
- L171 `test_token_estimate_proportional_to_schema_size(self)` (method)
- L187 `TestRetrieval` (class)
- L188 `_fake_catalog(self)` (method) — Build a catalog directly without touching the registry.
- L212 `test_search_finds_relevant_tool(self)` (method)
- L218 `test_search_returns_empty_for_irrelevant_query(self)` (method)
- L223 `test_search_substring_fallback(self)` (method) — Even when no BM25 hit, a literal substring of the tool name returns.
- L229 `test_search_respects_limit(self)` (method)
- L240 `TestAssembly` (class)
- L241 `test_no_deferrable_returns_unchanged(self)` (method) — Pure-core toolset: pass-through, no bridge tools added.
- L253 `test_below_threshold_returns_unchanged(self)` (method) — Tiny deferrable surface: don't bother.
- L268 `test_idempotent_when_bridge_already_present(self)` (method)
- L287 `TestBridgeDispatch` (class)
- L288 `test_tool_search_requires_query(self)` (method)
- L293 `test_tool_describe_requires_name(self)` (method)
- L298 `test_tool_describe_rejects_non_deferrable(self)` (method) — If the model asks to describe a core tool, refuse — it's already
- L307 `test_resolve_underlying_call_parses_object_args(self)` (method)
- L316 `test_resolve_underlying_call_parses_json_string_args(self)` (method) — Some models emit ``arguments`` as a JSON string instead of object.
- L329 `test_resolve_underlying_call_rejects_bad_json(self)` (method)
- L338 `test_resolve_underlying_call_rejects_recursion(self)` (method) — tool_call cannot invoke tool_call itself.
- L354 `TestHandleFunctionCallIntegration` (class)
- L355 `test_tool_search_dispatch_through_handle_function_call(self)` (method) — The dispatcher recognizes the bridge tool by name.
- L368 `TestRegression_OpenClawCron84141` (class) — Regression guard for the OpenClaw cron-tool-loss class of bug.
- L380 `test_core_tool_survives_alongside_many_mcp_tools(self)` (method)
- L407 `test_unwrap_rejects_core_tool_attempt(self)` (method) — Even if the model tries to invoke a core tool through tool_call,
- L419 `TestRegression_ToolsetScoping` (class) — A restricted-toolset session must not see or invoke out-of-scope tools.
- L437 `_register(name, toolset)` (method)
- L450 `test_search_catalog_is_scoped_to_session_toolsets(self)` (method)
- L472 `test_tool_call_rejects_out_of_scope_tool(self)` (method)
- L497 `test_bridge_dispatch_does_not_pollute_global_resolved_names(self)` (method)
- L524 `test_scoped_deferrable_names_helper(self)` (method)
