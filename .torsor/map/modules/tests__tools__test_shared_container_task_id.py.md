---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_shared_container_task_id.py

Symbols in `tests/tools/test_shared_container_task_id.py`.

- L24 `_clean_overrides()` (function) — Ensure no stray overrides from other tests leak in.
- L33 `test_none_task_id_maps_to_default()` (function)
- L37 `test_empty_task_id_maps_to_default()` (function)
- L41 `test_literal_default_stays_default()` (function)
- L45 `test_subagent_task_id_collapses_to_default()` (function)
- L52 `test_arbitrary_session_id_collapses_to_default()` (function)
- L57 `test_rl_task_with_override_keeps_its_own_id()` (function)
- L73 `test_cleared_override_collapses_again()` (function)
- L80 `test_get_active_env_reads_shared_container_from_subagent_id()` (function) — ``get_active_env`` must see the shared ``"default"`` sandbox when
- L94 `test_get_active_env_honours_rl_override()` (function)
