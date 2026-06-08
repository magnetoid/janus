---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_install_cua_driver.py

Symbols in `tests/hermes_cli/test_install_cua_driver.py`.

- L23 `TestInstallCuaDriverUpgrade` (class)
- L24 `test_upgrade_on_non_macos_is_silent_noop(self)` (method)
- L32 `test_non_upgrade_on_non_macos_warns(self)` (method)
- L40 `test_upgrade_on_macos_with_binary_runs_installer(self)` (method)
- L57 `test_upgrade_on_macos_without_binary_runs_installer(self)` (method)
- L70 `test_non_upgrade_on_macos_with_binary_skips_install(self)` (method)
- L82 `test_non_upgrade_on_macos_without_binary_runs_installer(self)` (method)
- L95 `TestCheckCuaDriverAssetForArch` (class)
- L96 `test_arm64_always_returns_true(self)` (method)
- L102 `test_x86_64_with_asset_returns_true(self)` (method)
- L121 `test_x86_64_without_asset_returns_false(self)` (method)
- L144 `test_x86_64_api_failure_returns_true(self)` (method) — Network failure should fail open — let the installer handle it.
- L152 `test_fresh_install_x86_64_no_asset_skips_installer(self)` (method) — When the latest release has no Intel asset, skip the installer.
- L176 `test_upgrade_x86_64_no_asset_returns_existing_status(self)` (method) — On upgrade with no Intel asset, return whether binary existed.
