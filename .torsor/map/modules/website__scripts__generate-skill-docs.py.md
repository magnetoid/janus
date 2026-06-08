---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# website/scripts/generate-skill-docs.py

Symbols in `website/scripts/generate-skill-docs.py`.

- L47 `_wrap_ascii_art_code_blocks(code_segment: str)` (function) — Wrap a fenced code segment in ascii-guard-ignore markers if it contains
- L65 `mdx_escape_body(body: str)` (function) — Escape MDX-dangerous characters in markdown body, leaving fenced code blocks alone.
- L226 `rewrite_relative_links(body: str, meta: dict[str, Any])` (function) — Rewrite references/foo.md style links in the SKILL.md body.
- L254 `parse_skill_md(path: Path)` (function)
- L269 `sanitize_yaml_string(s: str)` (function) — Make a string safe to embed in a YAML double-quoted scalar.
- L277 `derive_skill_meta(skill_path: Path, source_dir: Path, source_kind: str)` (function) — Extract category + skill slug from filesystem layout.
- L307 `page_id(meta: dict[str, Any])` (function) — Stable slug used for filename + sidebar id.
- L314 `page_output_path(meta: dict[str, Any])` (function)
- L323 `sidebar_doc_id(meta: dict[str, Any])` (function) — Docusaurus sidebar id, relative to docs/.
- L328 `render_skill_page(meta: dict[str, Any], fm: dict[str, Any], body: str, skill_index: dict[str, dict[str, Any]] | None=None)` (function)
- L452 `discover_skills()` (function)
- L462 `build_catalog_md_bundled(entries: list[tuple[dict[str, Any], dict[str, Any]]])` (function)
- L508 `build_catalog_md_optional(entries: list[tuple[dict[str, Any], dict[str, Any]]])` (function)
- L581 `build_sidebar_items(entries: list[tuple[dict[str, Any], dict[str, Any]]])` (function) — Build a dict representing the Skills sidebar tree.
- L630 `_render_sidebar_item(item: Any, indent: int)` (function) — Render one sidebar item (string doc id, or category dict) as ts lines.
- L653 `write_sidebar(entries)` (function)
- L735 `main()` (function)
