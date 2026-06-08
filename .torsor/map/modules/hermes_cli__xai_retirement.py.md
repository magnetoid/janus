---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/xai_retirement.py

Symbols in `hermes_cli/xai_retirement.py`.

- L36 `RetirementIssue` (class) — A reference to a retired xAI model found in a Hermes config.
- L46 `_normalize(model_id: str)` (function) — Strip provider prefix (``x-ai/grok-4`` → ``grok-4``) and lowercase.
- L56 `_looks_like_xai(model_id: Optional[str])` (function)
- L62 `find_retired_xai_refs(config: Dict[str, Any])` (function) — Walk all model slots in a Hermes config and return retirement issues.
- L123 `format_issue(issue: RetirementIssue)` (function) — One-line human-readable rendering of a retirement issue.
- L145 `ApplyResult` (class) — Outcome of an apply_migration call.
- L154 `_walk_to_parent(yaml_doc: Any, dotted_path: str)` (function) — Resolve a dotted slot path to (parent_mapping, leaf_key).
- L171 `apply_migration(config_path: Path, issues: List[RetirementIssue], backup: bool=True)` (function) — Rewrite ``config_path`` in-place so each issue is resolved.
