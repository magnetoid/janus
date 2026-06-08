---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_ssrf_local.py

Symbols in `tests/tools/test_browser_ssrf_local.py`.

- L19 `_make_browser_result(url='https://example.com')` (function) — Return a mock successful browser command result.
- L29 `TestPreNavigationSsrf` (class)
- L33 `_common_patches(self, monkeypatch)` (method) — Shared patches for pre-navigation tests that pass the SSRF check.
- L56 `test_cloud_blocks_private_url_by_default(self, monkeypatch, _common_patches)` (method) — SSRF protection blocks private URLs in cloud mode.
- L67 `test_cloud_allows_private_url_when_setting_true(self, monkeypatch, _common_patches)` (method) — Private URLs pass in cloud mode when allow_private_urls is True.
- L77 `test_cloud_allows_public_url(self, monkeypatch, _common_patches)` (method) — Public URLs always pass in cloud mode.
- L89 `test_local_allows_private_url(self, monkeypatch, _common_patches)` (method) — Local backends skip SSRF — private URLs are always allowed.
- L99 `test_local_allows_public_url(self, monkeypatch, _common_patches)` (method) — Local backends pass public URLs too (sanity check).
- L126 `test_cloud_blocks_imds_even_when_routing_to_local_sidecar(self, monkeypatch, _common_patches, imds_url)` (method) — Hybrid routing must not let cloud metadata endpoints through.
- L146 `test_cloud_allows_ordinary_private_url_via_sidecar(self, monkeypatch, _common_patches)` (method) — Hybrid routing still works for ordinary private URLs — floor
- L171 `TestIsLocalBackend` (class)
- L172 `test_camofox_is_local(self, monkeypatch)` (method) — Camofox mode counts as a local backend.
- L179 `test_no_cloud_provider_is_local(self, monkeypatch)` (method) — No cloud provider configured → local backend.
- L186 `test_cloud_provider_is_not_local(self, monkeypatch)` (method) — Cloud provider configured and not Camofox → NOT local.
- L199 `TestPostRedirectSsrf` (class)
- L204 `_common_patches(self, monkeypatch)` (method) — Shared patches for redirect tests.
- L222 `test_cloud_blocks_redirect_to_private(self, monkeypatch, _common_patches)` (method) — Redirects to private addresses are blocked in cloud mode.
- L240 `test_cloud_allows_redirect_to_private_when_setting_true(self, monkeypatch, _common_patches)` (method) — Redirects to private addresses pass in cloud mode with allow_private_urls.
- L260 `test_local_allows_redirect_to_private(self, monkeypatch, _common_patches)` (method) — Redirects to private addresses pass in local mode.
- L278 `test_cloud_allows_redirect_to_public(self, monkeypatch, _common_patches)` (method) — Redirects to public addresses always pass (cloud mode).
- L297 `test_cloud_blocks_redirect_to_imds_even_via_sidecar(self, monkeypatch, _common_patches)` (method) — Redirect to a cloud metadata endpoint is blocked regardless of
- L322 `TestAllowPrivateUrlsConfig` (class)
- L324 `_reset_cache(self)` (method)
- L331 `test_browser_config_string_false_stays_disabled(self, monkeypatch)` (method)
