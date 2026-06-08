---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_hybrid_routing.py

Symbols in `tests/tools/test_browser_hybrid_routing.py`.

- L21 `_reset_routing_state(monkeypatch)` (function) — Clear module-level caches so each test starts clean.
- L36 `TestNavigationSessionKey` (class) — Tests for _navigation_session_key URL-based routing decisions.
- L39 `test_public_url_uses_bare_task_id(self, monkeypatch)` (method) — Public URL with cloud provider configured → bare task_id (cloud).
- L45 `test_localhost_routes_to_local_sidecar(self, monkeypatch)` (method) — ``localhost`` URL → ``::local`` suffix when cloud configured + flag on.
- L51 `test_loopback_ipv4_routes_to_local_sidecar(self, monkeypatch)` (method)
- L56 `test_rfc1918_lan_routes_to_local_sidecar(self, monkeypatch)` (method)
- L61 `test_ipv6_loopback_routes_to_local_sidecar(self, monkeypatch)` (method)
- L66 `test_public_ip_literal_uses_bare_task_id(self, monkeypatch)` (method)
- L71 `test_mdns_local_hostname_routes_to_sidecar(self, monkeypatch)` (method) — ``*.local`` mDNS / ``*.lan`` / ``*.internal`` hostnames route to sidecar.
- L78 `test_no_cloud_provider_stays_on_bare_task_id(self, monkeypatch)` (method) — When cloud provider is not configured, no hybrid routing happens.
- L84 `test_camofox_mode_stays_on_bare_task_id(self, monkeypatch)` (method) — Camofox is already local — no hybrid routing needed.
- L91 `test_cdp_override_stays_on_bare_task_id(self, monkeypatch)` (method) — A user-supplied CDP endpoint owns the whole session — no hybrid.
- L98 `test_feature_flag_off_disables_hybrid_routing(self, monkeypatch)` (method) — ``auto_local_for_private_urls: false`` keeps private URLs on cloud.
- L105 `test_none_task_id_defaults(self, monkeypatch)` (method) — ``None`` task_id resolves to 'default'.
- L112 `TestSessionKeyHelpers` (class)
- L113 `test_is_local_sidecar_key(self)` (method)
- L119 `test_last_session_key_falls_back_to_task_id(self, monkeypatch)` (method) — Without a recorded last-active key, returns the bare task_id.
- L126 `test_last_session_key_returns_recorded_key(self, monkeypatch)` (method)
- L138 `TestHybridRoutingSessionCreation` (class) — _get_session_info must force a local session when the key carries ``::local``.
- L141 `test_local_sidecar_key_skips_cloud_provider(self, monkeypatch)` (method) — A ``::local``-suffixed key creates a local session even when cloud is set.
- L159 `test_bare_task_id_with_cloud_provider_uses_cloud(self, monkeypatch)` (method) — A bare task_id with cloud provider configured hits the cloud path.
- L177 `TestCleanupHybridSessions` (class) — cleanup_browser(bare_task_id) must reap both cloud + local sidecar sessions.
- L180 `test_cleanup_reaps_both_primary_and_sidecar(self, monkeypatch)` (method) — Given a bare task_id with both sessions alive, both get cleaned.
- L206 `test_cleanup_reaps_only_primary_when_no_sidecar(self, monkeypatch)` (method) — When no sidecar exists, only the primary is reaped.
- L224 `test_cleanup_sidecar_directly_keeps_primary(self, monkeypatch)` (method) — Calling cleanup with a ``::local`` key reaps only the sidecar.
