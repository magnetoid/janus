---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_comment_rules.py

Symbols in `tests/gateway/test_feishu_comment_rules.py`.

- L27 `TestCommentDocumentRuleParsing` (class)
- L28 `test_parse_full_rule(self)` (method)
- L38 `test_parse_partial_rule(self)` (method)
- L44 `test_parse_empty_rule(self)` (method)
- L50 `test_invalid_policy_ignored(self)` (method)
- L55 `TestResolveRule` (class)
- L56 `test_exact_match(self)` (method)
- L68 `test_wildcard_match(self)` (method)
- L79 `test_top_level_fallback(self)` (method)
- L86 `test_exact_overrides_wildcard(self)` (method)
- L98 `test_field_by_field_fallback(self)` (method) — Exact sets policy, wildcard sets allow_from, enabled from top.
- L114 `test_explicit_empty_allow_from_does_not_fall_through(self)` (method) — allow_from=[] on exact should NOT inherit from wildcard or top.
- L129 `test_wiki_token_match(self)` (method)
- L140 `test_exact_takes_priority_over_wiki(self)` (method)
- L151 `test_default_config(self)` (method)
- L159 `TestHasWikiKeys` (class)
- L160 `test_no_wiki_keys(self)` (method)
- L167 `test_has_wiki_keys(self)` (method)
- L173 `test_empty_documents(self)` (method)
- L178 `TestIsUserAllowed` (class)
- L179 `test_allowlist_allows_listed(self)` (method)
- L183 `test_allowlist_denies_unlisted(self)` (method)
- L187 `test_allowlist_empty_denies_all(self)` (method)
- L191 `test_pairing_allows_in_allow_from(self)` (method)
- L195 `test_pairing_checks_store(self)` (method)
- L205 `TestMtimeCache` (class)
- L206 `test_returns_empty_dict_for_missing_file(self)` (method)
- L210 `test_reads_file_and_caches(self)` (method)
- L225 `test_reloads_on_mtime_change(self)` (method)
- L244 `TestLoadConfig` (class)
- L245 `test_load_with_documents(self)` (method)
- L271 `test_load_missing_file_returns_defaults(self)` (method)
- L280 `TestPairingStore` (class)
- L281 `setUp(self)` (method)
- L294 `tearDown(self)` (method)
- L301 `test_add_and_list(self)` (method)
- L306 `test_add_duplicate(self)` (method)
- L310 `test_remove(self)` (method)
- L315 `test_remove_nonexistent(self)` (method)
