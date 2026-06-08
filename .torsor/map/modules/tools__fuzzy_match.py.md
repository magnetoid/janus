---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/fuzzy_match.py

Symbols in `tools/fuzzy_match.py`.

- L43 `_unicode_normalize(text: str)` (function) — Normalizes Unicode characters to their standard ASCII equivalents.
- L50 `fuzzy_find_and_replace(content: str, old_string: str, new_string: str, replace_all: bool=False)` (function) — Find and replace text using a chain of increasingly fuzzy matching strategies.
- L147 `_detect_escape_drift(content: str, matches: List[Tuple[int, int]], old_string: str, new_string: str)` (function) — Detect tool-call escape-drift artifacts in new_string.
- L187 `_leading_whitespace(line: str)` (function) — Return the leading whitespace prefix of a line (spaces/tabs).
- L195 `_first_meaningful_line(text: str)` (function) — Return the first line of ``text`` that has any non-whitespace content.
- L206 `_reindent_replacement(file_region: str, old_string: str, new_string: str)` (function) — Adjust ``new_string`` so its indentation matches ``file_region``.
- L271 `_maybe_unescape_new_string(new_string: str, content: str, matches: List[Tuple[int, int]])` (function) — Conditionally unescape ``\t``/``\r`` in new_string.
- L307 `_apply_replacements(content: str, matches: List[Tuple[int, int]], new_string: str, old_string: Optional[str]=None)` (function) — Apply replacements at the given positions.
- L343 `_strategy_exact(content: str, pattern: str)` (function) — Strategy 1: Exact string match.
- L356 `_strategy_line_trimmed(content: str, pattern: str)` (function) — Strategy 2: Match with line-by-line whitespace trimming.
- L376 `_strategy_whitespace_normalized(content: str, pattern: str)` (function) — Strategy 3: Collapse multiple whitespace to single space.
- L397 `_strategy_indentation_flexible(content: str, pattern: str)` (function) — Strategy 4: Ignore indentation differences entirely.
- L413 `_strategy_escape_normalized(content: str, pattern: str)` (function) — Strategy 5: Convert escape sequences to actual characters.
- L432 `_strategy_trimmed_boundary(content: str, pattern: str)` (function) — Strategy 6: Trim whitespace from first and last lines only.
- L474 `_build_orig_to_norm_map(original: str)` (function) — Build a list mapping each original character index to its normalized index.
- L495 `_map_positions_norm_to_orig(orig_to_norm: List[int], norm_matches: List[Tuple[int, int]])` (function) — Convert (start, end) positions in the normalised string to original positions.
- L524 `_strategy_unicode_normalized(content: str, pattern: str)` (function) — Strategy 7: Unicode normalisation.
- L555 `_strategy_block_anchor(content: str, pattern: str)` (function) — Strategy 8: Match by anchoring on first and last lines.
- L611 `_strategy_context_aware(content: str, pattern: str)` (function) — Strategy 9: Line-by-line similarity with 50% threshold.
- L650 `_calculate_line_positions(content_lines: List[str], start_line: int, end_line: int, content_length: int)` (function) — Calculate start and end character positions from line indices.
- L669 `_find_normalized_matches(content: str, content_lines: List[str], content_normalized_lines: List[str], pattern: str, pattern_normalized: str)` (function) — Find matches in normalized content and map back to original positions.
- L704 `_map_normalized_positions(original: str, normalized: str, normalized_matches: List[Tuple[int, int]])` (function) — Map positions from normalized string back to original.
- L780 `find_closest_lines(old_string: str, content: str, context_lines: int=2, max_results: int=3)` (function) — Find lines in content most similar to old_string for "did you mean?" feedback.
- L842 `format_no_match_hint(error: Optional[str], match_count: int, old_string: str, content: str)` (function) — Return a '\n\nDid you mean...' snippet for plain no-match errors.
