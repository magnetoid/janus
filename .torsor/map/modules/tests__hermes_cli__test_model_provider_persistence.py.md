---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_provider_persistence.py

Symbols in `tests/hermes_cli/test_model_provider_persistence.py`.

- L15 `config_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with a minimal string-format config.
- L39 `TestSaveModelChoiceAlwaysDict` (class)
- L40 `test_string_model_becomes_dict(self, config_home)` (method) — When config.model is a plain string, _save_model_choice must
- L55 `test_dict_model_stays_dict(self, config_home)` (method) — When config.model is already a dict, _save_model_choice preserves it.
- L72 `TestProviderPersistsAfterModelSave` (class)
- L73 `test_update_config_for_provider_uses_atomic_yaml_write(self, config_home)` (method) — Provider switches should delegate config writes to atomic_yaml_write.
- L99 `test_api_key_provider_saved_when_model_was_string(self, config_home, monkeypatch)` (method) — _model_flow_api_key_provider must persist the provider even when
- L130 `test_copilot_provider_saved_when_selected(self, config_home)` (method) — _model_flow_copilot should persist provider/base_url/model together.
- L179 `test_named_custom_provider_preserves_explicit_api_mode(self, config_home)` (method) — Named custom providers should re-activate with their saved api_mode.
- L210 `test_copilot_acp_provider_saved_when_selected(self, config_home)` (method) — _model_flow_copilot_acp should persist provider/base_url/model together.
- L272 `test_opencode_go_models_are_selectable_and_persist_normalized(self, config_home, monkeypatch)` (method)
- L292 `test_opencode_go_same_provider_switch_recomputes_api_mode(self, config_home, monkeypatch)` (method)
- L321 `TestBaseUrlValidation` (class) — Reject non-URL values in the base URL prompt (e.g. shell commands).
- L324 `test_invalid_base_url_rejected(self, config_home, monkeypatch, capsys)` (method) — Typing a non-URL string should not be saved as the base URL.
- L350 `test_valid_base_url_accepted(self, config_home, monkeypatch)` (method) — A proper URL should be saved normally.
- L371 `test_empty_base_url_keeps_default(self, config_home, monkeypatch)` (method) — Pressing Enter (empty) should not change the base URL.
