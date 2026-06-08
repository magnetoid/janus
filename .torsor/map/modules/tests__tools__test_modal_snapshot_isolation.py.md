---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_modal_snapshot_isolation.py

Symbols in `tests/tools/test_modal_snapshot_isolation.py`.

- L15 `_load_module(module_name: str, path: Path)` (function)
- L24 `_reset_modules(prefixes: tuple[str, ...])` (function)
- L31 `_restore_tool_modules()` (function)
- L54 `_install_modal_test_modules(tmp_path: Path, *, fail_on_snapshot_ids: set[str] | None=None, snapshot_id: str='im-fresh')` (function)
- L200 `test_modal_environment_migrates_legacy_snapshot_key_and_uses_snapshot_id(tmp_path)` (function)
- L217 `test_modal_environment_prunes_stale_direct_snapshot_and_retries_base_image(tmp_path)` (function)
- L236 `test_modal_environment_cleanup_writes_namespaced_snapshot_key(tmp_path)` (function)
- L247 `test_resolve_modal_image_uses_snapshot_ids_and_registry_images(tmp_path)` (function)
