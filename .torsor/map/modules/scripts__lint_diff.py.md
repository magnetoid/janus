---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/lint_diff.py

Symbols in `scripts/lint_diff.py`.

- L29 `_load_json(path: Path | None)` (function)
- L42 `_normalize_ruff(entries: list[dict])` (function) — Ruff JSON: {code, filename, location.row, message}.
- L66 `_normalize_ty(entries: list[dict])` (function) — ty gitlab JSON: {check_name, location.path, location.positions.begin.line, description}.
- L84 `_key(d: dict)` (function) — Stable diagnostic identity across commits: (path, rule, message).
- L91 `_diff(base: list[dict], head: list[dict])` (function)
- L107 `_rule_counts(entries: list[dict])` (function)
- L111 `_section(title: str, entries: list[dict], limit: int=25)` (function)
- L135 `_tool_report(tool_name: str, base: list[dict], head: list[dict], base_available: bool)` (function)
- L164 `main()` (function)
