---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/tool_search.py

Symbols in `tools/tool_search.py`.

- L64 `ToolSearchConfig` (class) — Resolved, validated tool-search configuration for a single assembly.
- L73 `from_raw(cls, raw: Any)` (method) — Build a config from a raw dict / bool / None.
- L117 `_safe_int(value: Any, fallback: int)` (function)
- L124 `_safe_float(value: Any, fallback: float)` (function)
- L131 `load_config()` (function) — Load tool-search config from the user config file.
- L150 `_core_tool_names()` (function) — Return the set of tool names that must NEVER be deferred.
- L163 `is_deferrable_tool_name(name: str)` (function) — Return True if a tool with this name is *eligible* for deferral.
- L189 `classify_tools(tool_defs: List[Dict[str, Any]])` (function) — Split a tool-defs list into (visible, deferrable).
- L217 `estimate_tokens_from_schemas(tool_defs: Iterable[Dict[str, Any]])` (function) — Estimate the token cost of a tool-defs list via the chars/4 rule.
- L234 `should_activate(config: ToolSearchConfig, deferrable_tokens: int, context_length: Optional[int])` (function) — Decide whether tool search should activate for the current assembly.
- L267 `CatalogEntry` (class) — One deferrable tool, in a form the bridge tools can search and serve.
- L283 `_tokenize(text: str)` (function)
- L289 `_entry_search_text(td: Dict[str, Any])` (function) — Build the search-text blob for a deferrable tool.
- L307 `_classify_source(name: str)` (function) — Return (source_kind, source_name) for a registered tool name.
- L321 `build_catalog(tool_defs: List[Dict[str, Any]])` (function) — Build the deferred-tool catalog from a tool-defs list.
- L347 `_bm25_score(query_tokens: List[str], doc_tokens: List[str], doc_lengths: List[int], avg_dl: float, doc_freq: Dict[str, int], n_docs: int, k1: float=1.5, b: float=0.75)` (function) — Standard BM25 score for one query against one document.
- L378 `search_catalog(catalog: List[CatalogEntry], query: str, limit: int=5)` (function) — Return the top-``limit`` catalog entries for ``query`` by BM25.
- L426 `bridge_tool_schemas(deferred_count: int)` (function) — Build the bridge tool schemas to inject in place of deferred tools.
- L519 `AssemblyResult` (class) — Outcome of one assembly. Useful for tests and observability.
- L529 `assemble_tool_defs(tool_defs: List[Dict[str, Any]], *, context_length: Optional[int]=None, config: Optional[ToolSearchConfig]=None)` (function) — Return the tool-defs list the model should actually see.
- L591 `is_bridge_tool(name: str)` (function)
- L595 `_format_search_hit(entry: CatalogEntry)` (function)
- L605 `dispatch_tool_search(args: Dict[str, Any], *, current_tool_defs: List[Dict[str, Any]], config: Optional[ToolSearchConfig]=None)` (function) — Execute the ``tool_search`` bridge tool. Returns a JSON string.
- L632 `dispatch_tool_describe(args: Dict[str, Any], *, current_tool_defs: List[Dict[str, Any]])` (function) — Execute the ``tool_describe`` bridge tool. Returns a JSON string.
- L660 `scoped_deferrable_names(tool_defs: List[Dict[str, Any]])` (function) — Return the set of deferrable tool names present in ``tool_defs``.
- L680 `resolve_underlying_call(args: Dict[str, Any])` (function) — Parse a ``tool_call`` invocation into (underlying_name, args, error_msg).
