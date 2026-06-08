---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/schema_sanitizer.py

Symbols in `tools/schema_sanitizer.py`.

- L40 `sanitize_tool_schemas(tools: list[dict])` (function) — Return a copy of ``tools`` with each tool's parameter schema sanitized.
- L58 `_sanitize_single_tool(tool: dict)` (function) — Deep-copy and sanitize a single OpenAI-format tool entry.
- L99 `_strip_top_level_combinators(params: dict, *, path: str='<tool>')` (function) — Drop combinator keywords from the top-level of a function parameters schema.
- L131 `strip_nullable_unions(schema: Any, *, keep_nullable_hint: bool=True)` (function) — Collapse ``anyOf`` / ``oneOf`` nullable unions to the non-null branch.
- L193 `_sanitize_node(node: Any, path: str)` (function) — Recursively sanitize a JSON-Schema fragment.
- L308 `strip_pattern_and_format(tools: list[dict])` (function) — Strip ``pattern`` and ``format`` JSON Schema keywords from tool schemas.
- L385 `strip_slash_enum(tools: list[dict])` (function) — Strip ``enum`` keywords whose string values contain a forward slash.
