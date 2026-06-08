---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_provider_groups.py

Symbols in `tests/hermes_cli/test_provider_groups.py`.

- L17 `_slugs(rows)` (function) — Flatten picker rows back to the concrete slugs they expose.
- L28 `test_groups_reference_real_canonical_slugs()` (function) — Every group member must be an actual provider slug. Guards typos and
- L40 `test_member_slugs_are_unique_across_groups()` (function) — A slug may belong to at most one group.
- L49 `test_reverse_index_matches_groups()` (function)
- L57 `test_ungrouped_providers_pass_through_in_order()` (function)
- L63 `test_multi_member_group_folds_to_one_row()` (function)
- L75 `test_group_appears_at_first_member_position()` (function) — The group row takes the slot of its earliest-listed present member,
- L89 `test_single_present_member_degrades_to_single_row()` (function) — A group with only one present member shows no submenu.
- L97 `test_member_order_follows_declaration_not_input()` (function) — Inside a folded group, members are ordered by PROVIDER_GROUPS, not by
- L104 `test_duplicate_slugs_ignored()` (function)
- L109 `test_fold_is_lossless_for_present_slugs()` (function) — Every input slug (deduped) must still be reachable through the folded
- L117 `test_canonical_fold_row_count_shrinks()` (function) — Folding the full canonical list produces fewer top-level rows than the
