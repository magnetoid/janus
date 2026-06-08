---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_docker_exec_privilege_drop.py

Symbols in `tests/docker/test_docker_exec_privilege_drop.py`.

- L37 `_wait_for_init(container: str)` (function) — Block until /init is up enough that `docker exec` is responsive.
- L52 `sleep_container(built_image: str, container_name: str)` (function) — Long-lived container running `sleep infinity` so we can docker exec into it.
- L74 `test_shim_drops_root_to_hermes_uid(sleep_container: str)` (function) — docker exec defaults to root; the shim should drop to uid 10000.
- L117 `test_shim_short_circuits_for_non_root_exec(sleep_container: str)` (function) — docker exec --user hermes already runs as 10000; shim should be a no-op.
- L150 `test_shim_opt_out_keeps_root(sleep_container: str)` (function) — HERMES_DOCKER_EXEC_AS_ROOT=1 should suppress the privilege drop.
- L184 `test_shim_opt_out_strict_truthiness(sleep_container: str, falsy_value: str)` (function) — Anything other than 1/true/yes (case-insensitive) does NOT opt out.
- L219 `test_main_cmd_path_unaffected(built_image: str)` (function) — The CMD path (docker run <image> <args>) must still work.
- L241 `test_e2e_login_then_supervised_gateway_can_read_auth(sleep_container: str)` (function) — End-to-end regression for the original bug.
