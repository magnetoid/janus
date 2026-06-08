---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_lint_config.py

Symbols in `tests/test_lint_config.py`.

- L33 `_load_pyproject()` (function)
- L38 `TestRuffConfig` (class)
- L39 `test_plw1514_is_in_select_list(self)` (method) — pyproject.toml must keep PLW1514 in [tool.ruff.lint.select].
- L57 `test_preview_mode_enabled(self)` (method) — PLW1514 is a preview rule in ruff 0.15.x — preview=true is
- L70 `TestLintWorkflow` (class)
- L73 `test_workflow_exists(self)` (method)
- L78 `test_workflow_has_blocking_ruff_step(self)` (method) — The workflow must run a blocking ``ruff check .`` step
- L104 `test_workflow_yaml_is_valid(self)` (method) — Workflow file must parse as valid YAML (can't ship a broken
