---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/kanban_swarm.py

Symbols in `hermes_cli/kanban_swarm.py`.

- L30 `SwarmWorkerSpec` (class) — A single parallel worker card in a swarm.
- L42 `SwarmCreated` (class) — IDs produced by :func:`create_swarm`.
- L50 `as_dict(self)` (method)
- L59 `_require_text(value: str, field_name: str)` (function)
- L66 `_swarm_context(root_id: str, goal: str)` (function)
- L77 `create_swarm(conn: sqlite3.Connection, *, goal: str, workers: Iterable[SwarmWorkerSpec], verifier_assignee: str, synthesizer_assignee: str, root_title: Optional[str]=None, verifier_title: str='Verify swarm outputs', synthesizer_title: str='Synthesize swarm outputs', tenant: Optional[str]=None, created_by: str='swarm-orchestrator', workspace_kind: str='scratch', workspace_path: Optional[str]=None, priority: int=0, idempotency_key: Optional[str]=None)` (function) — Create a durable Kanban swarm graph.
- L226 `post_blackboard_update(conn: sqlite3.Connection, root_id: str, *, author: str, key: str, value: Any)` (function) — Append one structured update to the swarm root blackboard.
- L243 `latest_blackboard(conn: sqlite3.Connection, root_id: str)` (function) — Merge structured blackboard comments on a root card.
- L270 `parse_worker_arg(raw: str)` (function) — Parse CLI ``--worker profile:title[:skill,skill]`` values.
