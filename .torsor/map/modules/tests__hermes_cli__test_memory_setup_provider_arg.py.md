---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_memory_setup_provider_arg.py

Symbols in `tests/hermes_cli/test_memory_setup_provider_arg.py`.

- L16 `TestMemorySetupProviderRouting` (class)
- L17 `test_setup_with_provider_arg_skips_picker(self)` (method) — `memory setup honcho` routes straight to cmd_setup_provider.
- L26 `test_setup_without_provider_runs_picker(self)` (method) — `memory setup` (no provider) runs the interactive picker.
- L35 `test_setup_with_missing_provider_attr_runs_picker(self)` (method) — A SimpleNamespace lacking `provider` must not crash — fall back to picker.
- L44 `test_unknown_provider_reports_and_returns_early(self, capsys)` (method) — An unknown provider name surfaces a helpful message and returns
- L53 `TestInstallDependenciesRunner` (class) — `_install_dependencies` must install via `uv` when present and fall back
- L58 `_run_with_missing_dep(self, tmp_path, which_side_effect)` (method) — Drive _install_dependencies for a plugin that declares one missing
- L78 `test_uses_uv_when_available(self, tmp_path)` (method)
- L85 `test_falls_back_to_pip_when_uv_missing(self, tmp_path, capsys)` (method) — The salvaged behavior (#5954): no uv but pip present -> python -m pip.
- L94 `test_aborts_when_neither_uv_nor_pip(self, tmp_path, capsys)` (method)
