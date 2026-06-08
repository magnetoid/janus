---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_cli_dispatch_passthrough.py

Symbols in `tests/hermes_cli/test_kanban_cli_dispatch_passthrough.py`.

- L21 `isolated_kanban_home(monkeypatch)` (function) — Spin up a fresh HERMES_HOME with a clean kanban DB.
- L32 `test_cli_dispatch_passes_max_in_progress_from_config(isolated_kanban_home, monkeypatch)` (function) — #33488: hermes kanban dispatch must pass kanban.max_in_progress from
- L74 `test_cli_max_flag_overrides_config_max_spawn(isolated_kanban_home, monkeypatch)` (function) — --max on the CLI takes precedence over kanban.max_spawn in config.
- L97 `test_cli_invalid_max_in_progress_silently_disables(isolated_kanban_home, monkeypatch)` (function) — Invalid kanban.max_in_progress values (0, negative, non-int) should
- L119 `test_kanban_swarm_uses_existing_humanizer_skill()` (function) — #29415: kanban_swarm.py used to hardcode skills=['avoid-ai-writing'],
