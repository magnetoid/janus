---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/scripts/check_deps.py

Symbols in `skills/creative/comfyui/scripts/check_deps.py`.

- L123 `fetch_object_info(url: str, headers: dict)` (function) — Returns (installed_node_set, error_info). Error info is a dict if we
- L147 `_fetch_one_folder(base: str, folder: str, headers: dict, *, is_cloud: bool)` (function) — Single-folder fetch, no aliasing. Returns (installed_set, error_info).
- L179 `fetch_models_for_folder(base: str, folder: str, headers: dict, *, is_cloud: bool)` (function) — Fetch installed models for a folder, trying aliases.
- L207 `fetch_embeddings(base: str, headers: dict, *, is_cloud: bool)` (function) — Local ComfyUI exposes /embeddings; cloud uses /experiment/models/embeddings.
- L231 `normalize_for_match(name: str)` (function) — Generate matching variants of a model name (with/without extension, slashes, etc.)
- L244 `model_present(needed: str, installed: set[str])` (function)
- L254 `suggest_install_command(node_class: str)` (function)
- L261 `suggest_git_url(node_class: str)` (function) — For nodes not on the registry, return a git URL the user can hand to
- L267 `check_deps(workflow: dict, host: str, *, api_key: str | None=None)` (function)
- L386 `main(argv: list[str] | None=None)` (function)
