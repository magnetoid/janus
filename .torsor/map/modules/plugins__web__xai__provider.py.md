---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/xai/provider.py

Symbols in `plugins/web/xai/provider.py`.

- L64 `_load_xai_web_config()` (function) — Read ``web.xai`` from config.yaml (returns {} on miss).
- L78 `_coerce_domain_list(value: Any)` (function) — Coerce a config value to a clean list of <=5 domain strings.
- L96 `XAIWebSearchProvider` (class) — Search-only provider backed by xAI's agentic Web Search tool.
- L121 `name(self)` (method)
- L125 `display_name(self)` (method)
- L128 `is_available(self)` (method) — Cheap availability probe — env var OR auth-store has OAuth tokens.
- L140 `supports_search(self)` (method)
- L143 `supports_extract(self)` (method)
- L148 `search(self, query: str, limit: int=5)` (method) — Execute a Grok-backed web search.
- L340 `_build_prompt(query: str, limit: int)` (method) — Compose the prompt that asks Grok to act as a search engine.
- L361 `_extract_results(cls, response_data: Dict[str, Any], *, limit: int)` (method) — Pull a ``[{title, url, description, position}, ...]`` list out of a
- L418 `_collect_output_text(response_data: Dict[str, Any])` (method) — Return (text_blocks, annotations) extracted from ``response.output``.
- L448 `_try_parse_json_results(text: str, *, limit: int)` (method) — Parse a JSON object with a ``results`` array out of ``text``.
- L499 `_results_from_annotations(annotations: List[Dict[str, Any]], joined_text: str, *, limit: int)` (method) — Best-effort fallback when JSON parsing fails.
- L544 `get_setup_schema(self)` (method)
