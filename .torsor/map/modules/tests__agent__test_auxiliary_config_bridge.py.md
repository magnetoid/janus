---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_config_bridge.py

Symbols in `tests/agent/test_auxiliary_config_bridge.py`.

- L16 `_run_auxiliary_bridge(config_dict, monkeypatch)` (function) — Simulate the auxiliary config → env var bridging logic shared by CLI and gateway.
- L71 `TestAuxiliaryConfigBridge` (class) — Verify the config.yaml → env var bridging logic used by CLI and gateway.
- L74 `test_vision_provider_bridged(self, monkeypatch)` (method)
- L86 `test_vision_model_bridged(self, monkeypatch)` (method)
- L97 `test_web_extract_bridged(self, monkeypatch)` (method)
- L107 `test_direct_endpoint_bridged(self, monkeypatch)` (method)
- L122 `test_empty_values_not_bridged(self, monkeypatch)` (method)
- L132 `test_missing_auxiliary_section_safe(self, monkeypatch)` (method) — Config without auxiliary section should not crash.
- L138 `test_non_dict_task_config_ignored(self, monkeypatch)` (method) — Malformed task config (e.g. string instead of dict) is safely ignored.
- L148 `test_mixed_tasks(self, monkeypatch)` (method)
- L161 `test_all_tasks_with_overrides(self, monkeypatch)` (method)
- L174 `test_whitespace_in_values_stripped(self, monkeypatch)` (method)
- L184 `test_empty_auxiliary_dict_safe(self, monkeypatch)` (method)
- L194 `TestGatewayBridgeCodeParity` (class) — Verify the gateway/run.py config bridge contains the auxiliary section.
- L197 `test_gateway_has_auxiliary_bridge(self)` (method) — The gateway config bridge must include auxiliary.* bridging.
- L225 `test_gateway_no_compression_env_bridge(self)` (method) — Gateway should NOT bridge compression config to env vars (config-only).
- L238 `TestVisionModelOverride` (class) — Test that AUXILIARY_VISION_MODEL env var overrides the default model in the handler.
- L241 `test_env_var_overrides_default(self, monkeypatch)` (method)
- L251 `test_default_model_when_no_override(self, monkeypatch)` (method)
- L266 `TestDefaultConfigShape` (class) — Verify the DEFAULT_CONFIG in hermes_cli/config.py has correct auxiliary structure.
- L269 `test_auxiliary_section_exists(self)` (method)
- L273 `test_vision_task_structure(self)` (method)
- L281 `test_web_extract_task_structure(self)` (method)
- L293 `TestCLIDefaultsHaveAuxiliaryKeys` (class) — Verify cli.py load_cli_config() defaults dict does NOT include auxiliary
- L297 `test_cli_defaults_can_merge_auxiliary(self)` (method) — The load_cli_config deep merge logic handles keys not in defaults.
