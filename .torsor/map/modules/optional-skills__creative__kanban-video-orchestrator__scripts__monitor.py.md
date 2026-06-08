---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/creative/kanban-video-orchestrator/scripts/monitor.py

Symbols in `optional-skills/creative/kanban-video-orchestrator/scripts/monitor.py`.

- L29 `hermes_available()` (function)
- L33 `kanban_list(tenant: str)` (function) — Returns parsed task rows. Falls back to plain stdout parsing if JSON
- L69 `kanban_show(task_id: str)` (function)
- L82 `detect_issues(tasks: list[dict])` (function) — Return a list of issue strings, one per concern.
- L134 `snapshot(tenant: str)` (function)
- L140 `print_snapshot(tasks: list[dict], issues: list[str])` (function)
- L163 `main()` (function)
