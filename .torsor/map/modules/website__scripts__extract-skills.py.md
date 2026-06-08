---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# website/scripts/extract-skills.py

Symbols in `website/scripts/extract-skills.py`.

- L114 `_extract_overview(body: str)` (function) — Pull the first non-heading paragraph from a SKILL.md body.
- L141 `_docs_page_path(rel_dir: str, source_label: str)` (function) — Compute the per-skill docs-site URL slug for a given SKILL.md location.
- L165 `_install_command(source: str, identifier: str, name: str)` (function) — Build the ``hermes skills install …`` command for a unified-index entry.
- L196 `_source_url(source: str, identifier: str, extra: dict)` (function) — Best-effort clickable URL to the skill's origin (repo / detail page).
- L250 `extract_local_skills()` (function)
- L333 `_label_for_github_identifier(identifier: str)` (function) — Return a friendly source label for a unified-index 'github' entry.
- L343 `extract_unified_index_skills()` (function) — Read website/static/api/skills-index.json — the canonical multi-source index.
- L444 `extract_legacy_cache_skills()` (function) — Read the deprecated skills/index-cache/ snapshots — fallback only.
- L562 `_guess_category(tags: list)` (function) — Map a skill's tags to a curated category, or 'uncategorized'.
- L592 `_consolidate_small_categories(skills: list)` (function)
- L621 `main()` (function)
