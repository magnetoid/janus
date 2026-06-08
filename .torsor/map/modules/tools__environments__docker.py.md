---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/docker.py

Symbols in `tools/environments/docker.py`.

- L38 `_normalize_forward_env_names(forward_env: list[str] | None)` (function) — Return a deduplicated list of valid environment variable names.
- L63 `_normalize_env_dict(env: dict | None)` (function) — Validate and normalize a docker_env dict to {str: str}.
- L93 `_load_hermes_env_vars()` (function) — Load ~/.hermes/.env values without failing Docker command execution.
- L109 `_sanitize_label_value(value: str)` (function) — Coerce *value* into a Docker label-safe form (alnum + ``_.-``, ≤63 chars).
- L123 `_get_active_profile_name()` (function) — Return the active Hermes profile name, or ``"default"`` on any error.
- L138 `reap_orphan_containers(*, max_age_seconds: int=600, profile_filter: str | None=None, docker_exe: str | None=None)` (function) — Remove stale hermes-tagged containers left behind by prior processes.
- L230 `_container_finished_at(docker_exe: str, container_id: str)` (function) — Parse ``docker inspect`` FinishedAt for *container_id*.
- L264 `find_docker()` (function) — Locate the docker (or podman) CLI binary.
- L352 `_build_security_args(run_as_host_user: bool, run_exec: bool=False)` (function) — Return the security/cap/tmpfs args tailored to the privilege mode.
- L367 `_image_uses_init_entrypoint(docker_exe: str, image: str)` (function) — Return True if ``image``'s entrypoint is the s6-overlay ``/init``.
- L411 `_resolve_host_user_spec()` (function) — Return ``<uid>:<gid>`` for the current host user, or ``None`` on platforms
- L432 `_ensure_docker_available()` (function) — Best-effort check that the docker CLI is available before use.
- L498 `DockerEnvironment` (class) — Hardened Docker container execution with resource limits and persistence.
- L510 `__init__(self, image: str, cwd: str='/root', timeout: int=60, cpu: float=0, memory: int=0, disk: int=0, persistent_filesystem: bool=False, task_id: str='default', volumes: list=None, forward_env: list[str] | None=None, env: dict | None=None, network: bool=True, host_cwd: str=None, auto_mount_cwd: bool=False, run_as_host_user: bool=False, extra_args: list=None, persist_across_processes: bool=True)` (method)
- L903 `_build_init_env_args(self)` (method) — Build -e KEY=VALUE args for injecting host env vars into init_session.
- L935 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method) — Spawn a bash process inside the Docker container.
- L968 `_is_container_gone(self, output: str)` (method) — Return True if the output indicates the container no longer exists.
- L972 `_recreate_container(self)` (method) — Recreate the container after it was removed out-of-band.
- L1052 `execute(self, command: str, cwd: str='', **kwargs)` (method) — Execute a command, auto-recovering from dead containers.
- L1070 `_storage_opt_supported()` (method) — Check if Docker's storage driver supports --storage-opt size=.
- L1109 `_find_reusable_container(self, task_label: str, profile_label: str)` (method) — Look for an existing container labeled for this (task, profile).
- L1166 `cleanup(self, *, force_remove: bool=False)` (method) — Tear down the container according to persist mode and *force_remove*.
- L1283 `wait_for_cleanup(self, timeout: float=30.0)` (method) — Block up to *timeout* seconds for the cleanup worker thread.
