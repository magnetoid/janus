---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_browser_connect.py

Symbols in `tests/cli/test_cli_browser_connect.py`.

- L18 `_assert_chrome_debug_cmd(cmd, expected_chrome, expected_port)` (function) — Verify the auto-launch command has all required flags.
- L29 `_FakeResponse` (class)
- L32 `__enter__(self)` (method)
- L35 `__exit__(self, exc_type, exc, tb)` (method)
- L39 `TestChromeDebugLaunch` (class)
- L40 `test_browser_debug_ready_requires_http_cdp_endpoint(self)` (method)
- L54 `test_browser_debug_ready_rejects_non_cdp_listener(self)` (method)
- L58 `test_windows_launch_uses_browser_found_on_path(self)` (method)
- L80 `test_windows_launch_falls_back_to_common_install_dirs(self, monkeypatch)` (method)
- L102 `test_manual_command_uses_detected_linux_browser(self)` (method)
- L110 `test_linux_candidates_prefer_chrome_before_brave_when_both_exist(self)` (method)
- L126 `test_linux_candidates_prefer_chrome_install_path_before_brave_on_path(self)` (method)
- L136 `test_windows_candidates_prefer_chrome_install_path_before_brave_on_path(self, monkeypatch)` (method)
- L151 `test_linux_candidates_include_arch_brave_install_path(self)` (method)
- L163 `test_linux_candidates_include_brave_binary_name(self)` (method)
- L175 `test_linux_candidates_include_official_brave_and_edge_stable_paths(self)` (method)
- L185 `test_launch_tries_next_browser_when_first_candidate_fails(self)` (method)
- L202 `test_manual_command_uses_wsl_windows_chrome_when_available(self)` (method)
- L213 `test_manual_command_uses_windows_quoting_on_windows(self)` (method)
- L225 `test_manual_command_returns_none_when_linux_browser_missing(self)` (method)
- L230 `test_connect_context_note_allows_expected_browser_use(self, monkeypatch)` (method) — `/browser connect` is an instruction to use the CDP browser.
