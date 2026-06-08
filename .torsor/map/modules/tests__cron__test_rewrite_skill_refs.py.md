---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_rewrite_skill_refs.py

Symbols in `tests/cron/test_rewrite_skill_refs.py`.

- L23 `cron_env(tmp_path, monkeypatch)` (function) — Isolated cron environment with temp HERMES_HOME.
- L40 `TestRewriteSkillRefsNoop` (class) — No jobs, no rewrites, no map — every combination of empty inputs.
- L43 `test_empty_map_and_no_jobs(self, cron_env)` (method)
- L49 `test_jobs_exist_but_map_empty(self, cron_env)` (method)
- L58 `test_jobs_exist_but_no_match(self, cron_env)` (method)
- L73 `TestRewriteSkillRefsConsolidation` (class) — Consolidated skills should be replaced with their umbrella target.
- L76 `test_single_skill_replaced(self, cron_env)` (method)
- L91 `test_multiple_skills_one_consolidated(self, cron_env)` (method)
- L105 `test_umbrella_already_in_list_dedupes(self, cron_env)` (method)
- L120 `test_rewrite_report_records_mapping(self, cron_env)` (method)
- L144 `TestRewriteSkillRefsPruning` (class) — Pruned skills should be dropped outright (no forwarding target).
- L147 `test_pruned_skill_dropped(self, cron_env)` (method)
- L162 `test_all_skills_pruned_leaves_empty_list(self, cron_env)` (method)
- L172 `test_pruned_report_records_drops(self, cron_env)` (method)
- L183 `TestRewriteSkillRefsMixed` (class) — Consolidation + pruning in the same pass.
- L186 `test_mixed_consolidation_and_pruning(self, cron_env)` (method)
- L202 `test_skill_in_both_maps_wins_as_consolidated(self, cron_env)` (method) — Defensive: if a skill appears in both lists (shouldn't happen
- L218 `TestRewriteSkillRefsMultipleJobs` (class) — Multiple jobs, some affected, some not.
- L221 `test_only_affected_jobs_reported(self, cron_env)` (method)
- L242 `test_legacy_skill_field_also_rewritten(self, cron_env)` (method) — Old jobs may have the legacy single-skill ``skill`` field
- L260 `TestRewriteSkillRefsPersistence` (class) — Rewrites persist to disk and survive a reload.
- L263 `test_changes_persist_across_reload(self, cron_env)` (method)
- L275 `test_noop_does_not_rewrite_file(self, cron_env)` (method)
