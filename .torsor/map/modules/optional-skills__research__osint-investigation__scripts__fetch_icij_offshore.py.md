---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/research/osint-investigation/scripts/fetch_icij_offshore.py

Symbols in `optional-skills/research/osint-investigation/scripts/fetch_icij_offshore.py`.

- L47 `_cache_dir()` (function)
- L54 `_download(dest: Path, force: bool=False)` (function) — Download (or reuse cached) ICIJ bulk ZIP.
- L80 `_open_csv(zf: zipfile.ZipFile, name_pattern: str)` (function) — Open the first CSV matching name_pattern (case-insensitive substring).
- L88 `_match(needle_norm: str, hay: str)` (function)
- L92 `_normalize_query(s: str)` (function)
- L99 `fetch(entity: str | None, officer: str | None, jurisdiction: str | None, out_path: str, cache_dir: Path, force_refresh: bool=False, limit: int=500)` (function)
- L199 `main()` (function)
