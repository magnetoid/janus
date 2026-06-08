---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_website_policy.py

Symbols in `tests/tools/test_website_policy.py`.

- L12 `test_load_website_blocklist_merges_config_and_shared_file(tmp_path)` (function)
- L44 `test_check_website_access_matches_parent_domain_subdomains(tmp_path)` (function)
- L68 `test_check_website_access_supports_wildcard_subdomains_only(tmp_path)` (function)
- L90 `test_default_config_exposes_website_blocklist_shape()` (function)
- L99 `test_load_website_blocklist_uses_enabled_default_when_section_missing(tmp_path)` (function)
- L108 `test_load_website_blocklist_raises_clean_error_for_invalid_domains_type(tmp_path)` (function)
- L129 `test_load_website_blocklist_raises_clean_error_for_invalid_shared_files_type(tmp_path)` (function)
- L150 `test_load_website_blocklist_raises_clean_error_for_invalid_top_level_config_type(tmp_path)` (function)
- L158 `test_load_website_blocklist_raises_clean_error_for_invalid_security_type(tmp_path)` (function)
- L166 `test_load_website_blocklist_raises_clean_error_for_invalid_website_blocklist_type(tmp_path)` (function)
- L184 `test_load_website_blocklist_raises_clean_error_for_invalid_enabled_type(tmp_path)` (function)
- L204 `test_load_website_blocklist_raises_clean_error_for_malformed_yaml(tmp_path)` (function)
- L212 `test_load_website_blocklist_wraps_shared_file_read_errors(tmp_path, monkeypatch)` (function)
- L244 `test_check_website_access_uses_dynamic_hermes_home(monkeypatch, tmp_path)` (function)
- L276 `test_check_website_access_blocks_scheme_less_urls(tmp_path)` (function)
- L300 `test_browser_navigate_returns_policy_block(monkeypatch)` (function)
- L327 `test_browser_navigate_allows_when_shared_file_missing(monkeypatch, tmp_path)` (function) — Missing shared blocklist files are warned and skipped, not fatal.
- L351 `TestWebToolPolicy` (class) — Tests that exercise web_extract_tool with website-policy gates.
- L363 `_populate_web_registry(self)` (method)
- L370 `test_web_extract_short_circuits_blocked_url(self, monkeypatch)` (method)
- L407 `test_web_extract_blocks_redirected_final_url(self, monkeypatch)` (method)
- L453 `test_check_website_access_fails_open_on_malformed_config(tmp_path, monkeypatch)` (function) — Malformed config with default path should fail open (return None), not crash.
