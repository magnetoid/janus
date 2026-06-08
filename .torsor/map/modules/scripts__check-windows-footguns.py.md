---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/check-windows-footguns.py

Symbols in `scripts/check-windows-footguns.py`.

- L118 `Footgun` (class) — A Windows cross-platform footgun pattern.
- L330 `should_scan_file(path: Path)` (function) — Return True if this file is in scope for the checker.
- L352 `iter_files(paths: Iterable[Path])` (function)
- L367 `_strip_code(line: str)` (function) — Return just the code portion of a line — strip trailing comments and
- L386 `_find_unquoted_hash(line: str)` (function) — Index of the first `#` not inside a single/double/triple-quoted string.
- L411 `scan_file(path: Path, footguns: list[Footgun])` (function) — Return a list of (line_number, line, footgun) for unsuppressed matches.
- L488 `get_staged_files()` (function) — Return paths staged in the current git index. Empty on non-git trees.
- L502 `get_diff_files(ref: str)` (function) — Return paths modified vs. the given git ref.
- L516 `parse_args(argv: list[str])` (function)
- L544 `print_rules()` (function)
- L553 `main(argv: list[str])` (function)
