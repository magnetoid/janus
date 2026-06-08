---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/reporter.py

Symbols in `agent/lsp/reporter.py`.

- L22 `format_diagnostic(d: Dict[str, Any])` (function) — One-line representation of a single diagnostic.
- L37 `report_for_file(file_path: str, diagnostics: List[Dict[str, Any]], *, severities: frozenset=DEFAULT_SEVERITIES, max_per_file: int=MAX_PER_FILE)` (function) — Build a ``<diagnostics file=...>`` block for one file.
- L63 `truncate(s: str, *, limit: int=MAX_TOTAL_CHARS)` (function) — Hard-cap a formatted summary string.
