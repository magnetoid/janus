---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway_platform_gating.py

Symbols in `tests/hermes_cli/test_gateway_platform_gating.py`.

- L17 `TestMatrixHiddenOnWindows` (class)
- L18 `test_matrix_present_on_linux(self, monkeypatch)` (method) — Sanity: matrix is still in the picker on Linux/macOS.
- L27 `test_matrix_present_on_macos(self, monkeypatch)` (method)
- L35 `test_matrix_hidden_on_windows(self, monkeypatch)` (method) — The actual gate: matrix must NOT appear on Windows.
- L47 `test_other_platforms_unaffected_on_windows(self, monkeypatch)` (method) — Gating must only drop matrix, not collateral damage.
