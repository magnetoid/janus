---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_delta_key.py

Symbols in `tests/agent/lsp/test_delta_key.py`.

- L31 `_diag(*, line: int, message: str='Undefined variable', severity: int=1, code: str='reportUndefinedVariable', source: str='Pyright', end_line: int | None=None)` (function)
- L52 `test_diag_key_treats_shifted_diagnostics_as_distinct()` (function) — Two diagnostics with the same message but at different lines hash
- L62 `test_diag_key_matches_client_key_for_shifted_baseline()` (function) — When a baseline diagnostic is remapped through a shift, its
- L77 `test_diag_key_distinguishes_message()` (function)
- L83 `test_diag_key_distinguishes_severity()` (function)
- L89 `test_diag_key_distinguishes_source()` (function)
- L95 `test_diag_key_matches_client_key_byte_for_byte()` (function) — The manager-side and client-side keys must agree on diagnostic
- L107 `test_shift_identity_for_identical_content()` (function)
- L114 `test_shift_pure_deletion_above_line()` (function) — Delete 2 lines at the top; everything below shifts up by 2.
- L128 `test_shift_pure_insertion_above_line()` (function) — Insert 3 lines at the top; everything below shifts down by 3.
- L139 `test_shift_replacement_in_middle()` (function) — Replace 2 lines in the middle with 1 line.  Lines above
- L152 `test_shift_handles_empty_pre()` (function) — First write of a file: pre is empty, post has content.  Nothing
- L160 `test_shift_handles_empty_post()` (function) — File deleted to empty.  Every pre line returns None.
- L171 `test_shift_diag_remaps_start_and_end()` (function)
- L182 `test_shift_diag_drops_diagnostic_in_deleted_region()` (function)
- L190 `test_shift_diag_does_not_mutate_original()` (function)
- L200 `test_shift_baseline_drops_deleted_and_remaps_rest()` (function)
- L220 `test_pipeline_filters_shifted_baseline_under_strict_key()` (function) — The exact scenario the bug fix is for: an edit deletes lines,
- L241 `test_pipeline_preserves_new_instance_at_different_line()` (function) — The case content-only keys would miss: the model introduces a
