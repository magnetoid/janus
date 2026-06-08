---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_project_plugin_rce_bypass.py

Symbols in `tests/hermes_cli/test_project_plugin_rce_bypass.py`.

- L44 `_reset_plugin_cache(monkeypatch)` (function) — The plugin scanner caches its result per-process.  Bust the
- L54 `_write_plugin_manifest(root: Path, name: str, manifest: dict)` (function) — Drop a manifest under ``root/<name>/dashboard/manifest.json`` and
- L68 `TestProjectPluginsEnvGate` (class) — Project plugins must only be discovered when the env var is set
- L74 `project_plugin(self, tmp_path, monkeypatch)` (method) — Plant a project-source plugin under CWD's ``.hermes/plugins``
- L94 `test_falsy_values_keep_project_plugins_disabled(self, project_plugin, monkeypatch, value)` (method)
- L110 `test_truthy_values_enable_project_plugins(self, project_plugin, monkeypatch, value)` (method)
- L125 `TestApiPathSanitizer` (class) — Unit-level coverage for the new ``_safe_plugin_api_relpath``
- L130 `_dashboard_dir(self, tmp_path)` (method)
- L135 `test_simple_relative_path_accepted(self, tmp_path)` (method)
- L140 `test_nested_relative_path_accepted(self, tmp_path)` (method)
- L155 `test_absolute_path_rejected(self, tmp_path, payload)` (method)
- L165 `test_traversal_rejected(self, tmp_path, payload)` (method)
- L170 `test_non_string_or_empty_rejected(self, tmp_path, payload)` (method)
- L180 `TestDiscoveryScrubsApiField` (class) — The cached plugin entry must NEVER carry an unsanitised api path.
- L186 `user_plugin_factory(self, tmp_path, monkeypatch)` (method)
- L195 `test_absolute_api_path_in_manifest_is_scrubbed(self, user_plugin_factory)` (method)
- L207 `test_traversal_api_path_in_manifest_is_scrubbed(self, user_plugin_factory)` (method)
- L219 `test_safe_api_path_survives(self, user_plugin_factory, tmp_path)` (method)
- L242 `TestMountApiRoutesRefusesUntrusted` (class) — The mount routine is the actual ``importlib`` call site — these
- L247 `_payload_plugin(self, tmp_path, *, source: str, api_file: str='api.py')` (method)
- L269 `test_project_source_api_is_not_imported(self, tmp_path)` (method)
- L279 `test_bundled_source_api_imports_normally(self, tmp_path)` (method)
- L291 `test_traversal_api_caught_at_mount_time(self, tmp_path)` (method) — Defence-in-depth: if discovery is bypassed (e.g. cache
- L308 `TestEndToEndPocBlocked` (class) — Reproduces the original advisory PoC shape: untrusted CWD with a
- L317 `test_full_chain_blocked(self, tmp_path, monkeypatch)` (method)
