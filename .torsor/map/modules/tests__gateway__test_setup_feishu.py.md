---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_setup_feishu.py

Symbols in `tests/gateway/test_setup_feishu.py`.

- L15 `_run_setup_feishu(*, qr_result=None, prompt_yes_no_responses=None, prompt_choice_responses=None, prompt_responses=None, existing_env=None)` (function) — Run _setup_feishu() with mocked I/O and return the env vars that were saved.
- L64 `TestSetupFeishuQrPath` (class) — Tests for the QR scan-to-create happy path.
- L67 `test_qr_success_saves_core_credentials(self)` (method)
- L85 `test_qr_success_does_not_persist_bot_identity(self)` (method) — Bot identity is discovered at runtime by _hydrate_bot_identity — not persisted
- L109 `TestSetupFeishuConnectionMode` (class) — Connection mode: QR always websocket, manual path lets user choose.
- L112 `test_qr_path_defaults_to_websocket(self)` (method)
- L124 `test_manual_path_websocket(self, _mock_probe)` (method)
- L133 `test_manual_path_webhook(self, _mock_probe)` (method)
- L146 `TestSetupFeishuDmPolicy` (class) — DM policy must use platform-scoped FEISHU_ALLOW_ALL_USERS, not the global flag.
- L149 `_run_with_dm_choice(self, dm_choice_idx, prompt_responses=None)` (method)
- L160 `test_pairing_sets_feishu_allow_all_false(self)` (method)
- L166 `test_allow_all_sets_feishu_allow_all_true(self)` (method)
- L172 `test_allowlist_sets_feishu_allow_all_false_with_list(self)` (method)
- L178 `test_allowlist_prepopulates_with_scan_owner_open_id(self)` (method) — When open_id is available from QR scan, it should be the default allowlist value.
- L190 `TestSetupFeishuGroupPolicy` (class)
- L192 `test_open_with_mention(self)` (method)
- L204 `test_disabled(self)` (method)
- L221 `TestSetupFeishuAdapterIntegration` (class) — Verify that env vars written by _setup_feishu() produce a valid adapter config.
- L228 `_make_env_from_setup(self, dm_idx=0, group_idx=0)` (method) — Run _setup_feishu via QR path and return the env vars it would write.
- L245 `test_qr_env_produces_valid_adapter_settings(self)` (method) — QR setup → adapter initializes with websocket mode.
- L259 `test_open_dm_env_sets_correct_adapter_state(self)` (method) — Setup with 'allow all DMs' → adapter sees allow-all flag.
- L271 `test_group_open_env_sets_adapter_group_policy(self)` (method) — Setup with 'open groups' → adapter group_policy is 'open'.
