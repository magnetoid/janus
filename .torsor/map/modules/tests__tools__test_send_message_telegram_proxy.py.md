---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_send_message_telegram_proxy.py

Symbols in `tests/tools/test_send_message_telegram_proxy.py`.

- L26 `_install_telegram_mock_with_request(monkeypatch: pytest.MonkeyPatch, bot_factory: MagicMock, httpx_request_factory: MagicMock)` (function) — Install a stub ``telegram`` package whose ``Bot`` and
- L53 `_make_bot()` (function)
- L59 `TestSendTelegramStandaloneProxy` (class) — The standalone ``_send_telegram`` path must route through
- L65 `test_proxy_env_passed_to_httpx_request(self, monkeypatch: pytest.MonkeyPatch)` (method) — With TELEGRAM_PROXY set, Bot() is constructed with HTTPXRequest
- L112 `test_no_proxy_env_uses_plain_bot(self, monkeypatch: pytest.MonkeyPatch)` (method) — Without TELEGRAM_PROXY (and no inherited HTTPS_PROXY/etc), Bot()
