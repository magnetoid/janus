---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_mcp_catalog.py

Symbols in `tests/hermes_cli/test_mcp_catalog.py`.

- L23 `_default_mock_probe(monkeypatch)` (function) — By default tests run the probe-fails path so install_entry() doesn't
- L39 `catalog_dir(tmp_path, monkeypatch)` (function) — Provide an isolated optional-mcps/ directory.
- L48 `_isolate_hermes_home(tmp_path, monkeypatch)` (function) — Redirect all config I/O to a temp HERMES_HOME.
- L69 `_write_manifest(catalog_dir: Path, name: str, body: dict)` (function)
- L78 `_basic_manifest(name: str='demo', **overrides)` (function)
- L95 `_entry(name: str)` (function) — Wrapper that asserts entry exists (satisfies type-checker + nicer failure msg).
- L110 `TestManifestParsing` (class)
- L111 `test_minimal_valid(self, catalog_dir)` (method)
- L125 `test_api_key_auth(self, catalog_dir)` (method)
- L146 `test_install_block(self, catalog_dir)` (method)
- L169 `test_invalid_manifest_skipped(self, catalog_dir)` (method)
- L184 `test_missing_transport_command_rejected(self, catalog_dir)` (method)
- L192 `test_get_entry_strips_official_prefix(self, catalog_dir)` (method)
- L206 `TestInstall` (class)
- L207 `test_install_simple_stdio_writes_config(self, catalog_dir)` (method)
- L221 `test_install_with_install_dir_substitution(self, catalog_dir, tmp_path)` (method)
- L252 `test_install_with_api_key_prompts_and_saves(self, catalog_dir, monkeypatch)` (method)
- L273 `test_install_http_oauth_writes_auth_marker(self, catalog_dir)` (method)
- L289 `test_install_required_env_missing_raises(self, catalog_dir, monkeypatch)` (method)
- L313 `TestUninstall` (class)
- L314 `test_uninstall_removes_server_block(self, catalog_dir)` (method)
- L325 `test_uninstall_missing_returns_false(self)` (method)
- L336 `TestPicker` (class)
- L337 `test_show_catalog_empty(self, catalog_dir, capsys)` (method)
- L344 `test_show_catalog_lists_entry(self, catalog_dir, capsys)` (method)
- L353 `test_install_by_name_unknown(self, catalog_dir, capsys)` (method)
- L360 `test_install_by_name_success(self, catalog_dir)` (method)
- L369 `test_run_picker_non_tty_falls_back(self, catalog_dir, capsys, monkeypatch)` (method)
- L386 `TestToolSelection` (class)
- L387 `_make_probed(self, *names)` (method) — Return a list of (tool_name, description) tuples for mocking.
- L391 `test_probe_fail_no_default_writes_no_filter(self, catalog_dir)` (method)
- L402 `test_probe_fail_with_default_applies_directly(self, catalog_dir)` (method)
- L414 `test_probe_success_non_tty_with_default_filters_to_default(self, catalog_dir, monkeypatch)` (method)
- L436 `test_probe_success_non_tty_no_default_clears_filter(self, catalog_dir, monkeypatch)` (method)
- L454 `test_default_enabled_filters_out_unknown_tool_names(self, catalog_dir, monkeypatch)` (method) — If manifest names a tool the server doesn't actually expose, it
- L477 `test_reinstall_preserves_prior_user_selection(self, catalog_dir, monkeypatch)` (method) — Second install of the same entry uses the user's prior
- L508 `test_manifest_invalid_default_enabled_rejected(self, catalog_dir)` (method)
- L525 `TestCatalogDiagnostics` (class)
- L526 `test_future_manifest_version_skipped_with_diagnostic(self, catalog_dir)` (method) — A manifest with a newer manifest_version is skipped, but the skip
- L546 `test_invalid_manifest_diagnostic(self, catalog_dir)` (method)
- L559 `test_picker_surfaces_future_manifest_warning(self, catalog_dir, capsys, monkeypatch)` (method) — The text-dump path should print a warning line for future-manifest
- L582 `TestCustomMcpRows` (class)
- L583 `test_custom_mcp_shown_alongside_catalog(self, catalog_dir, capsys)` (method) — Servers in mcp_servers that aren't in the catalog show up in the
- L604 `test_custom_mcp_only_no_catalog(self, catalog_dir, capsys)` (method) — If the catalog is empty but the user has custom MCPs, they're
- L626 `TestGitInstallShaRef` (class)
- L627 `test_sha_ref_skips_branch_attempt(self, catalog_dir, monkeypatch, tmp_path)` (method) — When install.ref is a SHA-shaped hex string, _do_git_install
- L680 `test_branch_ref_uses_branch_clone(self, catalog_dir, monkeypatch)` (method) — When install.ref is a branch/tag (not SHA-shaped), the fast
- L724 `TestToolsConfigIncludeMode` (class)
- L725 `test_configure_mcp_writes_include_not_exclude(self, monkeypatch, tmp_path)` (method) — `_configure_mcp_tools_interactive` in tools_config.py must write
- L769 `TestShippedCatalog` (class)
- L770 `test_all_shipped_manifests_parse(self, monkeypatch)` (method) — Every manifest in optional-mcps/ must parse cleanly.
