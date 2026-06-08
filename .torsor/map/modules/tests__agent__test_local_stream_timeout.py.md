---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_local_stream_timeout.py

Symbols in `tests/agent/test_local_stream_timeout.py`.

- L16 `TestLocalStreamReadTimeout` (class) — Verify stream read timeout auto-detection logic.
- L29 `test_local_endpoint_bumps_read_timeout(self, base_url)` (method) — Local endpoint + default timeout -> bumps to base_timeout.
- L39 `test_user_override_respected_for_local(self)` (method) — User sets HERMES_STREAM_READ_TIMEOUT -> keep their value even for local.
- L54 `test_remote_endpoint_keeps_default(self, base_url)` (method) — Remote endpoint -> keep 120s default.
- L64 `test_empty_base_url_keeps_default(self)` (method) — No base_url set -> keep 120s default.
- L76 `TestIsLocalEndpoint` (class) — Direct unit tests for is_local_endpoint.
- L88 `test_classic_local_addresses(self, url)` (method)
- L98 `test_container_dns_names(self, url)` (method)
- L107 `test_unqualified_docker_hostnames(self, url)` (method) — Unqualified hostnames (no dots) are local — Docker Compose, /etc/hosts, etc.
- L117 `test_remote_endpoints(self, url)` (method)
- L128 `test_tailscale_cgnat_is_local(self, url)` (method) — Tailscale 100.64.0.0/10 should be treated as local for timeout bumps.
- L138 `test_near_but_not_cgnat_is_remote(self, url)` (method) — Hosts adjacent to but outside 100.64.0.0/10 must not match.
