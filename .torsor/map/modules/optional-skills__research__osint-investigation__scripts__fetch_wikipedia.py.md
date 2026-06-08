---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/research/osint-investigation/scripts/fetch_wikipedia.py

Symbols in `optional-skills/research/osint-investigation/scripts/fetch_wikipedia.py`.

- L45 `_wp_search(query: str, limit: int)` (function)
- L69 `_wp_summary(title: str)` (function) — Pull the REST summary for a title — short bio, image, type.
- L79 `_wd_lookup_by_qid(qid: str)` (function) — Pull common facts for a QID via Wikidata's Action API (no SPARQL).
- L178 `_wd_qid_for_title(title: str)` (function) — Get the Wikidata QID associated with a Wikipedia article title.
- L203 `fetch(query: str, limit: int, no_wikidata: bool, out_path: str)` (function)
- L249 `main()` (function)
