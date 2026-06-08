---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/managed_tool_gateway.py

Symbols in `tools/managed_tool_gateway.py`.

- L23 `ManagedToolGatewayConfig` (class)
- L30 `auth_json_path()` (function) — Return the Hermes auth store path, respecting HERMES_HOME overrides.
- L35 `_read_nous_provider_state()` (function)
- L52 `_parse_timestamp(value: object)` (function)
- L67 `_access_token_is_expiring(expires_at: object, skew_seconds: int)` (function)
- L75 `peek_nous_access_token()` (function) — Cheap probe for a Nous gateway token without triggering refresh.
- L96 `read_nous_access_token()` (function) — Read a Nous Subscriber OAuth access token from auth store or env override.
- L124 `get_tool_gateway_scheme()` (function) — Return configured shared gateway URL scheme.
- L136 `build_vendor_gateway_url(vendor: str)` (function) — Return the gateway origin for a specific vendor.
- L151 `resolve_managed_tool_gateway(vendor: str, gateway_builder: Optional[Callable[[str], str]]=None, token_reader: Optional[Callable[[], Optional[str]]]=None)` (function) — Resolve shared managed-tool gateway config for a vendor.
- L176 `is_managed_tool_gateway_ready(vendor: str, gateway_builder: Optional[Callable[[str], str]]=None, token_reader: Optional[Callable[[], Optional[str]]]=None)` (function) — Return True when gateway URL and a likely-usable Nous token are present.
