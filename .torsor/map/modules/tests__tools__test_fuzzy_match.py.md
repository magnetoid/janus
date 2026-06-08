---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_fuzzy_match.py

Symbols in `tests/tools/test_fuzzy_match.py`.

- L6 `TestExactMatch` (class)
- L7 `test_single_replacement(self)` (method)
- L14 `test_no_match(self)` (method)
- L21 `test_empty_old_string(self)` (method)
- L26 `test_identical_strings(self)` (method)
- L31 `test_multiline_exact(self)` (method)
- L39 `TestWhitespaceDifference` (class)
- L40 `test_extra_spaces_match(self)` (method)
- L47 `TestIndentDifference` (class)
- L48 `test_different_indentation(self)` (method)
- L55 `TestIndentationPreservation` (class) — When a non-exact strategy matches, ``new_string`` should be re-indented
- L62 `test_unindented_input_reindented_to_match_file(self)` (method)
- L86 `test_dedent_at_start_anchors_to_file_base(self)` (method)
- L104 `test_exact_match_no_reindent(self)` (method)
- L114 `test_llm_zero_indent_shifts_to_file_two_space(self)` (method)
- L127 `test_indent_already_matches_passthrough(self)` (method)
- L140 `test_blank_lines_left_alone(self)` (method)
- L155 `TestReplaceAll` (class)
- L156 `test_multiple_matches_without_flag_errors(self)` (method)
- L162 `test_multiple_matches_with_flag(self)` (method)
- L170 `TestUnicodeNormalized` (class) — Tests for the unicode_normalized strategy (Bug 5).
- L173 `test_em_dash_matched(self)` (method) — Em-dash in content should match ASCII '--' in pattern.
- L183 `test_smart_quotes_matched(self)` (method) — Smart double quotes in content should match straight quotes in pattern.
- L192 `test_no_unicode_skips_strategy(self)` (method) — When content and pattern have no Unicode variants, strategy is skipped.
- L201 `TestBlockAnchorThreshold` (class) — Tests for the raised block_anchor threshold (Bug 4).
- L204 `test_high_similarity_matches(self)` (method) — A block with >50% middle similarity should match.
- L212 `test_completely_different_middle_does_not_match(self)` (method) — A block where only first+last lines match but middle is completely different
- L238 `TestStrategyNameSurfaced` (class) — Tests for the strategy name in the 4-tuple return (Bug 6).
- L241 `test_exact_strategy_name(self)` (method)
- L246 `test_failed_match_returns_none_strategy(self)` (method)
- L252 `TestEscapeDriftGuard` (class) — Tests for the escape-drift guard that catches bash/JSON serialization
- L258 `test_drift_blocked_apostrophe(self)` (method) — File has ', old_string and new_string both have \' — classic
- L280 `test_drift_blocked_double_quote(self)` (method) — Same idea but with \" drift instead of \'.
- L289 `test_drift_allowed_when_file_genuinely_has_backslash_escapes(self)` (method) — If the file already contains \' (e.g. inside an existing escaped
- L301 `test_drift_allowed_on_exact_match(self)` (method) — Exact matches bypass the drift guard entirely — if the file
- L313 `test_drift_allowed_when_adding_escaped_strings(self)` (method) — Model is adding new content with \' that wasn't in the original.
- L324 `test_no_drift_check_when_new_string_lacks_suspect_chars(self)` (method) — Fast-path: if new_string has no \' or \", guard must not
- L335 `TestFindClosestLines` (class)
- L336 `setup_method(self)` (method)
- L340 `test_finds_similar_line(self)` (method)
- L345 `test_returns_empty_for_no_match(self)` (method)
- L350 `test_returns_empty_for_empty_inputs(self)` (method)
- L354 `test_includes_context_lines(self)` (method)
- L359 `test_includes_line_numbers(self)` (method)
- L366 `TestFormatNoMatchHint` (class) — Gating tests for format_no_match_hint — the shared helper that decides
- L371 `setup_method(self)` (method)
- L375 `test_fires_on_could_not_find_with_match(self)` (method) — Classic no-match: similar content exists → hint fires.
- L385 `test_silent_on_ambiguous_match_error(self)` (method) — 'Found N matches' is not a missing-match failure — no hint.
- L394 `test_silent_on_escape_drift_error(self)` (method) — Escape-drift errors are intentional blocks — hint would mislead.
- L403 `test_silent_on_identical_strings(self)` (method) — old_string == new_string — hint irrelevant.
- L411 `test_silent_when_match_count_nonzero(self)` (method) — If match succeeded, we shouldn't be in the error path — defense in depth.
- L419 `test_silent_on_none_error(self)` (method) — No error at all — no hint.
- L424 `test_silent_when_no_similar_content(self)` (method) — Even for a valid no-match error, skip hint when nothing similar exists.
- L433 `TestEscapeNormalizedNewString` (class) — Regression tests for unescaping common sequences in new_string when
- L448 `test_tab_in_new_string_unescaped_under_escape_normalized(self)` (method) — File has real tab, model sends literal \t in BOTH old and new.
- L463 `test_tab_in_new_string_unescaped_under_exact(self)` (method) — File has real tab, old_string has real tab too (matches via
- L480 `test_carriage_return_in_new_string_unescaped(self)` (method) — File has real CR, model sends literal \r in new_string.
- L491 `test_newline_in_new_string_NOT_unescaped(self)` (method) — ``\n`` is intentionally left alone — newlines serialize correctly
- L507 `test_mixed_tab_and_newline_only_tab_unescaped(self)` (method) — When new_string contains both \t and \n, only \t is converted.
- L521 `test_exact_match_preserves_literal_backslash_t_in_string_literal(self)` (method) — If the matched region of the file does NOT contain a real tab,
- L537 `test_no_escape_sequences_passthrough(self)` (method) — When new_string has no \t or \r, the helper is a no-op.
