---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/markdown_tables.py

Symbols in `agent/markdown_tables.py`.

- L49 `_disp_width(s: str)` (function) — ``wcswidth`` clamped to a non-negative integer.
- L61 `_pad_to_width(s: str, target: int)` (function)
- L65 `split_table_row(row: str)` (function) — Split ``| a | b | c |`` into ``["a", "b", "c"]`` with trims.
- L76 `is_table_divider(row: str)` (function) — True when ``row`` is a markdown table separator line.
- L83 `looks_like_table_row(row: str)` (function) — True when ``row`` could plausibly be a markdown table row.
- L105 `_render_block(rows: List[List[str]], available_width: int | None=None)` (function) — Render ``rows`` (header + body, divider implied) at uniform widths.
- L145 `_wrap_to_width(text: str, width: int)` (function) — Soft-wrap ``text`` at word boundaries to fit ``width`` display cells.
- L211 `_render_vertical(rows: List[List[str]], ncols: int, available_width: int)` (function) — Render a too-wide table as vertical ``Header: value`` rows.
- L263 `realign_markdown_tables(text: str, available_width: int | None=None)` (function) — Rewrite every ``| ... |`` + divider block with wcwidth-aware padding.
