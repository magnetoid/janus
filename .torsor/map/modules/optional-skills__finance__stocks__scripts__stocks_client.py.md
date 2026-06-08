---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/finance/stocks/scripts/stocks_client.py

Symbols in `optional-skills/finance/stocks/scripts/stocks_client.py`.

- L40 `print_json(data: dict | list)` (function)
- L44 `fmt_price(value)` (function)
- L53 `fmt_large(value)` (function) — Format large numbers with B/T suffix.
- L70 `fmt_pct(value)` (function)
- L79 `safe_get(d: dict, *keys, default=None)` (function) — Safely traverse nested dict.
- L91 `ts_to_date(ts)` (function) — Convert Unix timestamp to ISO date string.
- L106 `_build_request(url: str, headers: dict | None=None)` (function)
- L117 `fetch_url(url: str, headers: dict | None=None, retries: int=MAX_RETRIES)` (function) — Fetch a URL, parse JSON, retry on transient errors.
- L147 `_fetch_crumb()` (function) — Yahoo Finance v8 requires a crumb + consent cookie.
- L179 `yf_url(path: str, params: dict | None=None)` (function) — Build a Yahoo Finance URL, injecting crumb if available.
- L196 `yf_chart(symbol: str, interval: str='1d', range_: str='1d')` (function)
- L211 `yf_search(query: str, count: int=5)` (function)
- L225 `yf_quote_summary(symbol: str)` (function) — Fetch detailed quote summary (quoteSummary) for PE, market cap, etc.
- L246 `av_overview(symbol: str)` (function)
- L264 `extract_quote_from_chart(symbol: str, chart_data: dict)` (function) — Extract current quote info from v8 chart response.
- L311 `extract_quote_summary_fields(qs_data: dict)` (function) — Extract PE, market cap, etc. from quoteSummary response.
- L355 `cmd_quote(symbols: list[str])` (function)
- L410 `cmd_search(query: str)` (function)
- L444 `cmd_history(symbol: str, range_: str='1mo')` (function)
- L526 `cmd_compare(symbols: list[str])` (function)
- L598 `cmd_crypto(symbol: str, vs: str='USD')` (function)
- L673 `build_parser()` (function)
- L728 `main()` (function)
