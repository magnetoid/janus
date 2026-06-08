---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_profile_gateway.py

Symbols in `tests/docker/test_profile_gateway.py`.

- L34 `_sh(container: str, command: str, timeout: int=30)` (function)
- L40 `_svstat(container: str)` (function) — Returns the raw s6-svstat output for the test profile's slot.
- L48 `_svstat_wants_up(container: str)` (function) — Read the slot's want-state from s6-svstat output.
- L69 `test_profile_create_then_gateway_start(built_image: str, container_name: str)` (function)
- L112 `test_profile_delete_stops_gateway(built_image: str, container_name: str)` (function) — Deleting a profile should stop its gateway and remove the s6
