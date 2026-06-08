---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/feishu_comment.py

Symbols in `gateway/platforms/feishu_comment.py`.

- L37 `_build_request(method: str, uri: str, paths=None, queries=None, body=None)` (function) — Build a lark_oapi BaseRequest.
- L60 `_exec_request(client, method, uri, paths=None, queries=None, body=None)` (function) — Execute a lark API request and return (code, msg, data_dict).
- L103 `parse_drive_comment_event(data: Any)` (function) — Extract structured fields from a ``drive.notice.comment_add_v1`` payload.
- L156 `add_comment_reaction(client: Any, *, file_token: str, file_type: str, reply_id: str, reaction_type: str='OK')` (function) — Add an emoji reaction to a document comment reply.
- L206 `delete_comment_reaction(client: Any, *, file_token: str, file_type: str, reply_id: str, reaction_type: str='OK')` (function) — Remove an emoji reaction from a document comment reply.
- L258 `query_document_meta(client: Any, file_token: str, file_type: str)` (function) — Fetch document title and URL via batch_query meta API.
- L304 `batch_query_comment(client: Any, file_token: str, file_type: str, comment_id: str)` (function) — Fetch comment details via batch_query comment API.
- L355 `list_whole_comments(client: Any, file_token: str, file_type: str)` (function) — List all whole-document comments (paginated, up to 500).
- L398 `list_comment_replies(client: Any, file_token: str, file_type: str, comment_id: str, *, expect_reply_id: str='')` (function) — List all replies in a comment thread (paginated, up to 500).
- L465 `_sanitize_comment_text(text: str)` (function) — Escape characters not allowed in Feishu comment text_run content.
- L470 `reply_to_comment(client: Any, file_token: str, file_type: str, comment_id: str, text: str)` (function) — Post a reply to a local comment thread.
- L504 `add_whole_comment(client: Any, file_token: str, file_type: str, text: str)` (function) — Add a new whole-document comment.
- L536 `_chunk_text(text: str, limit: int=_REPLY_CHUNK_SIZE)` (function) — Split text into chunks for delivery, preferring line breaks.
- L554 `deliver_comment_reply(client: Any, file_token: str, file_type: str, comment_id: str, text: str, is_whole: bool)` (function) — Route agent reply to the correct API, chunking long text.
- L602 `_extract_reply_text(reply: Dict[str, Any])` (function) — Extract plain text from a comment reply's content structure.
- L626 `_get_reply_user_id(reply: Dict[str, Any])` (function) — Extract user_id from a reply dict.
- L634 `_extract_semantic_text(reply: Dict[str, Any], self_open_id: str='')` (function) — Extract semantic text from a reply, stripping self @mentions and extra whitespace.
- L678 `_extract_docs_links(replies: List[Dict[str, Any]])` (function) — Extract unique document links from a list of comment replies.
- L711 `_reverse_lookup_wiki_token(client: Any, obj_type: str, obj_token: str)` (function) — Reverse-lookup: given an obj_token, find its wiki node_token.
- L732 `_resolve_wiki_nodes(client: Any, links: List[Dict[str, str]])` (function) — Resolve wiki links to their underlying document type and token.
- L770 `_format_referenced_docs(links: List[Dict[str, str]], current_file_token: str='')` (function) — Format resolved document links for prompt embedding.
- L795 `_truncate(text: str, limit: int=_PROMPT_TEXT_LIMIT)` (function) — Truncate text for prompt embedding.
- L802 `_select_local_timeline(timeline: List[Tuple[str, str, bool]], target_index: int)` (function) — Select up to _LOCAL_TIMELINE_LIMIT entries centered on target_index.
- L833 `_select_whole_timeline(timeline: List[Tuple[str, str, bool]], current_index: int, nearest_self_index: int)` (function) — Select up to _WHOLE_TIMELINE_LIMIT entries for whole-doc comments.
- L884 `build_local_comment_prompt(*, doc_title: str, doc_url: str, file_token: str, file_type: str, comment_id: str, quote_text: str, root_comment_text: str, target_reply_text: str, timeline: List[Tuple[str, str, bool]], self_open_id: str, target_index: int=-1, referenced_docs: str='')` (function) — Build the prompt for a local (quoted-text) comment.
- L929 `build_whole_comment_prompt(*, doc_title: str, doc_url: str, file_token: str, file_type: str, comment_text: str, timeline: List[Tuple[str, str, bool]], self_open_id: str, current_index: int=-1, nearest_self_index: int=-1, referenced_docs: str='')` (function) — Build the prompt for a whole-document comment.
- L975 `_resolve_model_and_runtime()` (function) — Resolve model and provider credentials, same as gateway message handling.
- L1010 `_session_key(file_type: str, file_token: str)` (function)
- L1014 `_load_session_history(key: str)` (function) — Load conversation history for a document session.
- L1029 `_save_session_history(key: str, messages: List[Dict[str, Any]])` (function) — Save conversation history for a document session (keeps last N messages).
- L1047 `_run_comment_agent(prompt: str, client: Any, session_key: str='')` (function) — Create an AIAgent with feishu tools and run the prompt.
- L1120 `handle_drive_comment_event(client: Any, data: Any, *, self_open_id: str='')` (function) — Full orchestration for a drive comment event.
