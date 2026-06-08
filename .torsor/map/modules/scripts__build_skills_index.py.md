---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/build_skills_index.py

Symbols in `scripts/build_skills_index.py`.

- L52 `_meta_to_dict(meta: SkillMeta)` (function) — Convert a SkillMeta to a serializable dict.
- L67 `crawl_source(source, source_name: str, limit: int)` (function) — Crawl a single source and return skill dicts.
- L82 `crawl_skills_sh(source: SkillsShSource)` (function) — Crawl skills.sh via its sitemap to enumerate the full catalog (~20k entries).
- L111 `_fetch_repo_tree(repo: str, auth: GitHubAuth)` (function) — Fetch the recursive tree for a repo. Returns list of tree entries.
- L138 `batch_resolve_paths(skills: list, auth: GitHubAuth)` (function) — Resolve GitHub paths for skills.sh entries using batch tree lookups.
- L243 `main()` (function)
