---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/conftest.py

Symbols in `tests/docker/conftest.py`.

- L27 `_docker_available()` (function) — Return True iff a docker CLI is on PATH and the daemon answers.
- L40 `pytest_collection_modifyitems(config, items)` (function) — Apply docker-suite policy: timeout bump + skip on missing docker.
- L56 `built_image()` (function) — Build the image once per test session.
- L78 `container_name(request)` (function) — Generate a unique container name and ensure cleanup on test exit.
- L108 `docker_exec(container: str, *args: str, user: str='hermes', timeout: int=30, extra_docker_args: tuple[str, ...]=())` (function) — Run a command inside ``container`` as ``user`` (default: hermes).
- L129 `docker_exec_sh(container: str, command: str, *, user: str='hermes', timeout: int=30)` (function) — Run ``sh -c <command>`` inside the container as ``user``.
