---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/feishu_comment_rules.py

Symbols in `gateway/platforms/feishu_comment_rules.py`.

- L43 `CommentDocumentRule` (class) — Per-document rule.  ``None`` means 'inherit from lower tier'.
- L51 `CommentsConfig` (class) — Top-level comment access config.
- L60 `ResolvedCommentRule` (class) — Fully resolved rule after field-by-field fallback.
- L72 `_MtimeCache` (class) — Generic mtime-based file cache.  ``stat()`` per access, re-read only on change.
- L75 `__init__(self, path: Path)` (method)
- L80 `load(self)` (method)
- L114 `_parse_frozenset(raw: Any)` (function) — Parse a list of strings into a frozenset; return None if key absent.
- L123 `_parse_document_rule(raw: dict)` (function)
- L136 `load_config()` (function) — Load comment rules from disk (mtime-cached).
- L165 `has_wiki_keys(cfg: CommentsConfig)` (function) — Check if any document rule key starts with 'wiki:'.
- L170 `resolve_rule(cfg: CommentsConfig, file_type: str, file_token: str, wiki_token: str='')` (function) — Resolve effective rule: exact doc → wiki key → wildcard → top-level → defaults.
- L224 `_load_pairing_approved()` (function) — Return set of approved user open_ids (mtime-cached).
- L235 `_save_pairing(data: dict)` (function)
- L246 `pairing_add(user_open_id: str)` (function) — Add a user to the pairing-approved list. Returns True if newly added.
- L260 `pairing_remove(user_open_id: str)` (function) — Remove a user from the pairing-approved list. Returns True if removed.
- L274 `pairing_list()` (function) — Return the approved dict  {user_open_id: {approved_at: ...}}.
- L285 `is_user_allowed(rule: ResolvedCommentRule, user_open_id: str)` (function) — Check if user passes the resolved rule's policy gate.
- L298 `_print_status()` (function)
- L331 `_do_check(doc_key: str, user_open_id: str)` (function)
- L350 `_main()` (function)
