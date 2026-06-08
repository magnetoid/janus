---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_setup_model_provider.py

Symbols in `tests/hermes_cli/test_setup_model_provider.py`.

- L15 `_maybe_keep_current_tts(question, choices)` (function)
- L22 `_clear_provider_env(monkeypatch)` (function)
- L40 `_stub_tts(monkeypatch)` (function)
- L48 `_write_model_config(provider, base_url='', model_name='test-model')` (function) — Simulate what a _model_flow_* function writes to disk.
- L66 `_write_aux_config(task='compression', provider='gemini', model_name='gemini-2.5-flash')` (function) — Simulate the aux picker writing a task override to disk.
- L76 `test_setup_model_provider_preserves_auxiliary_choices_written_by_picker(tmp_path, monkeypatch)` (function) — Aux choices made inside hermes setup must survive the wizard's final save.
- L98 `test_setup_keep_current_custom_from_config_does_not_fall_through(tmp_path, monkeypatch)` (function) — Keep-current custom should not fall through to the generic model menu.
- L124 `test_setup_keep_current_config_provider_uses_provider_specific_model_menu(tmp_path, monkeypatch)` (function) — Keeping current provider preserves the config on disk.
- L149 `test_setup_copilot_acp_skips_same_provider_pool_step(tmp_path, monkeypatch)` (function)
- L183 `test_setup_copilot_uses_gh_auth_and_saves_provider(tmp_path, monkeypatch)` (function) — Copilot provider saves correctly through delegation.
- L204 `test_setup_copilot_acp_uses_model_picker_and_saves_provider(tmp_path, monkeypatch)` (function) — Copilot ACP provider saves correctly through delegation.
- L225 `test_setup_switch_custom_to_codex_clears_custom_endpoint_and_updates_config(tmp_path, monkeypatch)` (function) — Switching from custom to codex updates config correctly.
- L253 `test_setup_switch_preserves_non_model_config(tmp_path, monkeypatch)` (function) — Provider switch preserves other config sections (terminal, display, etc.).
- L278 `test_setup_summary_marks_anthropic_auth_as_vision_available(tmp_path, monkeypatch, capsys)` (function)
- L292 `test_setup_summary_shows_camofox_when_browser_feature_is_camofox(tmp_path, monkeypatch, capsys)` (function)
- L319 `test_setup_summary_does_not_mark_incomplete_browserbase_as_available(tmp_path, monkeypatch, capsys)` (function)
- L349 `test_setup_summary_local_browser_unavailable_without_chromium(tmp_path, monkeypatch, capsys)` (function) — End-to-end: agent-browser present but no Chromium in local mode must
