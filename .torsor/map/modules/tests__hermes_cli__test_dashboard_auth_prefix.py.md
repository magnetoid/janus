---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_prefix.py

Symbols in `tests/hermes_cli/test_dashboard_auth_prefix.py`.

- L47 `gated_app_proxied()` (function) — web_server.app configured for gated mode with proxy_headers + a
- L76 `gated_app_direct()` (function) — web_server.app configured for gated mode WITHOUT a proxy prefix,
- L104 `TestGateRedirectsCarryPrefix` (class)
- L105 `test_html_redirect_to_login_carries_prefix(self, gated_app_proxied)` (method)
- L119 `test_api_401_envelope_login_url_carries_prefix(self, gated_app_proxied)` (method)
- L133 `test_no_prefix_header_keeps_unprefixed_paths(self, gated_app_direct)` (method) — When no X-Forwarded-Prefix is sent, the Location header must
- L141 `test_malformed_prefix_header_is_ignored(self, gated_app_proxied)` (method) — A hostile proxy injects ``X-Forwarded-Prefix: <script>``;
- L160 `TestOAuthRedirectUriRespectsPrefix` (class)
- L161 `test_redirect_uri_includes_prefix_in_authorize_url(self, gated_app_proxied)` (method) — The IDP returns the user to the redirect_uri we sent. If we
- L192 `test_redirect_uri_no_prefix_when_direct_deploy(self, gated_app_direct)` (method)
- L211 `TestPublicUrlOverride` (class) — ``dashboard.public_url`` (env override:
- L236 `patch_config(self, monkeypatch)` (method) — Replace ``hermes_cli.config.load_config`` with a stub
- L251 `_redirect_uri(self, gated_app, *, headers=None)` (method) — Drive /auth/login and read the redirect_uri the IDP saw.
- L263 `test_public_url_env_overrides_request_reconstruction(self, gated_app_direct, patch_config, monkeypatch)` (method) — ``HERMES_DASHBOARD_PUBLIC_URL`` wins over the URL the
- L279 `test_public_url_config_yaml_used_when_env_unset(self, gated_app_direct, patch_config, monkeypatch)` (method)
- L287 `test_env_overrides_config_public_url(self, gated_app_direct, patch_config, monkeypatch)` (method) — Precedence pin — env wins over config.yaml. Fly.io / CI
- L302 `test_public_url_with_path_prefix_baked_in(self, gated_app_direct, patch_config, monkeypatch)` (method) — When public_url already carries a path prefix
- L316 `test_public_url_ignores_x_forwarded_prefix(self, gated_app_proxied, patch_config, monkeypatch)` (method) — X-Forwarded-Prefix is the auto-reconstruction signal; when
- L338 `test_public_url_strips_trailing_slash(self, gated_app_direct, patch_config, monkeypatch)` (method) — ``https://example.com/`` and ``https://example.com`` must
- L350 `test_malformed_public_url_falls_through_to_reconstruction(self, gated_app_direct, patch_config, monkeypatch)` (method) — Defence against header injection: a public_url that doesn't
- L379 `test_empty_public_url_env_treated_as_unset(self, gated_app_direct, patch_config, monkeypatch)` (method) — Same defensive behaviour as the other env vars in this
- L396 `TestCookiePathRespectsPrefix` (class) — Cookies must use ``Path=<prefix>`` when behind a proxy so they:
- L410 `test_pkce_cookie_uses_prefix_path(self, gated_app_proxied)` (method)
- L426 `test_pkce_cookie_uses_secure_prefix_when_proxied(self, gated_app_proxied)` (method) — Behind a proxy with Path != /, ``__Host-`` is disallowed
- L448 `test_pkce_cookie_uses_host_prefix_when_direct(self, gated_app_direct)` (method) — Fly-direct deploy: Path=/ is available, so we can use the
- L473 `test_loopback_cookies_unprefixed(self)` (method) — Loopback HTTP dev: no Secure, no __Host- / __Secure-.
- L502 `test_cookies_read_back_round_trip_through_prefix(self, gated_app_proxied)` (method) — The end-to-end property: after a successful OAuth round
