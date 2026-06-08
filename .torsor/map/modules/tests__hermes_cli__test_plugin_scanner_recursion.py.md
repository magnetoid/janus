---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_plugin_scanner_recursion.py

Symbols in `tests/hermes_cli/test_plugin_scanner_recursion.py`.

- L23 `_write_plugin(root: Path, segments: list[str], *, manifest_extra: Dict[str, Any] | None=None, register_body: str='pass')` (function) — Create a plugin dir at ``root/<segments...>/`` with plugin.yaml + __init__.py.
- L54 `_enable(hermes_home: Path, name: str)` (function) — Append ``name`` to ``plugins.enabled`` in ``<hermes_home>/config.yaml``.
- L73 `TestCategoryNamespaceRecursion` (class)
- L74 `test_category_namespace_discovered(self, tmp_path, monkeypatch)` (method) — ``<root>/image_gen/openai/plugin.yaml`` is discovered with key
- L93 `test_flat_plugin_key_matches_name(self, tmp_path, monkeypatch)` (method) — Flat plugins keep their bare name as the key (back-compat).
- L108 `test_depth_cap_two(self, tmp_path, monkeypatch)` (method) — Plugins nested three levels deep are not discovered.
- L129 `test_category_dir_with_manifest_is_leaf(self, tmp_path, monkeypatch)` (method) — If ``image_gen/plugin.yaml`` exists, ``image_gen`` itself IS the
- L159 `TestKindField` (class)
- L160 `test_default_kind_is_standalone(self, tmp_path, monkeypatch)` (method)
- L172 `test_valid_kinds_parsed(self, kind, tmp_path, monkeypatch)` (method)
- L189 `test_unknown_kind_falls_back_to_standalone(self, tmp_path, monkeypatch, caplog)` (method)
- L212 `TestBackendGate` (class)
- L213 `test_user_backend_still_gated_by_enabled(self, tmp_path, monkeypatch)` (method) — User-installed ``kind: backend`` plugins still require opt-in —
- L234 `test_user_backend_loads_when_enabled(self, tmp_path, monkeypatch)` (method)
- L251 `test_exclusive_kind_skipped(self, tmp_path, monkeypatch)` (method) — ``kind: exclusive`` plugins are recorded but not loaded — the
- L274 `TestBundledBackendAutoLoad` (class)
- L275 `test_bundled_image_gen_openai_autoloads(self, tmp_path, monkeypatch)` (method) — The bundled ``plugins/image_gen/openai/`` plugin loads without
- L294 `TestRegisterImageGenProvider` (class)
- L295 `test_accepts_valid_provider(self, tmp_path, monkeypatch)` (method)
- L334 `test_rejects_non_provider(self, tmp_path, monkeypatch, caplog)` (method)
