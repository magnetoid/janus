---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/profile-tui.py

Symbols in `scripts/profile-tui.py`.

- L65 `pick_longest_session(db: Path)` (function)
- L76 `drain(fd: int, timeout: float)` (function) — Read whatever's available from fd within `timeout`, then return.
- L94 `hold_key(fd: int, seq: bytes, seconds: float, rate_hz: int)` (function) — Write `seq` to fd at ~rate_hz for `seconds`. Returns keystrokes sent.
- L111 `summarize(log: Path, since_ts_ms: int)` (function) — Parse perf.log, keep only events newer than since_ts_ms, return stats.
- L139 `pct(values: list[float], p: float)` (function)
- L147 `format_report(data: dict[str, Any])` (function)
- L287 `key_metrics(data: dict[str, Any])` (function) — Flatten the report into a dict of scalar metrics for A/B diffing.
- L357 `format_diff(before: dict[str, float], after: dict[str, float])` (function) — Render a side-by-side A/B comparison table.
- L405 `run_once(args: argparse.Namespace)` (function)
- L476 `main()` (function)
- L528 `loop_mode(args: argparse.Namespace)` (function) — Watch source files, rebuild, rerun, print A/B diff against previous run.
- L605 `wait_for_change(prev: dict[str, float], collect)` (function) — Poll every 1s until a watched file's mtime changes. Debounced 500ms.
