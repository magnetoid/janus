---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/install.py

Symbols in `agent/lsp/install.py`.

- L114 `_is_windows()` (function)
- L118 `hermes_lsp_bin_dir()` (function) — Return the Hermes-owned bin staging dir for LSP servers.
- L128 `_native_binary_candidates(base: Path)` (function) — Return platform-native executable candidates for a staged binary.
- L142 `_existing_binary(name: str)` (function) — Probe the staging dir + PATH for a binary named ``name``.
- L158 `_get_lock(pkg: str)` (function)
- L167 `try_install(pkg: str, strategy: str='auto')` (function) — Try to install ``pkg`` and return the binary path if successful.
- L198 `_do_install(pkg: str)` (function)
- L231 `_install_npm(pkg: str, bin_name: str, extra_pkgs: Optional[list]=None)` (function) — Install an npm package into our staging dir.
- L295 `_install_go(pkg: str, bin_name: str)` (function) — Install a Go module to GOBIN=<staging>.
- L331 `_install_pip(pkg: str, bin_name: str)` (function) — Install a Python package into a hermes-owned target dir.
- L380 `detect_status(pkg: str)` (function) — Return ``installed``, ``missing``, or ``manual-only`` for a package.
