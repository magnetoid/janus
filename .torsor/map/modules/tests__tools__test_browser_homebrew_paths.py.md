---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_homebrew_paths.py

Symbols in `tests/tools/test_browser_homebrew_paths.py`.

- L21 `_clear_browser_caches()` (function) — Clear lru_cache and manual caches between tests.
- L32 `TestSanePath` (class) — Verify _SANE_PATH includes fallback directories used by browser_tool.
- L35 `test_includes_termux_bin(self)` (method)
- L38 `test_includes_termux_sbin(self)` (method)
- L41 `test_includes_homebrew_bin(self)` (method)
- L44 `test_includes_homebrew_sbin(self)` (method)
- L47 `test_includes_standard_dirs(self)` (method)
- L54 `TestDiscoverHomebrewNodeDirs` (class) — Tests for _discover_homebrew_node_dirs().
- L57 `test_returns_empty_when_no_homebrew(self)` (method) — Non-macOS systems without /opt/homebrew/opt should return empty.
- L62 `test_finds_versioned_node_dirs(self)` (method) — Should discover node@20/bin, node@24/bin etc.
- L85 `test_excludes_plain_node(self)` (method) — 'node' (unversioned) should be excluded — covered by /opt/homebrew/bin.
- L92 `test_handles_oserror_gracefully(self)` (method) — Should return empty list if listdir raises OSError.
- L99 `TestFindAgentBrowser` (class) — Tests for _find_agent_browser() Homebrew path search.
- L102 `test_finds_in_current_path(self)` (method) — Should return result from shutil.which if available on current PATH.
- L107 `test_finds_in_homebrew_bin(self)` (method) — Should search Homebrew dirs when not found on current PATH.
- L123 `test_finds_npx_in_homebrew(self)` (method) — Should find npx in Homebrew paths as a fallback.
- L152 `test_finds_npx_in_termux_fallback_path(self)` (method) — Should find npx when only Termux fallback dirs are available.
- L190 `test_raises_when_not_found(self)` (method) — Should raise FileNotFoundError when nothing works.
- L210 `TestBrowserRequirements` (class)
- L211 `test_cdp_override_does_not_require_agent_browser_cli(self, monkeypatch)` (method)
- L218 `test_termux_requires_real_agent_browser_install_not_npx_fallback(self, monkeypatch)` (method)
- L228 `TestRunBrowserCommandTermuxFallback` (class)
- L229 `test_termux_local_mode_rejects_bare_npx_fallback(self, monkeypatch)` (method)
- L242 `TestRunBrowserCommandPathConstruction` (class) — Verify _run_browser_command() includes Homebrew node dirs in subprocess PATH.
- L245 `test_subprocess_preserves_executable_path_with_spaces(self, tmp_path)` (method) — A local agent-browser path containing spaces must stay one argv entry.
- L298 `test_subprocess_splits_npx_fallback_into_command_and_package(self, tmp_path)` (method) — The synthetic npx fallback should still expand into separate argv items.
- L358 `test_subprocess_path_includes_homebrew_node_dirs(self, tmp_path)` (method) — When _discover_homebrew_node_dirs returns dirs, they should appear
- L420 `test_subprocess_path_includes_sane_path_homebrew(self, tmp_path)` (method) — _SANE_PATH Homebrew entries should appear even without versioned node dirs.
- L466 `test_subprocess_path_includes_termux_fallback_dirs(self, tmp_path)` (method) — Termux fallback dirs should survive browser PATH rebuilding.
