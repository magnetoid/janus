---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_curator.py

Symbols in `tests/agent/test_curator.py`.

- L17 `curator_env(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME + freshly reloaded curator + skill_usage modules.
- L43 `_write_skill(skills_dir: Path, name: str)` (function)
- L56 `test_curator_enabled_default_true(curator_env)` (function)
- L60 `test_curator_disabled_via_config(curator_env, monkeypatch)` (function)
- L67 `test_curator_defaults(curator_env)` (function)
- L75 `test_curator_config_overrides(curator_env, monkeypatch)` (function)
- L93 `test_first_run_defers(curator_env)` (function) — The FIRST observation of the curator (fresh install, no state file)
- L111 `test_recent_run_blocks(curator_env)` (function)
- L120 `test_old_run_eligible(curator_env)` (function) — A run older than the configured interval should re-trigger. Use a
- L132 `test_paused_blocks_even_if_stale(curator_env)` (function)
- L139 `test_set_paused_roundtrip(curator_env)` (function)
- L151 `test_unused_skill_transitions_to_stale(curator_env)` (function)
- L171 `test_very_old_skill_gets_archived(curator_env)` (function)
- L192 `test_pinned_skill_is_never_touched(curator_env)` (function)
- L215 `test_stale_skill_reactivates_on_recent_use(curator_env)` (function)
- L235 `test_new_skill_without_last_used_not_immediately_archived(curator_env)` (function) — A freshly-created skill with no use history should not get archived
- L251 `test_manual_skill_is_not_auto_archived(curator_env)` (function) — Manual skills can have usage records, but without the agent-created
- L272 `test_bundled_skill_not_touched_by_transitions(curator_env)` (function)
- L297 `_enable_prune_builtins(curator_env, monkeypatch)` (function) — Flip curator.prune_builtins on for both config-reading paths.
- L305 `_disable_prune_builtins(curator_env, monkeypatch)` (function) — Flip curator.prune_builtins off for both config-reading paths.
- L313 `test_prune_builtins_default_on(curator_env)` (function)
- L320 `test_prune_builtins_off_excludes_bundled(curator_env, monkeypatch)` (function)
- L334 `test_prune_builtins_seeds_clock_on_first_sight(curator_env, monkeypatch)` (function)
- L353 `test_prune_builtins_archives_stale_bundled_and_suppresses(curator_env, monkeypatch)` (function)
- L376 `test_prune_builtins_restore_clears_suppression(curator_env, monkeypatch)` (function)
- L393 `test_prune_builtins_never_touches_hub_skills(curator_env, monkeypatch)` (function)
- L417 `test_run_review_records_state(curator_env)` (function)
- L432 `test_dry_run_does_not_advance_state(curator_env, monkeypatch)` (function) — Dry-run previews must not bump last_run_at or run_count. A preview
- L461 `test_dry_run_injects_report_only_banner(curator_env, monkeypatch)` (function) — The dry-run prompt must carry a banner instructing the LLM not to
- L484 `test_dry_run_skips_automatic_transitions(curator_env, monkeypatch)` (function) — Dry-run must not call apply_automatic_transitions — the auto pass
- L509 `test_run_review_synchronous_invokes_llm_stub(curator_env, monkeypatch)` (function)
- L538 `test_run_review_skips_llm_when_no_candidates(curator_env, monkeypatch)` (function)
- L554 `test_maybe_run_curator_respects_disabled(curator_env, monkeypatch)` (function)
- L561 `test_maybe_run_curator_enforces_idle_gate(curator_env, monkeypatch)` (function)
- L569 `test_maybe_run_curator_runs_when_eligible(curator_env, monkeypatch)` (function)
- L585 `test_maybe_run_curator_defers_on_fresh_install(curator_env)` (function) — Fresh install (no curator state file) must NOT fire the curator on
- L601 `test_maybe_run_curator_swallows_exceptions(curator_env, monkeypatch)` (function)
- L616 `test_state_file_survives_corrupt_read(curator_env)` (function)
- L623 `test_state_atomic_write_no_tmp_leftovers(curator_env)` (function)
- L631 `test_state_preserves_last_report_path(curator_env)` (function)
- L644 `test_curator_review_prompt_has_invariants()` (function) — Core invariants must be in the review prompt text.
- L662 `test_curator_review_prompt_points_at_existing_tools_only()` (function) — The review prompt must rely on existing tools (skill_manage + terminal)
- L677 `test_curator_does_not_instruct_model_to_pin()` (function) — Pinning is a user opt-out, not a model decision. The prompt should
- L694 `test_curator_review_prompt_is_umbrella_first()` (function) — The curator prompt must push umbrella-building / class-level thinking,
- L719 `test_curator_review_prompt_preserves_skill_package_integrity()` (function) — Consolidation must not flatten package skills and break linked files.
- L734 `test_curator_review_prompt_offers_support_file_actions()` (function) — Support-file demotion (references/templates/scripts) must be one of
- L748 `test_cli_unpin_refuses_bundled_skill(curator_env, capsys)` (function) — hermes curator unpin must refuse bundled/hub skills too (matches pin).
- L766 `test_cli_pin_refuses_bundled_skill(curator_env, capsys)` (function)
- L794 `test_review_model_defaults_to_main_when_slot_is_auto(curator_env)` (function) — auxiliary.curator absent (or auto/empty) → use main model.provider/model.
- L807 `test_review_model_honors_auxiliary_curator_slot(curator_env)` (function) — auxiliary.curator.{provider,model} fully set → that pair wins.
- L824 `test_review_runtime_passes_auxiliary_curator_credentials(curator_env)` (function) — Per-slot api_key/base_url must ride into resolve_runtime_provider (not main-only creds).
- L845 `test_review_runtime_strips_blank_aux_credentials(curator_env)` (function)
- L863 `test_review_runtime_ignores_auxiliary_credentials_when_using_main(curator_env)` (function) — Falling through to main model must not pick up stray auxiliary.curator secrets.
- L883 `test_review_runtime_legacy_auxiliary_carry_credentials(curator_env, caplog)` (function)
- L904 `test_review_model_auxiliary_curator_partial_override_falls_back(curator_env)` (function) — Only one of slot provider/model set → fall back to the main pair.
- L930 `test_review_model_legacy_curator_auxiliary_still_works(curator_env, caplog)` (function) — Pre-unification users set curator.auxiliary.{provider,model} — honor it.
- L954 `test_review_model_new_slot_wins_over_legacy(curator_env)` (function) — When BOTH new and legacy are set, the canonical slot wins.
- L969 `test_review_model_handles_missing_sections(curator_env)` (function) — Missing auxiliary/curator sections never raise — fall back cleanly.
- L982 `test_curator_slot_is_canonical_aux_task()` (function) — Curator must be a first-class slot in every aux-task registry.
