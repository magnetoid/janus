---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/research/osint-investigation/scripts/timing_analysis.py

Symbols in `optional-skills/research/osint-investigation/scripts/timing_analysis.py`.

- L30 `parse_date(raw: str)` (function)
- L42 `_read(path: str)` (function)
- L47 `_nearest_distance(donation_date: dt.date, awards: list[dt.date])` (function) — Absolute days to nearest award date.
- L52 `_permute(awards_count: int, donations: list[dt.date], date_min: dt.date, date_max: dt.date, rng: random.Random)` (function) — One permutation: draw uniform random award dates, compute mean nearest-distance.
- L69 `analyze(donations_path: str, donation_date_col: str, donation_amount_col: str, donation_donor_col: str, donation_recipient_col: str, contracts_path: str, contract_date_col: str, contract_vendor_col: str, cross_links_path: str | None, n_permutations: int=1000, min_donations: int=3, p_threshold: float=0.05, seed: int | None=None, out_path: str='timing.json')` (function)
- L205 `main()` (function)
