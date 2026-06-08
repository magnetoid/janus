---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_anthropic_model_flow_stale_oauth.py

Symbols in `tests/hermes_cli/test_anthropic_model_flow_stale_oauth.py`.

- L13 `TestStaleOAuthTokenDetection` (class) — Bug 3: stale OAuth token must trigger needs_auth=True in _model_flow_anthropic.
- L16 `test_stale_oauth_token_triggers_reauth(self, tmp_path, monkeypatch, capsys)` (method) — Scenario: ANTHROPIC_TOKEN is an expired OAuth token and there are no
- L67 `test_valid_api_key_skips_stale_check(self, tmp_path, monkeypatch, capsys)` (method) — A non-OAuth ANTHROPIC_API_KEY (regular pay-per-token key) must NOT be
- L104 `test_valid_oauth_token_with_refresh_available_skips_reauth(self, tmp_path, monkeypatch, capsys)` (method) — When ANTHROPIC_TOKEN is OAuth and valid cc_creds with refresh exist,
- L149 `TestStaleOAuthGuardLogic` (class) — Unit-level test of the stale-OAuth detection guard logic.
- L152 `test_stale_oauth_flag_logic_no_cc_creds(self)` (method) — When existing_key is OAuth and cc_available is False,
- L171 `test_stale_oauth_flag_logic_with_valid_cc_creds(self)` (method) — When existing_key is OAuth but cc_available is True (valid creds exist),
- L190 `test_non_oauth_key_not_flagged_as_stale(self)` (method) — Regular ANTHROPIC_API_KEY (non-OAuth) must not be flagged as stale
