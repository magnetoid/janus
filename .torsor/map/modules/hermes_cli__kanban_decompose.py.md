---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/kanban_decompose.py

Symbols in `hermes_cli/kanban_decompose.py`.

- L128 `DecomposeOutcome` (class) — Result of decomposing a single triage task.
- L139 `_truncate(text: str, limit: int)` (function)
- L145 `_extract_json_blob(raw: str)` (function)
- L163 `_profile_author()` (function) — Mirror of ``hermes_cli.kanban._profile_author``.
- L172 `_load_config()` (function)
- L180 `_resolve_orchestrator_profile(cfg: dict)` (function) — Resolve which profile owns the root/orchestration task after fan-out.
- L201 `_resolve_default_assignee(cfg: dict)` (function) — Resolve which profile catches child tasks the orchestrator can't route.
- L217 `_build_roster()` (function) — Return (roster_for_prompt, valid_assignee_names).
- L242 `_format_roster(roster: list[dict])` (function)
- L252 `_normalize_assignee_choice(assignee: object, *, default_assignee: str, valid_names: set[str])` (function) — Return a valid assignee, falling back to ``default_assignee``.
- L271 `decompose_task(task_id: str, *, author: Optional[str]=None, timeout: Optional[int]=None)` (function) — Decompose a triage task into a graph of child tasks.
- L468 `list_triage_ids(*, tenant: Optional[str]=None)` (function) — Return task ids currently in the triage column.
