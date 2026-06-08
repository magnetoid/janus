---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_tui_prebuilt_bundle.py

Symbols in `tests/docker/test_tui_prebuilt_bundle.py`.

- L24 `_exec_py(image: str, py: str)` (function) — Run a Python snippet inside the image as the hermes user, return stdout.
- L42 `test_hermes_tui_dir_env_is_set(built_image: str)` (function) — HERMES_TUI_DIR must point at the prebuilt bundle dir in the image.
- L55 `test_prebuilt_bundle_present_and_no_runtime_install(built_image: str)` (function) — The launcher must (a) find the prebuilt bundle and (b) NOT want an
