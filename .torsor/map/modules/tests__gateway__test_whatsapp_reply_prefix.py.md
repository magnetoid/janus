---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_whatsapp_reply_prefix.py

Symbols in `tests/gateway/test_whatsapp_reply_prefix.py`.

- L21 `TestConfigYamlBridging` (class) — Test that whatsapp.reply_prefix in config.yaml flows into PlatformConfig.
- L24 `test_reply_prefix_bridged_from_yaml(self, tmp_path)` (method) — whatsapp.reply_prefix in config.yaml sets PlatformConfig.extra.
- L39 `test_empty_reply_prefix_bridged(self, tmp_path)` (method) — Empty string reply_prefix disables the header.
- L53 `test_no_whatsapp_section_no_extra(self, tmp_path)` (method) — Without whatsapp section, no reply_prefix is set.
- L67 `test_whatsapp_section_without_reply_prefix(self, tmp_path)` (method) — whatsapp section present but without reply_prefix key.
- L86 `TestAdapterInit` (class) — Test that WhatsAppAdapter reads reply_prefix from config.extra.
- L89 `test_reply_prefix_from_extra(self)` (method)
- L95 `test_reply_prefix_default_none(self)` (method)
- L101 `test_reply_prefix_empty_string(self)` (method)
- L113 `TestConfigVersionCoverage` (class) — Ensure _config_version covers all ENV_VARS_BY_VERSION keys.
- L116 `test_default_config_version_covers_env_var_versions(self)` (method) — _config_version must be >= the highest ENV_VARS_BY_VERSION key.
