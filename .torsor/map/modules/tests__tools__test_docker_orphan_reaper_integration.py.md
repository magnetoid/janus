---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_docker_orphan_reaper_integration.py

Symbols in `tests/tools/test_docker_orphan_reaper_integration.py`.

- L19 `_reset_reaper_gate()` (function) — Clear the once-per-process flag between tests.
- L24 `test_maybe_reap_runs_once_per_process(monkeypatch)` (function) — The reaper sweep must run at most once per Python interpreter.
- L47 `test_maybe_reap_respects_disable_flag(monkeypatch)` (function) — ``terminal.docker_orphan_reaper: false`` (via container_config) must
- L68 `test_maybe_reap_doubles_lifetime_for_max_age(monkeypatch)` (function) — The reaper's age threshold is ``2 × lifetime_seconds`` (with a 60s
- L88 `test_maybe_reap_floors_at_60_seconds(monkeypatch)` (function) — A user pinning TERMINAL_LIFETIME_SECONDS=0 (or any value <30) would
- L108 `test_maybe_reap_passes_current_profile_as_filter(monkeypatch)` (function) — The reaper must be scoped to the current Hermes profile — a research
- L128 `test_maybe_reap_swallows_exceptions(monkeypatch)` (function) — A reaper crash (docker daemon down, parse error in helper) must NOT
