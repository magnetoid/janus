---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_tools_container_config.py

Symbols in `tests/tools/test_file_tools_container_config.py`.

- L7 `_make_env_config(**overrides)` (function)
- L29 `TestFileToolsContainerConfig` (class)
- L30 `_run(self, env_config, task_id)` (method)
- L43 `test_docker_mount_cwd_to_workspace_passed(self)` (method) — docker_mount_cwd_to_workspace is forwarded to container_config.
- L48 `test_docker_forward_env_passed(self)` (method) — docker_forward_env is forwarded to container_config.
- L53 `test_docker_mount_cwd_defaults_to_false(self)` (method) — docker_mount_cwd_to_workspace defaults to False when absent from config.
- L60 `test_docker_forward_env_defaults_to_empty_list(self)` (method) — docker_forward_env defaults to [] when absent from config.
