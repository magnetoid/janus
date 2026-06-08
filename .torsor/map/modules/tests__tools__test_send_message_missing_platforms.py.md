---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_send_message_missing_platforms.py

Symbols in `tests/tools/test_send_message_missing_platforms.py`.

- L22 `_send_mattermost(token, extra, chat_id, message)` (function) — Pre-migration ``(token, extra, chat_id, message)`` shim around the
- L38 `_send_homeassistant(token, extra, chat_id, message)` (function) — Pre-migration ``(token, extra, chat_id, message)`` shim around the
- L51 `_make_aiohttp_resp(status, json_data=None, text_data=None)` (function) — Build a minimal async-context-manager mock for an aiohttp response.
- L60 `_make_aiohttp_session(resp)` (function) — Wrap a response mock in a session mock that supports async-with for post/put.
- L81 `TestSendMattermost` (class)
- L82 `test_success(self)` (method)
- L98 `test_http_error(self)` (method)
- L111 `test_missing_config(self)` (method)
- L118 `test_env_var_fallback(self)` (method)
- L137 `TestSendMatrix` (class)
- L138 `test_success(self)` (method)
- L162 `test_http_error(self)` (method)
- L176 `test_missing_config(self)` (method)
- L183 `test_env_var_fallback(self)` (method)
- L198 `test_txn_id_is_unique_across_calls(self)` (method) — Each call should generate a distinct transaction ID in the URL.
- L234 `TestSendHomeAssistant` (class)
- L235 `test_success(self)` (method)
- L251 `test_http_error(self)` (method)
- L265 `test_missing_config(self)` (method)
- L272 `test_env_var_fallback(self)` (method)
- L290 `TestSendDingtalk` (class)
- L291 `_make_httpx_resp(self, status_code=200, json_data=None)` (method)
- L298 `_make_httpx_client(self, resp)` (method)
- L306 `test_success(self)` (method)
- L320 `test_api_error_in_response_body(self)` (method) — DingTalk always returns HTTP 200 but signals errors via errcode.
- L334 `test_http_error(self)` (method) — If raise_for_status throws, the error is caught and returned.
- L349 `test_http_error_redacts_access_token_in_exception_text(self)` (method)
- L372 `test_missing_config(self)` (method)
- L379 `test_env_var_fallback(self)` (method)
