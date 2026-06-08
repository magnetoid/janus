---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_dockerfile_pid1_reaping.py

Symbols in `tests/tools/test_dockerfile_pid1_reaping.py`.

- L49 `dockerfile_text()` (function)
- L55 `_dockerfile_instructions(dockerfile_text: str)` (function)
- L73 `_run_steps(dockerfile_text: str)` (function)
- L81 `_instruction_text(dockerfile_text: str)` (function) — Join every non-comment Dockerfile instruction into one searchable
- L90 `test_dockerfile_installs_an_init_for_zombie_reaping(dockerfile_text)` (function) — Some init (tini, dumb-init, catatonit, s6-overlay) must be installed.
- L115 `test_dockerfile_entrypoint_routes_through_the_init(dockerfile_text)` (function) — The ENTRYPOINT must invoke the init, not the entrypoint script directly.
- L143 `test_dockerfile_installs_tui_dependencies(dockerfile_text)` (function)
- L161 `test_dockerfile_preinstalls_gateway_messaging_dependencies(dockerfile_text)` (function)
- L175 `test_dockerfile_preinstalls_hindsight_memory_dependency(dockerfile_text)` (function)
- L192 `test_dockerfile_builds_tui_assets(dockerfile_text)` (function)
- L199 `test_dockerfile_materializes_local_tui_ink_package(dockerfile_text)` (function)
- L214 `test_dockerignore_excludes_nested_dependency_dirs()` (function)
