---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_file_safety_container_mirror.py

Symbols in `tests/agent/test_file_safety_container_mirror.py`.

- L15 `TestClassifyContainerMirrorTarget` (class)
- L16 `test_returns_none_without_context(self)` (method) — No Docker context — /root/.hermes/… must not be flagged.
- L22 `test_catches_soul_md_with_context(self)` (method) — Primary failure mode from #32049: agent writes SOUL.md via container path.
- L38 `test_catches_authoritative_profile_files(self, inner)` (method)
- L48 `test_non_hermes_path_not_flagged(self)` (method) — /root/workspace/… is not .hermes state and must not be blocked.
- L61 `TestGetContainerMirrorWarning` (class)
- L62 `test_warning_names_inner_path_and_bypass(self)` (method)
- L74 `TestOrthogonality` (class) — Container-context guard catches what the shape-based guard (#32213) misses.
- L77 `test_inner_container_path_caught_by_context_guard(self)` (method) — No sandboxes/ segment — shape guard passes, context guard blocks.
- L87 `TestFileToolIntegration` (class) — file_tools must catch the mirror path before creating DockerEnvironment.
- L90 `test_guard_uses_current_docker_config_before_env_exists(self, monkeypatch)` (method)
