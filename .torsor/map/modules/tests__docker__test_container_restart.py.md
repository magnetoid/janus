---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_container_restart.py

Symbols in `tests/docker/test_container_restart.py`.

- L27 `_docker(*args: str, **kw)` (function)
- L35 `_exec(container: str, *args: str, timeout: int=30)` (function)
- L39 `_sh(container: str, cmd: str, timeout: int=30)` (function)
- L43 `_wait_for_path(container: str, path: str, *, kind: str='f', deadline_s: float=30.0, interval_s: float=0.25)` (function) — Poll `test -<kind> <path>` inside container until success or timeout.
- L71 `_wait_for_reconcile_log_mention(container: str, profile: str, *, deadline_s: float=30.0, interval_s: float=0.25)` (function) — Poll until /opt/data/logs/container-boot.log mentions `profile`.
- L99 `restart_container(request, built_image: str)` (function) — A long-running container with a named volume so docker restart
- L142 `test_running_gateway_survives_container_restart(restart_container: str)` (function)
- L197 `test_stopped_gateway_stays_stopped_after_restart(restart_container: str)` (function)
- L225 `test_stale_gateway_pid_cleaned_up_on_restart(restart_container: str)` (function) — A dead container's gateway.pid + processes.json must NOT
