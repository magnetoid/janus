---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_specify.py

Symbols in `tests/hermes_cli/test_kanban_specify.py`.

- L23 `kanban_home(tmp_path, monkeypatch)` (function)
- L32 `_fake_aux_response(content: str)` (function) — Build a minimal object shaped like an OpenAI chat.completions result.
- L44 `_mock_client_returning(content: str)` (function)
- L50 `_patch_aux_client(content: str, *, model: str='test-model')` (function) — Patch get_text_auxiliary_client at its source + at the module that
- L66 `test_extract_json_blob_handles_plain_json()` (function)
- L71 `test_extract_json_blob_handles_fenced_json()` (function)
- L76 `test_extract_json_blob_handles_prose_preamble()` (function)
- L81 `test_extract_json_blob_returns_none_for_unparseable()` (function)
- L91 `test_specify_task_happy_path(kanban_home)` (function)
- L115 `test_specify_task_falls_back_to_body_only_on_bad_json(kanban_home)` (function)
- L134 `test_specify_task_rejects_non_triage_task(kanban_home)` (function)
- L148 `test_specify_task_unknown_id(kanban_home)` (function)
- L157 `test_specify_task_no_aux_client_configured(kanban_home)` (function)
- L174 `test_specify_task_llm_api_error_keeps_task_in_triage(kanban_home)` (function)
- L192 `test_specify_task_empty_llm_response(kanban_home)` (function)
- L205 `test_list_triage_ids(kanban_home)` (function)
- L221 `_run_cli(*argv: str)` (function) — Invoke the `hermes kanban …` argparse surface directly.
- L230 `test_cli_specify_requires_id_or_all(kanban_home, capsys)` (function)
- L237 `test_cli_specify_rejects_both_id_and_all(kanban_home, capsys)` (function)
- L246 `test_cli_specify_single_id_success(kanban_home, capsys)` (function)
- L260 `test_cli_specify_all_success_and_json(kanban_home, capsys)` (function)
- L279 `test_cli_specify_all_empty_triage_column(kanban_home, capsys)` (function)
- L285 `test_cli_specify_all_returns_1_when_every_task_fails(kanban_home, capsys)` (function)
- L299 `test_cli_specify_tenant_filter(kanban_home, capsys)` (function)
- L326 `test_cli_specify_author_passed_through(kanban_home, capsys)` (function)
