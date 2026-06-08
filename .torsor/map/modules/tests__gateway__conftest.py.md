---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/conftest.py

Symbols in `tests/gateway/conftest.py`.

- L42 `_ensure_telegram_mock()` (function) — Install a comprehensive telegram mock in sys.modules.
- L86 `_ensure_discord_mock()` (function) — Install a comprehensive discord mock in sys.modules.
- L246 `_scan_for_plugin_adapter_antipattern(source: str)` (function) — Return a list of offending-line descriptions, or [] if clean.
- L316 `_fingerprint_gateway_tests()` (function) — Return a short fingerprint that changes when any gateway test file changes.
- L335 `_run_adapter_antipattern_scan()` (function) — Scan gateway test files for the plugin-adapter anti-pattern.
- L368 `pytest_configure(config)` (function) — Reject plugin-adapter tests that use the sys.path anti-pattern.
