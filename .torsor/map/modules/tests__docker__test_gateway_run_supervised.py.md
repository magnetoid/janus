---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_gateway_run_supervised.py

Symbols in `tests/docker/test_gateway_run_supervised.py`.

- L29 `_sh(container: str, command: str, timeout: int=30)` (function)
- L33 `_svstat(container: str, slot: str='gateway-default')` (function)
- L38 `_svstat_wants_up(container: str, slot: str='gateway-default')` (function) — See test_profile_gateway._svstat_wants_up for the format rules.
- L49 `test_gateway_run_redirects_to_supervised(built_image: str, container_name: str)` (function) — ``docker run <image> gateway run`` (the historical invocation)
- L122 `test_gateway_run_no_supervise_flag_preserves_legacy_behavior(built_image: str, container_name: str)` (function) — ``docker run <image> gateway run --no-supervise`` opts out of
- L206 `test_gateway_run_no_supervise_env_var(built_image: str, container_name: str)` (function) — Env-var opt-out works identically to the CLI flag.
- L246 `test_supervised_gateway_does_not_recurse(built_image: str, container_name: str)` (function) — The HERMES_S6_SUPERVISED_CHILD sentinel must prevent the
- L305 `test_dashboard_supervised_when_env_set(built_image: str, container_name: str)` (function) — When ``HERMES_DASHBOARD=1`` is set, ``docker run <image> gateway
- L332 `test_supervised_gateway_stdout_reaches_docker_logs(built_image: str, container_name: str)` (function) — The supervised gateway's stdout — including the rich-console
