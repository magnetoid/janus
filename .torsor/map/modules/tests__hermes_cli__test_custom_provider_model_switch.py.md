---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_custom_provider_model_switch.py

Symbols in `tests/hermes_cli/test_custom_provider_model_switch.py`.

- L15 `config_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with a minimal config.
- L32 `TestCustomProviderModelSwitch` (class) — Ensure _model_flow_named_custom always probes and shows menu.
- L35 `test_saved_model_still_probes_endpoint(self, config_home)` (method) — When a model is already saved, the function must still call
- L60 `test_can_switch_to_different_model(self, config_home)` (method) — User selects a different model than the saved one.
- L83 `test_probe_failure_falls_back_to_saved(self, config_home)` (method) — When endpoint probe fails and user presses Enter, saved model is used.
- L106 `test_no_saved_model_still_works(self, config_home)` (method) — First-time flow (no saved model) still works as before.
- L129 `test_api_mode_set_from_provider_info(self, config_home)` (method) — When custom_providers entry has api_mode, it should be applied.
- L159 `test_api_mode_cleared_when_not_specified(self, config_home)` (method) — When custom_providers entry has no api_mode, stale api_mode is removed.
- L186 `test_env_template_api_key_is_preserved_in_model_config(self, config_home, monkeypatch)` (method) — Selecting an env-backed custom provider must not inline the secret.
- L228 `test_key_env_custom_provider_persists_reference_not_secret(self, config_home, monkeypatch)` (method) — key_env custom providers should also avoid writing plaintext keys.
- L264 `test_env_ref_base_url_preserves_api_key_ref_through_picker(self, config_home, monkeypatch)` (method) — Integration regression: when BOTH ``base_url`` and ``api_key`` use
- L329 `test_bare_custom_current_provider_matches_env_base_url_before_first_fallback(self, config_home, monkeypatch)` (method) — `hermes model` must mark the custom provider matching model.base_url
- L390 `test_named_custom_provider_selection_preserves_base_url_env_ref(self, config_home, monkeypatch)` (method) — Selecting an env-backed custom provider should not expand its
- L441 `test_key_env_providers_dict_entry_does_not_add_api_key(self, config_home, monkeypatch)` (method) — Regression for #15803: a ``providers:`` (keyed-schema) entry that
- L515 `test_key_env_providers_dict_preserves_existing_api_key(self, config_home, monkeypatch)` (method) — A ``providers:`` entry that already has an inline ``api_key``
- L568 `TestCustomProviderDiscoverModels` (class) — #18726: honor ``discover_models: false`` in the terminal ``hermes model``
- L573 `test_discover_false_uses_configured_list_and_skips_probe(self, config_home)` (method) — discover_models: false + configured models → no live probe, the
- L596 `test_discover_false_saves_choice_from_configured_list(self, config_home)` (method) — User picks the 2nd configured model; it persists, list-driven.
- L622 `test_default_still_probes_when_discover_unset(self, config_home)` (method) — Default (discover_models unset → True) keeps live-probe behaviour
- L651 `test_probe_empty_falls_back_to_configured_list(self, config_home)` (method) — When discovery is on but the probe returns nothing, fall back to the
- L676 `test_discover_false_string_is_normalised(self, config_home)` (method) — String 'false' (hand-edited configs) disables discovery too.
