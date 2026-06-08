---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/account_usage.py

Symbols in `agent/account_usage.py`.

- L21 `_utc_now()` (function)
- L26 `AccountUsageWindow` (class)
- L34 `AccountUsageSnapshot` (class)
- L45 `available(self)` (method)
- L49 `_title_case_slug(value: Optional[str])` (function)
- L56 `_parse_dt(value: Any)` (function)
- L75 `_format_reset(dt: Optional[datetime])` (function)
- L95 `render_account_usage_lines(snapshot: Optional[AccountUsageSnapshot], *, markdown: bool=False)` (function)
- L123 `_fmt_usd(d: float)` (function)
- L127 `_is_finite_num(v: Any)` (function) — True iff v is a real numeric value (int or float, not bool, not NaN/Inf).
- L137 `build_nous_credits_snapshot(account_info)` (function) — Map a NousPortalAccountInfo into an AccountUsageSnapshot for /usage.
- L232 `nous_credits_lines(*, markdown: bool=False, timeout: float=10.0)` (function) — Return rendered Nous-credits /usage lines, or [] when there's nothing to show.
- L282 `_snapshot_from_credits_state(state)` (function) — Map a header-shaped CreditsState (e.g. a dev fixture) to the /usage snapshot.
- L340 `_resolve_codex_usage_url(base_url: str)` (function)
- L351 `_fetch_codex_account_usage()` (function)
- L399 `_fetch_anthropic_account_usage()` (function)
- L460 `_fetch_openrouter_account_usage(base_url: Optional[str], api_key: Optional[str])` (function)
- L532 `fetch_account_usage(provider: Optional[str], *, base_url: Optional[str]=None, api_key: Optional[str]=None)` (function)
