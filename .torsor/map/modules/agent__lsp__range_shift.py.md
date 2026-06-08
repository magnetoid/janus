---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/range_shift.py

Symbols in `agent/lsp/range_shift.py`.

- L33 `build_line_shift(pre_text: str, post_text: str)` (function) — Build a function mapping pre-edit line numbers to post-edit line numbers.
- L91 `shift_diagnostic_range(diag: Dict[str, Any], shift: Callable[[int], Optional[int]])` (function) — Return a copy of ``diag`` with its line range remapped through ``shift``.
- L136 `shift_baseline(baseline: List[Dict[str, Any]], shift: Callable[[int], Optional[int]])` (function) — Apply ``shift`` to every diagnostic in ``baseline``, dropping deleted entries.
