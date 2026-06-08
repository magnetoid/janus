---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_tui_backcompat.py

Symbols in `tests/hermes_cli/test_dashboard_tui_backcompat.py`.

- L28 `_run_cli(args, timeout=60)` (function) — Invoke the real hermes_cli.main parser in a subprocess.
- L47 `test_dashboard_tui_flag_is_accepted_not_rejected()` (function) — The exact argv an old desktop app sends must parse without argparse error.
- L61 `test_dashboard_tui_flag_is_hidden_from_help()` (function) — The deprecated shim must not re-advertise a removed feature in --help.
- L72 `test_dashboard_without_tui_still_parses()` (function) — Sanity: the modern (no --tui) invocation is unaffected by the shim.
