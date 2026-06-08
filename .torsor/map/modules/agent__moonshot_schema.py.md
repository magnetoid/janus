---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/moonshot_schema.py

Symbols in `agent/moonshot_schema.py`.

- L41 `_repair_schema(node: Any, is_schema: bool=True)` (function) — Recursively apply Moonshot repairs to a schema node.
- L136 `_fill_missing_type(node: Dict[str, Any])` (function) — Infer a reasonable ``type`` if this schema node has none.
- L163 `sanitize_moonshot_tool_parameters(parameters: Any)` (function) — Normalize tool parameters to a Moonshot-compatible object schema.
- L185 `sanitize_moonshot_tools(tools: List[Dict[str, Any]])` (function) — Apply ``sanitize_moonshot_tool_parameters`` to every tool's parameters.
- L212 `is_moonshot_model(model: str | None)` (function) — True for any Kimi / Moonshot model slug, regardless of aggregator prefix.
