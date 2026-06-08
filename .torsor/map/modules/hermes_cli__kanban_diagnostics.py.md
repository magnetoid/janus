---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/kanban_diagnostics.py

Symbols in `hermes_cli/kanban_diagnostics.py`.

- L44 `severity_at_or_above(severity: Optional[str], threshold: Optional[str])` (function) — Return True when ``severity`` meets or exceeds ``threshold``.
- L54 `DiagnosticAction` (class) — A single recovery action attached to a diagnostic.
- L79 `to_dict(self)` (method)
- L89 `Diagnostic` (class) — One active distress signal on a task.
- L105 `to_dict(self)` (method)
- L124 `_task_field(task, name, default=None)` (function) — Read a field from a task regardless of representation.
- L148 `_parse_payload(ev)` (function) — Tolerate event.payload being either a dict or a JSON string.
- L163 `_event_kind(ev)` (function)
- L167 `_event_ts(ev)` (function)
- L172 `_active_hallucination_events(events: Iterable[Any], kind: str)` (function) — Return events of ``kind`` that have no ``completed``/``edited``
- L197 `_generic_recovery_actions(task: Any, *, running: bool)` (function)
- L225 `_aux_slot_explicit(slot: Any)` (function) — Return True if the auxiliary slot has user-supplied non-default fields.
- L244 `_main_model_visible(raw_config: Any)` (function) — Best-effort check that a main model is configured.
- L266 `triage_aux_status(config: Optional[dict])` (function) — Inspect raw config and report whether triage paths look configured.
- L317 `_positive_int(value: Any, default: int)` (function)
- L325 `_rule_hallucinated_cards(task, events, runs, now, cfg)` (function) — Blocked-hallucination gate fires: a worker called kanban_complete
- L372 `_rule_triage_aux_unavailable(task, events, runs, now, cfg)` (function) — A triage task cannot leave triage without an auxiliary helper.
- L484 `_rule_prose_phantom_refs(task, events, runs, now, cfg)` (function) — Advisory prose-scan: the completion summary mentions ``t_<hex>``
- L518 `_rule_repeated_failures(task, events, runs, now, cfg)` (function) — Task's unified ``consecutive_failures`` counter is climbing —
- L640 `_rule_repeated_crashes(task, events, runs, now, cfg)` (function) — The worker spawns fine but keeps crashing mid-run. Check the last
- L727 `_rule_stuck_in_blocked(task, events, runs, now, cfg)` (function) — Task has been in ``blocked`` status for too long without a comment.
- L777 `_rule_block_unblock_cycling(task, events, runs, now, cfg)` (function) — Task has cycled through blocked → unblocked many times — the
- L854 `_rule_stranded_in_ready(task, events, runs, now, cfg)` (function) — Task has been in ``ready`` status for too long without any worker
- L1020 `config_from_kanban_config(kanban_cfg: Optional[dict])` (function) — Build diagnostics config from the runtime ``kanban`` config section.
- L1042 `config_from_runtime_config(raw_config: Optional[dict])` (function) — Build diagnostics config from the full Hermes runtime config.
- L1065 `compute_task_diagnostics(task, events: list, runs: list, *, now: Optional[int]=None, config: Optional[dict]=None)` (function) — Run every rule against a single task's state and return a
