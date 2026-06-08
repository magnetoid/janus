---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_decompose.py

Symbols in `tests/hermes_cli/test_kanban_decompose.py`.

- L21 `kanban_home(tmp_path, monkeypatch)` (function)
- L30 `_fake_aux_response(content: str)` (function)
- L37 `_mock_client_returning(content: str)` (function)
- L43 `_patch_aux_client(content: str, *, model: str='test-model')` (function)
- L51 `_patch_extra_body()` (function)
- L58 `_patch_list_profiles(names: list[str])` (function) — Pretend the named profiles exist. The decomposer uses
- L77 `test_decompose_with_fanout_creates_children(kanban_home)` (function)
- L115 `test_decompose_fanout_false_assigns_default_when_unassigned(kanban_home)` (function)
- L151 `test_decompose_fanout_false_preserves_existing_assignee(kanban_home)` (function)
- L189 `test_decompose_fanout_false_uses_valid_llm_assignee(kanban_home)` (function)
- L221 `test_decompose_fanout_false_invalid_llm_assignee_uses_default(kanban_home)` (function)
- L253 `test_decompose_unknown_assignee_falls_back_to_default(kanban_home)` (function)
- L295 `test_decompose_handles_malformed_llm_json(kanban_home)` (function)
- L313 `test_decompose_returns_false_when_task_not_triage(kanban_home)` (function)
- L329 `test_decompose_no_aux_client_configured(kanban_home)` (function)
