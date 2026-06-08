---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_comment.py

Symbols in `tests/gateway/test_feishu_comment.py`.

- L15 `_make_event(comment_id='c1', reply_id='r1', notice_type='add_reply', file_token='docx_token', file_type='docx', from_open_id='ou_user', to_open_id='ou_bot', is_mentioned=True)` (function) — Build a minimal drive comment event SimpleNamespace.
- L42 `TestParseEvent` (class)
- L43 `test_parse_valid_event(self)` (method)
- L52 `test_parse_missing_event_attr(self)` (method)
- L55 `test_parse_none_event(self)` (method)
- L59 `TestEventFiltering` (class) — Test the filtering logic in handle_drive_comment_event.
- L62 `_run(self, coro)` (method)
- L68 `test_self_reply_filtered(self, mock_allowed, mock_resolve, mock_load)` (method) — Events where from_open_id == self_open_id should be dropped.
- L79 `test_wrong_receiver_filtered(self, mock_allowed, mock_resolve, mock_load)` (method) — Events where to_open_id != self_open_id should be dropped.
- L90 `test_empty_to_open_id_filtered(self, mock_allowed, mock_resolve, mock_load)` (method) — Events with empty to_open_id should be dropped.
- L101 `test_invalid_notice_type_filtered(self, mock_allowed, mock_resolve, mock_load)` (method) — Events with unsupported notice_type should be dropped.
- L109 `test_allowed_notice_types(self)` (method)
- L115 `TestAccessControlIntegration` (class)
- L116 `_run(self, coro)` (method)
- L123 `test_denied_user_no_side_effects(self, mock_load, mock_resolve, mock_allowed, mock_wiki_keys)` (method) — Denied user should not trigger typing reaction or agent.
- L142 `test_disabled_comment_skipped(self, mock_load, mock_resolve, mock_allowed, mock_wiki_keys)` (method) — Disabled comments should return immediately.
- L155 `TestSanitizeCommentText` (class)
- L156 `test_angle_brackets_escaped(self)` (method)
- L159 `test_ampersand_escaped_first(self)` (method)
- L162 `test_ampersand_not_double_escaped(self)` (method)
- L168 `test_plain_text_unchanged(self)` (method)
- L171 `test_empty_string(self)` (method)
- L174 `test_code_snippet(self)` (method)
- L183 `TestWikiReverseLookup` (class)
- L184 `_run(self, coro)` (method)
- L188 `test_reverse_lookup_success(self, mock_exec)` (method)
- L204 `test_reverse_lookup_not_wiki(self, mock_exec)` (method)
- L212 `test_reverse_lookup_service_error(self, mock_exec)` (method)
- L227 `test_wiki_lookup_triggered_when_no_exact_match(self, mock_meta, mock_batch, mock_reaction, mock_load, mock_resolve, mock_allowed, mock_wiki_keys, mock_lookup)` (method) — Wiki reverse lookup should fire when rule falls to wildcard/top and wiki keys exist.
