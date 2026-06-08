---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/entry.py

Symbols in `acp_adapter/entry.py`.

- L46 `_BenignProbeMethodFilter` (class) — Suppress acp 'Background task failed' tracebacks caused by unknown
- L53 `filter(self, record: logging.LogRecord)` (method)
- L75 `_setup_logging()` (function) — Route all logging to stderr so stdout stays clean for ACP stdio.
- L96 `_load_env()` (function) — Load .env from HERMES_HOME (default ``~/.hermes``).
- L111 `_parse_args(argv: list[str] | None=None)` (function)
- L144 `_print_version()` (function)
- L150 `_run_check()` (function)
- L157 `_run_setup()` (function)
- L184 `_run_setup_browser(assume_yes: bool=False)` (function) — Bootstrap agent-browser + Chromium.
- L212 `main(argv: list[str] | None=None)` (function) — Entry point: load env, configure logging, run the ACP agent.
