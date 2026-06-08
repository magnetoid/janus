---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_yuanbao_markdown.py

Symbols in `tests/test_yuanbao_markdown.py`.

- L24 `TestHasUnclosedFence` (class)
- L25 `test_unclosed_fence(self)` (method)
- L28 `test_closed_fence(self)` (method)
- L31 `test_empty(self)` (method)
- L34 `test_no_fence(self)` (method)
- L37 `test_multiple_closed_fences(self)` (method)
- L41 `test_second_fence_unclosed(self)` (method)
- L45 `test_fence_at_start(self)` (method)
- L48 `test_inline_backtick_ignored(self)` (method)
- L55 `TestEndsWithTableRow` (class)
- L56 `test_simple_table_row(self)` (method)
- L59 `test_table_row_with_trailing_newline(self)` (method)
- L62 `test_table_row_in_middle(self)` (method)
- L66 `test_empty(self)` (method)
- L69 `test_non_table(self)` (method)
- L72 `test_only_pipe_start(self)` (method)
- L75 `test_table_separator_row(self)` (method)
- L78 `test_whitespace_only(self)` (method)
- L84 `TestSplitAtParagraphBoundary` (class)
- L85 `test_split_at_empty_line(self)` (method)
- L91 `test_split_at_sentence_end(self)` (method)
- L97 `test_forced_split_no_boundary(self)` (method)
- L103 `test_split_at_newline(self)` (method)
- L109 `test_chinese_sentence_boundary(self)` (method)
- L118 `TestChunkMarkdownText` (class)
- L119 `test_empty(self)` (method)
- L122 `test_short_text_no_split(self)` (method)
- L126 `test_exactly_max_chars(self)` (method)
- L132 `test_plain_text_split(self)` (method) — x * 9000 should return 3 chunks of ~3000
- L141 `test_5000_chars_returns_2(self)` (method) — 验收标准: 'a'*5000 with max 3000 → 2 chunks
- L146 `test_code_fence_not_split(self)` (method) — 代码块不应被切断
- L155 `test_table_not_split(self)` (method) — 表格行不应被切断
- L166 `test_code_fence_200_lines_not_cut(self)` (method) — 包含 200 行代码块的文本，代码块不被切断
- L174 `test_multiple_paragraphs(self)` (method) — 多段落文本应在段落边界切割
- L184 `test_single_long_line(self)` (method) — 单行超长文本应被强制切割
- L192 `test_fence_followed_by_text(self)` (method) — 围栏后的文本应正常切割
- L199 `test_returns_non_empty_strings(self)` (method) — 所有返回的片段都应为非空字符串
- L209 `TestAcceptanceCriteria` (class)
- L210 `test_9000_x_returns_3_chunks(self)` (method) — 验收：MarkdownProcessor.chunk_markdown_text("x" * 9000, 3000) 返回 3 个片段
- L217 `test_5000_a_returns_2_chunks(self)` (method) — 验收：python -c 输出 2
- L222 `test_has_unclosed_fence_true(self)` (method) — 验收：MarkdownProcessor.has_unclosed_fence("```python\ncode") 返回 True
- L226 `test_has_unclosed_fence_false(self)` (method) — 验收：MarkdownProcessor.has_unclosed_fence("```python\ncode\n```") 返回 False
- L230 `test_code_block_200_lines_not_broken(self)` (method) — 验收：包含 200 行代码块的文本，代码块不被切断
- L239 `test_table_rows_not_broken(self)` (method) — 验收：表格行不被切断（每个 chunk 中的表格 fence 完整）
- L256 `test_short_text_no_split()` (function)
- L260 `test_plain_text_split()` (function)
- L267 `test_fence_not_broken()` (function) — 代码块不应被切断
- L275 `test_large_fence_kept_whole()` (function) — 超大代码块即便超过 max_chars 也应整块输出
- L285 `test_mixed_content()` (function) — 代码块前后的普通文本可以正常切割
- L293 `test_table_not_broken()` (function) — 表格不应被切断
- L306 `test_has_unclosed_fence()` (function)
- L312 `test_ends_with_table_row()` (function)
- L317 `test_empty_text()` (function)
- L321 `test_exact_limit()` (function)
