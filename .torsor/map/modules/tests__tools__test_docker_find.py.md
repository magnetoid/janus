---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_docker_find.py

Symbols in `tests/tools/test_docker_find.py`.

- L12 `_reset_cache()` (function) — Clear the module-level docker executable cache between tests.
- L19 `TestFindDocker` (class)
- L20 `test_found_via_shutil_which(self)` (method)
- L25 `test_not_in_path_falls_back_to_known_locations(self, tmp_path)` (method)
- L36 `test_returns_none_when_not_found(self)` (method)
- L42 `test_caches_result(self)` (method)
- L50 `test_env_var_override_takes_precedence(self, tmp_path)` (method) — HERMES_DOCKER_BINARY overrides PATH and known-location discovery.
- L61 `test_env_var_override_ignored_if_not_executable(self, tmp_path)` (method) — Non-executable HERMES_DOCKER_BINARY falls through to normal discovery.
- L72 `test_env_var_override_ignored_if_nonexistent(self)` (method) — Non-existent HERMES_DOCKER_BINARY path falls through.
- L79 `test_podman_on_path_used_when_docker_missing(self)` (method) — When docker is not on PATH, podman is tried next.
- L93 `test_docker_preferred_over_podman(self)` (method) — When both docker and podman are on PATH, docker wins.
