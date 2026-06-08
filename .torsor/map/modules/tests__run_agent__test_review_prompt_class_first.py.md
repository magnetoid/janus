---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_review_prompt_class_first.py

Symbols in `tests/run_agent/test_review_prompt_class_first.py`.

- L24 `test_skill_review_prompt_biases_toward_active_updates()` (function) — Prompt must frame updating as the default stance, not something rare.
- L36 `test_skill_review_prompt_treats_user_corrections_as_skill_signal()` (function) — Style/format/verbosity complaints must be FIRST-CLASS skill signals, not just memory.
- L54 `test_skill_review_prompt_prefers_loaded_skills_first()` (function) — Currently-loaded skills must be the first patch target.
- L66 `test_skill_review_prompt_has_four_step_preference_order()` (function) — The 4-step patch/support-file/create ladder must be present.
- L75 `test_skill_review_prompt_names_three_support_file_kinds()` (function) — Support-file step must name references/, templates/, and scripts/.
- L93 `test_skill_review_prompt_has_name_veto_for_create()` (function) — Creating a new skill must be gated behind class-level naming.
- L102 `test_skill_review_prompt_embeds_user_preferences_in_skills()` (function) — Must explicitly say user-preference lessons belong in SKILL.md, not only memory.
- L112 `test_skill_review_prompt_flags_overlap_and_defers_to_curator()` (function) — Reviewer should not consolidate live; flag overlap for the curator.
- L119 `test_skill_review_prompt_still_has_opt_out_clause()` (function) — 'Nothing to save.' must remain as a real-but-not-default option.
- L129 `test_combined_review_prompt_has_memory_section()` (function) — Memory half must still cover user facts and preferences.
- L136 `test_combined_review_prompt_skills_biased_toward_active_updates()` (function) — Skills half must carry the active-update bias.
- L144 `test_combined_review_prompt_treats_user_corrections_as_skill_signal()` (function) — Combined prompt must carry the same user-preference-is-skill-signal rule.
- L152 `test_combined_review_prompt_prefers_loaded_skills_first()` (function) — Combined prompt must also prefer loaded skills first.
- L159 `test_combined_review_prompt_has_four_step_skill_ladder()` (function) — Combined prompt must keep the patch/support-file/create ladder on the Skills half.
- L168 `test_combined_review_prompt_names_three_support_file_kinds()` (function) — Combined prompt must also name all three support-file kinds.
- L176 `test_combined_review_prompt_preserves_opt_out_clause()` (function)
- L191 `_assert_anti_pattern_guidance(prompt: str, label: str)` (function) — Both review prompts must carry the same anti-pattern section.
- L215 `test_skill_review_prompt_has_anti_pattern_guidance()` (function) — _SKILL_REVIEW_PROMPT must tell the reviewer NOT to capture transient env failures (#6051).
- L220 `test_combined_review_prompt_has_anti_pattern_guidance()` (function) — _COMBINED_REVIEW_PROMPT must carry the same guidance — same failure mode applies.
- L229 `test_memory_review_prompt_still_focused_on_user_facts()` (function) — Memory-only review prompt stays focused on user facts — not touched by this change.
