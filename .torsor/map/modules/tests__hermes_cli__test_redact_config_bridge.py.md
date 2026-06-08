---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_redact_config_bridge.py

Symbols in `tests/hermes_cli/test_redact_config_bridge.py`.

- L23 `test_redact_secrets_false_in_config_yaml_is_honored(tmp_path)` (function) — Setting `security.redact_secrets: false` in config.yaml must disable
- L75 `test_redact_secrets_default_true_when_unset(tmp_path)` (function) — Without the config key or env var, redaction is ON by default (#17691).
- L115 `test_redact_secrets_true_in_config_yaml_is_honored(tmp_path)` (function) — Setting `security.redact_secrets: true` in config.yaml must enable
- L161 `test_dotenv_redact_secrets_beats_config_yaml(tmp_path)` (function) — .env HERMES_REDACT_SECRETS takes precedence over config.yaml.
