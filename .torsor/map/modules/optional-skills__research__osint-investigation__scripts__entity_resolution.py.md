---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/research/osint-investigation/scripts/entity_resolution.py

Symbols in `optional-skills/research/osint-investigation/scripts/entity_resolution.py`.

- L41 `_read_csv(path: str, name_col: str)` (function)
- L56 `_build_index(rows: list[dict[str, str]], name_col: str)` (function) — Index by exact-normalized and aggressive (sorted-token) form.
- L71 `_emit(out_rows: list[dict[str, str]], seen: set[tuple], match_type: str, left_row: dict[str, str], right_row: dict[str, str], left_col: str, right_col: str, ratio: float=0.0, shared: int=0)` (function)
- L108 `resolve(left_path: str, left_col: str, right_path: str, right_col: str, out_path: str, overlap_threshold: float=0.6, min_shared: int=2, skip_overlap: bool=False)` (function)
- L181 `main()` (function)
