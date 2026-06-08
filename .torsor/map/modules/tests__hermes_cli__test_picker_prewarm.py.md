---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_picker_prewarm.py

Symbols in `tests/hermes_cli/test_picker_prewarm.py`.

- L17 `_reset_guard()` (function)
- L21 `test_prewarm_runs_list_authenticated_providers_once()` (function) — First call spawns a thread that calls list_authenticated_providers;
- L34 `test_prewarm_guard_is_once_per_process()` (function) — The process-level Event guard must make repeat calls no-ops so a
- L48 `test_prewarm_never_raises_on_failure()` (function) — A failing/offline provider path must be fully swallowed — the prewarm
