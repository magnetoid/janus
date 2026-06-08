---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/kanban_specify.py

Symbols in `hermes_cli/kanban_specify.py`.

- L93 `SpecifyOutcome` (class) — Result of specifying a single triage task.
- L102 `_truncate(text: str, limit: int)` (function)
- L111 `_extract_json_blob(raw: str)` (function) — Lenient JSON extraction — tolerates fenced code blocks and
- L132 `_profile_author()` (function) — Mirror of ``hermes_cli.kanban._profile_author``. Kept local to
- L142 `specify_task(task_id: str, *, author: Optional[str]=None, timeout: Optional[int]=None)` (function) — Specify a single triage task and promote it to ``todo``.
- L261 `list_triage_ids(*, tenant: Optional[str]=None)` (function) — Return task ids currently in the triage column.
