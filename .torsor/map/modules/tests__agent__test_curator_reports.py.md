---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_curator_reports.py

Symbols in `tests/agent/test_curator_reports.py`.

- L17 `curator_env(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with a skills/ dir + reset curator module state.
- L36 `_make_llm_meta(**overrides)` (function)
- L49 `test_reports_root_is_under_logs_not_skills(curator_env)` (function) — Reports live in logs/curator/, not skills/ — operational telemetry
- L61 `test_write_run_report_creates_both_files(curator_env)` (function) — Each run writes both a run.json (machine) and a REPORT.md (human).
- L85 `test_run_json_has_expected_shape(curator_env)` (function) — run.json must carry the machine-readable fields downstream tooling needs.
- L142 `test_report_md_is_human_readable(curator_env)` (function) — REPORT.md should be a valid markdown doc with the key sections visible.
- L197 `test_same_second_reruns_get_unique_dirs(curator_env)` (function) — If the curator somehow runs twice in the same second, the second
- L221 `test_report_captures_llm_error_and_continues(curator_env)` (function) — If the LLM pass recorded an error, the report still writes and
- L245 `test_state_transitions_captured_in_report(curator_env)` (function) — When a skill moves active → stale or stale → archived between
- L288 `curator_env_with_cron(curator_env, monkeypatch)` (function) — Extend curator_env with an initialized + repointed cron.jobs module.
- L305 `test_curator_rewrites_cron_skills_when_skill_consolidated(curator_env_with_cron)` (function) — A skill consolidated into an umbrella should be rewritten in any
- L374 `test_curator_drops_pruned_skill_from_cron_job(curator_env_with_cron)` (function) — A pruned (no-umbrella) skill should be dropped from the cron
- L409 `test_curator_report_has_no_cron_section_when_nothing_changes(curator_env_with_cron)` (function) — When the curator run doesn't touch any skills, cron jobs are
