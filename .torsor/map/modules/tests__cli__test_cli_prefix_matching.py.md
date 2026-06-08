---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_prefix_matching.py

Symbols in `tests/cli/test_cli_prefix_matching.py`.

- L6 `_make_cli()` (function)
- L17 `TestSlashCommandPrefixMatching` (class)
- L18 `test_unique_prefix_dispatches_command(self)` (method) — /con should dispatch to /config when it uniquely matches.
- L25 `test_unique_prefix_with_args_does_not_recurse(self)` (method) — /con set key value should expand to /config set key value without infinite recursion.
- L49 `test_exact_command_with_args_does_not_recurse(self)` (method) — /config set key value hits exact branch and does not loop back to prefix.
- L72 `test_ambiguous_prefix_shows_suggestions(self)` (method) — /re matches multiple commands — should show ambiguous message.
- L80 `test_unknown_command_shows_error(self)` (method) — /xyz should show unknown command error.
- L88 `test_exact_command_still_works(self)` (method) — /help should still work as exact match.
- L95 `test_skill_command_prefix_matches(self)` (method) — A prefix that uniquely matches a skill command should dispatch it.
- L110 `test_ambiguous_between_builtin_and_skill(self)` (method) — Ambiguous prefix spanning builtin + skill commands shows suggestions.
- L125 `test_shortest_match_preferred_over_longer_skill(self)` (method) — /qui should dispatch to /quit (5 chars) not report ambiguous with /quint-pipeline (15 chars).
- L140 `test_tied_shortest_matches_still_ambiguous(self)` (method) — /re matches /reset and /retry (both 6 chars) — no unique shortest, stays ambiguous.
- L150 `test_exact_typed_name_dispatches_over_longer_match(self)` (method) — /help typed with /help-extra skill installed → exact match wins.
