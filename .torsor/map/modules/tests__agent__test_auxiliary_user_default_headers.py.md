---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_user_default_headers.py

Symbols in `tests/agent/test_auxiliary_user_default_headers.py`.

- L18 `_isolate(tmp_path, monkeypatch)` (function) — Redirect HERMES_HOME so load_config() reads our test config.yaml.
- L26 `_write_config(tmp_path, config_dict)` (function)
- L31 `TestApplyUserDefaultHeadersHelper` (class) — Direct unit tests for the merge helper.
- L34 `test_user_headers_merged_and_win(self, tmp_path)` (method)
- L43 `test_no_config_is_noop_returns_original(self, tmp_path)` (method)
- L50 `test_none_headers_with_config_creates_dict(self, tmp_path)` (method)
- L58 `test_none_headers_no_config_returns_none(self, tmp_path)` (method)
- L63 `test_none_values_skipped(self, tmp_path)` (method)
- L73 `TestAuxClientHonorsUserDefaultHeaders` (class) — Integration: resolve_provider_client must pass overridden headers to OpenAI.
- L76 `test_custom_provider_overrides_sdk_user_agent(self, tmp_path)` (method) — The #40033 reproduction on the auxiliary path.
- L97 `test_custom_provider_no_override_sends_no_user_agent(self, tmp_path)` (method) — Without config, the aux client injects nothing — SDK defaults apply.
- L115 `test_named_custom_provider_honors_override(self, tmp_path)` (method) — A `custom_providers:` entry's aux calls also honor model.default_headers.
