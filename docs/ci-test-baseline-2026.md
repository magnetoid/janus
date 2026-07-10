# CI Test Baseline — Pre-existing failures to drive to zero

*Established 2026-07-10 when CI was first added (Track 1 Phase 0.1 of
[`self-improvement-evaluation-2026.md`](self-improvement-evaluation-2026.md), gap G2).*

## Why this file exists

Janus had **no CI** before [`.github/workflows/tests.yml`](../.github/workflows/tests.yml).
The full suite is run only on maintainer dev boxes, which carry environment
state (config, credentials, installed extras, a populated `~/.janus`) that a
clean CI runner does not. The first CI run therefore surfaced a large batch of
failures that are **pre-existing** — every one reproduces on `main` at the
commit CI was added, none was introduced by the Phase 0 work — of the exact
"works locally, fails in CI" class `CLAUDE.md` warns about.

The `tests-full` job runs **informationally** (`continue-on-error: true`) so
this baseline stays visible and shrinkable without blocking merges. The gate
becomes hard once the count reaches zero. `lint` and `tests-changed` are hard
gates today.

## Failure categories (from the clean `.[all,dev]` run)

1. **Change-detector tests that broke on legitimate refactors** — e.g.
   `test_windows_native_support.py::test_readme_mentions_powershell_installer`
   asserts `install.ps1` appears in `README.md` (the README was rewritten in
   `8857e06` and dropped it); `test_terminal_config_env_sync.py` asserts a
   `_terminal_env_map = {…}` literal exists in source (refactored away). These
   violate the repo's own "no change-detector tests" policy (`CLAUDE.md`) and
   are the cheapest wins — fix by asserting the invariant, not the text.
2. **Headless-approval env gap** — `test_code_execution.py` etc. expect
   `execute_code` to run, but the approval guard blocks it in a non-interactive
   context. Needs the test to set `approvals.headless_mode: approve` (or mock
   the guard).
3. **Missing test config / state divergence** — dashboard, gateway/service,
   model-picker, LSP, and honcho suites that depend on env/config a dev box
   has and a clean runner does not.

## The baseline list

<!-- BASELINE_LIST_START -->
39 files, from the first informational `tests-full` run (clean Ubuntu runner,
`.[all,dev]`, CI run 29099061312). Check a box when the file passes clean.

- [ ] `tests/agent/test_embeddings.py` *(needs `numpy` — the `voice`/embeddings optional dep)*
- [ ] `tests/cli/test_personality_none.py`
- [ ] `tests/cron/test_codex_execution_paths.py`
- [ ] `tests/janus_cli/test_aux_config.py`
- [ ] `tests/janus_cli/test_gateway_restart_loop.py`
- [ ] `tests/janus_cli/test_kanban_core_functionality.py`
- [ ] `tests/janus_cli/test_prompt_size.py`
- [ ] `tests/janus_cli/test_setup_reconfigure.py`
- [ ] `tests/janus_cli/test_startup_plugin_gating.py`
- [ ] `tests/janus_cli/test_status.py`
- [ ] `tests/janus_cli/test_terminal_menu_fallbacks.py`
- [ ] `tests/janus_cli/test_tool_token_estimation.py`
- [ ] `tests/janus_cli/test_tools_config.py`
- [ ] `tests/janus_cli/test_update_autostash.py`
- [ ] `tests/janus_cli/test_web_server.py`
- [ ] `tests/janus_cli/test_web_server_cron_profiles.py`
- [ ] `tests/janus_cli/test_web_server_session_search.py`
- [ ] `tests/janus_cli/test_web_ui_build.py`
- [ ] `tests/plugins/test_kanban_dashboard_plugin.py`
- [ ] `tests/run_agent/test_anthropic_prompt_cache_policy.py`
- [ ] `tests/run_agent/test_background_review_toolset_restriction.py`
- [ ] `tests/run_agent/test_percentage_clamp.py`
- [ ] `tests/run_agent/test_tool_arg_coercion.py`
- [ ] `tests/test_janus_bootstrap.py`
- [ ] `tests/test_lint_config.py`
- [ ] `tests/test_model_tools.py`
- [ ] `tests/test_sanitize_tool_error.py`
- [ ] `tests/test_timezone.py`
- [ ] `tests/test_tui_gateway_server.py`
- [ ] `tests/tools/test_approval.py`
- [ ] `tests/tools/test_code_execution.py` *(headless-approval env gap)*
- [ ] `tests/tools/test_code_execution_modes.py`
- [ ] `tests/tools/test_cron_approval_mode.py`
- [ ] `tests/tools/test_delegate_composite_toolsets.py`
- [ ] `tests/tools/test_execute_code_approval_cluster.py`
- [ ] `tests/tools/test_hardline_blocklist.py`
- [ ] `tests/tools/test_modal_sandbox_fixes.py`
- [ ] `tests/tools/test_terminal_config_env_sync.py` *(change-detector: source-literal introspection)*
- [ ] `tests/tools/test_terminal_tool_requirements.py`
- [ ] `tests/tools/test_windows_native_support.py` *(change-detector: README text pin)*
<!-- BASELINE_LIST_END -->

## How to shrink it

- Pick a file from the list, run it clean: `scripts/run_tests.sh <path>`
  (the wrapper's hermetic env reproduces CI locally).
- Fix the test or the code so it passes without dev-box state.
- Remove it from the list here. When the list is empty, flip `tests-full`'s
  `continue-on-error` off in the workflow — the gate is now hard.
