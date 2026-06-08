---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_curator_classification.py

Symbols in `tests/agent/test_curator_classification.py`.

- L24 `curator_env(tmp_path, monkeypatch)` (function)
- L40 `test_classify_consolidated_via_write_file_evidence(curator_env)` (function) — skill_manage write_file on umbrella references/<removed>.md = consolidated.
- L64 `test_classify_pruned_when_no_destination_reference(curator_env)` (function) — Removed skill with no referencing tool call = pruned.
- L83 `test_classify_consolidated_into_newly_created_umbrella(curator_env)` (function) — Removed skill absorbed into a skill that was created THIS run.
- L105 `test_classify_handles_underscore_hyphen_variants(curator_env)` (function) — Names with hyphens match underscore forms in paths/content and vice versa.
- L127 `test_classify_self_reference_does_not_count(curator_env)` (function) — A tool call that targets the removed skill itself is NOT consolidation.
- L150 `test_classify_destination_must_exist_after_run(curator_env)` (function) — A reference to a skill that doesn't exist after the run can't be the umbrella.
- L172 `test_classify_mixed_run_produces_both_buckets(curator_env)` (function) — A realistic run: one skill consolidated, one skill pruned.
- L197 `test_classify_handles_malformed_arguments_string(curator_env)` (function) — Truncated/malformed JSON in arguments falls back to substring match.
- L223 `test_classify_no_false_positive_short_name_in_file_path(curator_env)` (function) — Short skill name that is a substring of another filename = pruned, not consolidated.
- L249 `test_classify_no_false_positive_short_name_in_content(curator_env)` (function) — Short skill name embedded in longer word in content = pruned, not consolidated.
- L274 `test_classify_still_matches_exact_word_in_content(curator_env)` (function) — Word-boundary match still works for exact word occurrences.
- L298 `test_report_md_splits_consolidated_and_pruned_sections(curator_env)` (function) — End-to-end: REPORT.md shows both sections distinctly.
- L370 `test_parse_structured_summary_happy_path(curator_env)` (function)
- L398 `test_parse_structured_summary_missing_block(curator_env)` (function)
- L403 `test_parse_structured_summary_malformed_yaml(curator_env)` (function)
- L409 `test_parse_structured_summary_empty_lists(curator_env)` (function)
- L415 `test_parse_structured_summary_ignores_bare_strings(curator_env)` (function) — Entries that aren't dicts (e.g. a model wrote bare names) are skipped.
- L432 `test_parse_structured_summary_missing_required_fields(curator_env)` (function) — Consolidation entries without from+into are skipped.
- L455 `test_reconcile_model_wins_when_umbrella_exists(curator_env)` (function) — Model claim + umbrella in destinations → model authority (with reason).
- L479 `test_reconcile_model_hallucinates_umbrella(curator_env)` (function) — Model names a non-existent umbrella — downgrade, prefer heuristic if any.
- L504 `test_reconcile_model_hallucinates_with_no_heuristic_evidence(curator_env)` (function) — Model names a non-existent umbrella AND no tool-call evidence → prune.
- L524 `test_reconcile_heuristic_catches_model_omission(curator_env)` (function) — Model forgot to list a consolidation, heuristic found it.
- L545 `test_reconcile_model_prunes_with_reason(curator_env)` (function) — Model says pruned, heuristic agrees, we surface the reason.
- L562 `test_reconcile_model_block_visible_in_full_report(curator_env)` (function) — End-to-end: LLM final response with the YAML block → reasons in REPORT.md.
- L633 `test_extract_absorbed_into_picks_up_consolidation(curator_env)` (function) — Delete call with absorbed_into=<umbrella> yields a declaration.
- L650 `test_extract_absorbed_into_empty_string_is_explicit_prune(curator_env)` (function) — absorbed_into='' is recorded as an explicit prune declaration.
- L665 `test_extract_absorbed_into_missing_arg_ignored(curator_env)` (function) — Delete call without absorbed_into is skipped — fallback to heuristic.
- L679 `test_extract_absorbed_into_ignores_non_delete_actions(curator_env)` (function) — Patch, create, write_file etc. must not leak into declarations.
- L696 `test_extract_absorbed_into_accepts_dict_arguments(curator_env)` (function) — arguments can arrive as a dict (defensive path) — still works.
- L711 `test_extract_absorbed_into_strips_whitespace(curator_env)` (function)
- L725 `test_extract_absorbed_into_ignores_non_skill_manage_calls(curator_env)` (function)
- L733 `test_extract_absorbed_into_handles_malformed_arguments(curator_env)` (function) — Garbage JSON in arguments must not crash the extractor.
- L748 `test_reconcile_absorbed_into_beats_everything_else(curator_env)` (function) — Model declared absorbed_into at delete; YAML/heuristic disagree — declaration wins.
- L775 `test_reconcile_absorbed_into_empty_is_explicit_prune(curator_env)` (function) — absorbed_into='' takes precedence and routes to pruned, not fallback.
- L791 `test_reconcile_absorbed_into_nonexistent_target_falls_through(curator_env)` (function) — If the declared umbrella doesn't exist in destinations, fall through to
- L812 `test_reconcile_declaration_preserves_yaml_reason(curator_env)` (function) — When the model both declared absorbed_into AND emitted YAML with reason,
- L838 `test_reconcile_without_declarations_preserves_legacy_behavior(curator_env)` (function) — Backward compat: no absorbed_declarations arg → all existing logic intact.
- L854 `test_reconcile_mixed_declarations_and_legacy_calls(curator_env)` (function) — Real-world run: some deletes declared absorbed_into, some didn't.
- L899 `test_rename_summary_empty_when_nothing_archived(curator_env)` (function) — No removals = empty string (no log noise on no-op ticks).
- L913 `test_rename_summary_consolidation_shows_target(curator_env)` (function) — Consolidated skills render as `name → umbrella` with the actual target.
- L944 `test_rename_summary_pruned_marked_explicitly(curator_env)` (function) — Pruned skills (no umbrella) say `pruned (stale)` so users don't think they were merged.
- L965 `test_rename_summary_caps_at_ten_with_more_indicator(curator_env)` (function) — Large consolidations don't blow up the log line — cap + `… and N more`.
- L992 `test_rename_summary_mixed_consolidation_and_pruning(curator_env)` (function) — Consolidated entries come first, pruned entries follow — matches REPORT.md ordering.
- L1033 `test_rename_summary_pin_hint_appears_when_consolidation_produced_umbrella(curator_env)` (function) — When at least one skill was absorbed into an umbrella, hint at pinning it.
- L1062 `test_rename_summary_pin_hint_skipped_for_pruned_only_runs(curator_env)` (function) — Pruned-only runs have nothing surviving to pin — hint should not appear.
- L1093 `test_rename_summary_pin_hint_picks_one_umbrella_when_multiple_absorbed(curator_env)` (function) — Multiple umbrellas → hint shows one example (alphabetically first), not a list.
