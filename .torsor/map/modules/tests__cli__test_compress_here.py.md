---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_compress_here.py

Symbols in `tests/cli/test_compress_here.py`.

- L13 `_make_history()` (function)
- L22 `_wire_agent(shell, compressed_head)` (function)
- L31 `test_compress_here_compresses_head_only(capsys)` (function) — /compress here 2 passes only the head to _compress_context.
- L53 `test_compress_here_reappends_verbatim_tail(capsys)` (function) — The most recent exchanges are preserved verbatim after the summary.
- L76 `test_compress_here_banner_mentions_summarizing_up_to_here(capsys)` (function)
- L90 `test_bare_compress_still_full(capsys)` (function) — /compress with no args compresses the whole history (full mode).
- L107 `test_focus_still_works(capsys)` (function) — /compress <focus> keeps the existing focus behavior.
