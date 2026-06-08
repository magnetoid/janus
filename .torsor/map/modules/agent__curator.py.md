---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/curator.py

Symbols in `agent/curator.py`.

- L40 `_strip_aux_credential(value: Any)` (function)
- L47 `_ReviewRuntimeBinding` (class) — Provider/model for the curator review fork plus optional per-slot overrides.
- L66 `_state_file()` (function)
- L70 `_default_state()` (function)
- L82 `load_state()` (function)
- L97 `save_state(data: Dict[str, Any])` (function)
- L118 `set_paused(paused: bool)` (function)
- L124 `is_paused()` (function)
- L132 `_load_config()` (function) — Read curator.* config from ~/.hermes/config.yaml. Tolerates missing file.
- L148 `is_enabled()` (function) — Default ON when no config says otherwise.
- L154 `get_interval_hours()` (function)
- L162 `get_min_idle_hours()` (function)
- L170 `get_stale_after_days()` (function)
- L178 `get_archive_after_days()` (function)
- L186 `get_prune_builtins()` (function) — Whether the curator may prune (archive) bundled built-in skills too.
- L202 `_parse_iso(ts: Optional[str])` (function)
- L211 `should_run_now(now: Optional[datetime]=None)` (function) — Return True if the curator should run immediately.
- L268 `apply_automatic_transitions(now: Optional[datetime]=None)` (function) — Walk every curator-managed skill and move active/stale/archived based on
- L498 `_reports_root()` (function) — Directory where curator run reports are written.
- L520 `_needle_in_path_component(needle: str, path: str)` (function) — Check if *needle* is a complete filename stem or directory name in *path*.
- L538 `_classify_removed_skills(removed: List[str], added: List[str], after_names: Set[str], tool_calls: List[Dict[str, Any]])` (function) — Split ``removed`` into consolidated vs pruned.
- L660 `_parse_structured_summary(llm_final: str)` (function) — Extract the structured YAML block from the curator's final response.
- L741 `_extract_absorbed_into_declarations(tool_calls: List[Dict[str, Any]])` (function) — Walk this run's tool calls and extract model-declared absorption targets.
- L795 `_reconcile_classification(removed: List[str], heuristic: Dict[str, List[Dict[str, Any]]], model_block: Dict[str, List[Dict[str, str]]], destinations: Set[str], absorbed_declarations: Optional[Dict[str, Dict[str, Any]]]=None)` (function) — Merge heuristic (tool-call evidence) with the model's structured block.
- L926 `_build_rename_summary(*, before_names: Set[str], after_report: List[Dict[str, Any]], tool_calls: List[Dict[str, Any]], model_final: str)` (function) — Format the user-visible rename map for a curator run.
- L1016 `_write_run_report(*, started_at: datetime, elapsed_seconds: float, auto_counts: Dict[str, int], auto_summary: str, before_report: List[Dict[str, Any]], before_names: Set[str], after_report: List[Dict[str, Any]], llm_meta: Dict[str, Any])` (function) — Write run.json + REPORT.md under logs/curator/{YYYYMMDD-HHMMSS}/.
- L1208 `_render_report_markdown(p: Dict[str, Any])` (function) — Render the human-readable report.
- L1395 `_render_candidate_list()` (function) — Human/agent-readable list of agent-created skills with usage stats.
- L1415 `run_curator_review(on_summary: Optional[Callable[[str], None]]=None, synchronous: bool=False, dry_run: bool=False)` (function) — Execute a single curator review pass.
- L1619 `_resolve_review_runtime(cfg: Dict[str, Any])` (function) — Resolve provider/model and per-slot credentials for the curator review fork.
- L1665 `_resolve_review_model(cfg: Dict[str, Any])` (function) — Pick (provider, model) for the curator review fork.
- L1684 `_run_llm_review(prompt: str)` (function) — Spawn an AIAgent fork to run the curator review prompt.
- L1825 `maybe_run_curator(*, idle_for_seconds: Optional[float]=None, on_summary: Optional[Callable[[str], None]]=None)` (function) — Best-effort: run a curator pass if all gates pass. Returns the result
