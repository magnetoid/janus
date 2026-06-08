---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/website/test_generate_skill_docs.py

Symbols in `tests/website/test_generate_skill_docs.py`.

- L25 `gen_module()` (function) — Load generate-skill-docs.py as a module (hyphenated filename, not importable via normal import).
- L34 `test_code_block_without_box_chars_is_not_wrapped(gen_module)` (function) — Plain bash/python code blocks should stay uncluttered.
- L42 `test_code_block_with_box_chars_gets_wrapped(gen_module)` (function) — A code fence containing Unicode box-drawing chars must be wrapped in
- L64 `test_multiple_code_blocks_only_box_ones_wrapped(gen_module)` (function) — Mixed body: plain code stays plain, box code gets wrapped.
- L80 `test_tilde_fenced_box_is_wrapped(gen_module)` (function) — The generator supports both ``` and ~~~ fences — both must be covered.
- L87 `test_already_wrapped_source_double_wraps_harmlessly(gen_module)` (function) — If the SKILL.md already has ascii-guard-ignore markers, the generator's
- L103 `test_box_drawing_detection_covers_common_chars(gen_module)` (function) — Smoke-test that the char set covers box-drawing ranges actually used
- L111 `test_bundled_catalog_explains_missing_local_skills(gen_module)` (function) — The bundled catalog should explain how to restore a listed skill that
