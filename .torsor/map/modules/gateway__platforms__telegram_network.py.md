---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/telegram_network.py

Symbols in `gateway/platforms/telegram_network.py`.

- L46 `_resolve_proxy_url(target_hosts=None)` (function)
- L52 `TelegramFallbackTransport` (class) — Retry Telegram Bot API requests via fallback IPs while preserving TLS/SNI.
- L61 `__init__(self, fallback_ips: Iterable[str], **transport_kwargs)` (method)
- L73 `handle_async_request(self, request: httpx.Request)` (method)
- L126 `aclose(self)` (method)
- L132 `_normalize_fallback_ips(values: Iterable[str])` (function)
- L153 `parse_fallback_ip_env(value: str | None)` (function)
- L160 `_resolve_system_dns()` (function) — Return the IPv4 addresses that the OS resolver gives for api.telegram.org.
- L169 `_query_doh_provider(client: httpx.AsyncClient, provider: dict)` (function) — Query one DoH provider and return A-record IPs.
- L195 `discover_fallback_ips()` (function) — Auto-discover Telegram API IPs via DNS-over-HTTPS.
- L242 `_rewrite_request_for_ip(request: httpx.Request, ip: str)` (function)
- L258 `_is_retryable_connect_error(exc: Exception)` (function)
