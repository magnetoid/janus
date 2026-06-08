---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_stage2_hook_build_tree_chown.py

Symbols in `tests/tools/test_stage2_hook_build_tree_chown.py`.

- L36 `stage2_text()` (function)
- L42 `_build_tree_block(text: str)` (function) — Extract the build-tree chown block: from the `venv_owner=` probe
- L53 `test_build_tree_chown_not_gated_on_hermes_home(stage2_text: str)` (function) — The build-tree chown must NOT live inside the `if [ "$needs_chown" = true ]`
- L65 `_run_build_tree_block(text: str, *, venv_owner: int, hermes_uid: int)` (function) — Run the extracted build-tree block with `stat`, `id`, and `chown`
- L97 `test_chown_fires_when_venv_owner_differs(stage2_text: str)` (function) — The #35027 regression scenario: after a remap $HERMES_HOME already
- L108 `test_chown_skipped_when_venv_already_owned(stage2_text: str)` (function) — Idempotency: once the venv is hermes-owned, the recursive chown is
- L118 `test_chown_skipped_for_default_uid(stage2_text: str)` (function) — No remap: venv owned by the default build UID (10000) and hermes is
