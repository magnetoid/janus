---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/research/polymarket/scripts/polymarket.py

Symbols in `skills/research/polymarket/scripts/polymarket.py`.

- L26 `_get(url: str)` (function) — GET request, return parsed JSON.
- L40 `_parse_json_field(val)` (function) — Parse double-encoded JSON fields (outcomePrices, outcomes, clobTokenIds).
- L50 `_fmt_pct(price_str: str)` (function) — Format price string as percentage.
- L58 `_fmt_volume(vol)` (function) — Format volume as human-readable.
- L71 `_print_market(m: dict, indent: str='')` (function) — Print a market summary.
- L96 `cmd_search(query: str)` (function) — Search for markets.
- L114 `cmd_trending(limit: int=10)` (function) — Show trending events by volume.
- L130 `cmd_market(slug: str)` (function) — Get market details by slug.
- L152 `cmd_event(slug: str)` (function) — Get event details by slug.
- L168 `cmd_price(token_id: str)` (function) — Get current price for a token.
- L179 `cmd_book(token_id: str)` (function) — Get orderbook for a token.
- L198 `cmd_history(condition_id: str, interval: str='all', fidelity: int=50)` (function) — Get price history for a market.
- L214 `cmd_trades(limit: int=10, market: str=None)` (function) — Get recent trades.
- L234 `main()` (function)
