---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_uv_tool_update.py

Symbols in `tests/hermes_cli/test_uv_tool_update.py`.

- L33 `_patch_managed_uv(request)` (function) — Make managed_uv helpers follow shutil.which mocking in tests.
- L59 `TestIsUvToolInstall` (class)
- L60 `test_returns_true_when_sys_prefix_matches_uv_tool_layout(self)` (method)
- L66 `test_returns_true_when_sys_executable_matches_uv_tool_layout(self)` (method) — Some uv-tool layouts surface the marker on ``sys.executable`` (bin/python).
- L78 `test_returns_false_when_neither_prefix_nor_executable_matches(self)` (method)
- L85 `test_does_not_consult_uv_tool_list(self)` (method) — Detection must NOT shell out: ``uv tool list`` would false-positive
- L99 `test_case_insensitive_match(self)` (method) — Match must be case-insensitive — Windows paths preserve case
- L111 `test_handles_empty_executable(self)` (method)
- L124 `TestRecommendedUpdateCommandForUvTool` (class)
- L125 `test_uv_tool_install_recommends_uv_tool_upgrade(self)` (method)
- L133 `test_uv_tool_install_recommends_uv_tool_upgrade_even_without_uv_on_path(self)` (method) — Recommendation reflects the *install method*, not whether ``uv`` is
- L143 `test_uv_pip_install_keeps_legacy_recommendation(self)` (method) — Existing behavior: uv is on PATH but Hermes is a regular pip install.
- L152 `test_no_uv_falls_back_to_plain_pip(self)` (method)
- L160 `test_recommendation_does_not_spawn_subprocess(self)` (method) — Computing the recommendation string must be cheap — no ``uv tool list``
- L181 `TestCmdUpdatePipUsesUvTool` (class)
- L183 `test_runs_uv_tool_upgrade_when_uv_tool_install(self, mock_run)` (method) — The actual subprocess invocation must switch to ``uv tool upgrade``.
- L195 `test_runs_uv_pip_install_when_not_uv_tool(self, mock_run)` (method) — Existing behavior preserved when uv is present but Hermes isn't a tool install.
- L213 `test_falls_back_to_pip_when_no_uv(self, mock_run)` (method)
- L225 `test_exits_nonzero_on_subprocess_failure(self, mock_run)` (method)
- L236 `test_uv_tool_install_without_uv_on_path_exits_with_hint(self, mock_run)` (method) — If the running interpreter looks like a uv-tool install but ``uv`` is
- L257 `TestCmdUpdatePipInstallLayouts` (class) — The uv pip path must adapt to where the running interpreter lives:
- L266 `test_pipx_managed_uses_pipx_upgrade(self, mock_run, monkeypatch)` (method)
- L285 `test_pipx_layout_without_pipx_binary_treated_as_venv(self, mock_run, monkeypatch)` (method)
- L309 `test_bare_pip_outside_venv_adds_system(self, mock_run, monkeypatch)` (method)
- L327 `test_venv_exports_virtualenv_and_omits_system(self, mock_run, monkeypatch)` (method)
