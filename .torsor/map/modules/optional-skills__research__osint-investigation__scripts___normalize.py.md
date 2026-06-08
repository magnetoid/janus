---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/research/osint-investigation/scripts/_normalize.py

Symbols in `optional-skills/research/osint-investigation/scripts/_normalize.py`.

- L31 `normalize_name(name: str | None)` (function) — Standard normalization: uppercase, strip suffixes, drop punctuation.
- L41 `normalize_aggressive(name: str | None)` (function) — Aggressive normalization: sorted unique tokens (word-bag).
- L49 `name_tokens(name: str | None, min_len: int=4)` (function) — Token set used for overlap matching.
- L57 `token_overlap_ratio(left: str | None, right: str | None)` (function) — Return (jaccard-like ratio, shared token count) over min-len tokens.
