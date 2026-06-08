---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_compound_background.py

Symbols in `tests/tools/test_terminal_compound_background.py`.

- L19 `TestRewrites` (class) — Commands that trigger the subshell-wait bug MUST be rewritten.
- L22 `test_simple_and_background(self)` (method)
- L25 `test_or_background(self)` (method)
- L28 `test_chained_and(self)` (method)
- L31 `test_chained_or(self)` (method)
- L34 `test_mixed_and_or(self)` (method)
- L37 `test_realistic_server_start(self)` (method)
- L51 `test_newline_resets_chain_state(self)` (method)
- L56 `test_semicolon_resets_chain_state(self)` (method)
- L60 `test_pipe_resets_chain_state(self)` (method)
- L64 `test_multiple_rewrites_in_one_script(self)` (method)
- L69 `TestPreserved` (class) — Commands that DON'T have the bug MUST pass through unchanged.
- L72 `test_simple_background(self)` (method)
- L76 `test_plain_server_background(self)` (method)
- L79 `test_semicolon_sequence(self)` (method)
- L82 `test_no_trailing_ampersand(self)` (method)
- L85 `test_no_chain_at_all(self)` (method)
- L88 `test_empty_string(self)` (method)
- L91 `test_whitespace_only(self)` (method)
- L95 `TestRedirectsNotConfused` (class) — ``&>``, ``2>&1``, ``>&2`` must not be mistaken for background ``&``.
- L98 `test_amp_gt_redirect_alone(self)` (method)
- L101 `test_fd_to_fd_redirect(self)` (method)
- L104 `test_fd_redirect_with_trailing_bg(self)` (method)
- L108 `test_amp_gt_inside_compound_background(self)` (method)
- L113 `test_gt_amp_inside_compound(self)` (method)
- L118 `TestQuotingAndParens` (class) — Shell metacharacters inside quotes/parens must not be parsed as operators.
- L121 `test_and_and_inside_single_quotes(self)` (method)
- L125 `test_and_and_inside_double_quotes(self)` (method)
- L129 `test_parenthesised_subshell_left_alone(self)` (method)
- L135 `test_command_substitution_not_rewritten(self)` (method)
- L141 `test_backslash_escaped_ampersand(self)` (method)
- L146 `test_comment_line_not_rewritten(self)` (method)
- L151 `TestIdempotence` (class) — Running the rewriter twice should be a no-op on its own output.
- L154 `test_already_rewritten(self)` (method)
- L160 `test_multiline_idempotent(self)` (method)
- L165 `TestEdgeCases` (class)
- L166 `test_only_chain_op_no_second_command(self)` (method)
- L172 `test_only_trailing_ampersand(self)` (method)
- L175 `test_leading_whitespace(self)` (method)
- L178 `test_tabs_between_tokens(self)` (method)
