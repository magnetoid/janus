---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_aux_config.py

Symbols in `tests/hermes_cli/test_aux_config.py`.

- L29 `test_title_generation_present_in_default_config()` (function) — `title_generation` task must be defined in DEFAULT_CONFIG.
- L45 `test_session_search_no_longer_appears_in_auxiliary_model_config()` (function) — session_search is a direct DB-backed tool, not an auxiliary LLM task.
- L51 `test_aux_tasks_keys_all_exist_in_default_config()` (function) — Every task the menu offers must be defined in DEFAULT_CONFIG.
- L91 `test_format_aux_current(task_cfg, expected)` (function)
- L95 `test_format_aux_current_handles_non_dict()` (function)
- L103 `test_save_aux_choice_persists_to_config_yaml(tmp_path, monkeypatch)` (function) — Saving a task writes provider/model/base_url/api_key to auxiliary.<task>.
- L121 `test_save_aux_choice_preserves_timeout(tmp_path, monkeypatch)` (function) — Saving must NOT clobber user-tuned timeout values.
- L140 `test_save_aux_choice_does_not_touch_main_model(tmp_path, monkeypatch)` (function) — Aux config must never mutate model.default / model.provider / model.base_url.
- L174 `test_save_aux_choice_creates_missing_task_entry(tmp_path, monkeypatch)` (function) — Saving a task that was wiped from config.yaml should recreate it.
- L197 `test_reset_aux_to_auto_clears_routing_preserves_timeouts(tmp_path, monkeypatch)` (function)
- L228 `test_reset_aux_to_auto_idempotent(tmp_path, monkeypatch)` (function) — Second reset on already-auto config returns 0 without errors.
- L244 `test_select_provider_and_model_dispatches_to_aux_menu(tmp_path, monkeypatch)` (function) — Picking 'Configure auxiliary models...' in the provider list calls _aux_config_menu.
- L274 `test_leave_unchanged_replaces_cancel_label(tmp_path, monkeypatch)` (function) — The bottom cancel entry now reads 'Leave unchanged' (UX polish).
