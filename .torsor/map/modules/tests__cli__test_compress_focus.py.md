---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_compress_focus.py

Symbols in `tests/cli/test_compress_focus.py`.

- L11 `_make_history()` (function)
- L20 `test_focus_topic_extracted_and_passed(capsys)` (function) — Focus topic is extracted from the command and passed to _compress_context.
- L48 `test_no_focus_topic_when_bare_command(capsys)` (function) — When no focus topic is provided, None is passed.
- L66 `test_empty_focus_after_command_treated_as_none(capsys)` (function) — Trailing whitespace after /compress does not produce a focus topic.
- L84 `test_focus_topic_printed_in_compression_banner(capsys)` (function) — The focus topic shows in the compression progress banner.
- L102 `test_no_focus_prints_standard_banner(capsys)` (function) — Without focus, the standard banner (no focus: line) is printed.
