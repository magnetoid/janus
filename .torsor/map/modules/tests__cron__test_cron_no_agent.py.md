---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_no_agent.py

Symbols in `tests/cron/test_cron_no_agent.py`.

- L21 `hermes_env(tmp_path, monkeypatch)` (function) — Isolate HERMES_HOME for each test so jobs/scripts don't leak.
- L47 `test_create_job_no_agent_requires_script(hermes_env)` (function)
- L54 `test_create_job_no_agent_stores_field(hermes_env)` (function)
- L73 `test_create_job_default_is_not_no_agent(hermes_env)` (function)
- L80 `test_update_job_roundtrips_no_agent_flag(hermes_env)` (function)
- L101 `test_cronjob_tool_create_no_agent_without_script_errors(hermes_env)` (function)
- L111 `test_cronjob_tool_create_no_agent_with_script_succeeds(hermes_env)` (function)
- L131 `test_cronjob_tool_update_toggles_no_agent(hermes_env)` (function)
- L157 `test_cronjob_tool_update_no_agent_without_script_errors(hermes_env)` (function) — Flipping no_agent=True on a job that has no script must fail.
- L171 `test_cronjob_tool_create_does_not_require_prompt_when_no_agent(hermes_env)` (function) — The 'prompt or skill required' rule is relaxed for no_agent jobs.
- L195 `test_run_job_no_agent_success_returns_script_stdout(hermes_env)` (function) — Happy path: script exits 0 with output, delivered verbatim.
- L213 `test_run_job_no_agent_empty_output_is_silent(hermes_env)` (function) — Empty stdout → SILENT_MARKER, which suppresses delivery downstream.
- L230 `test_run_job_no_agent_wake_gate_is_silent(hermes_env)` (function) — wakeAgent=false gate in stdout triggers a silent run.
- L246 `test_run_job_no_agent_script_failure_delivers_error(hermes_env)` (function) — Non-zero exit → success=False, error alert is the delivered message.
- L264 `test_run_job_no_agent_never_invokes_aiagent(hermes_env)` (function) — no_agent jobs must NOT import/construct the AIAgent.
- L288 `test_run_job_script_shell_script_runs_via_bash(hermes_env)` (function) — .sh files should execute under /bin/bash even without a shebang line.
- L301 `test_run_job_script_bash_extension_also_runs_via_bash(hermes_env)` (function)
- L312 `test_run_job_script_python_still_runs_via_python(hermes_env)` (function) — Regression: .py files must keep running via sys.executable.
- L324 `test_run_job_script_path_traversal_still_blocked(hermes_env)` (function) — Security regression: shell-script support must NOT loosen containment.
