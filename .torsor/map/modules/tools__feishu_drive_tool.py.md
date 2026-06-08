---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/feishu_drive_tool.py

Symbols in `tools/feishu_drive_tool.py`.

- L20 `set_client(client)` (function) — Store a lark client for the current thread (called by feishu_comment).
- L25 `get_client()` (function) — Return the lark client for the current thread, or None.
- L30 `_check_feishu()` (function)
- L40 `_do_request(client, method, uri, paths=None, queries=None, body=None)` (function) — Build and execute a BaseRequest, return (code, msg, data_dict).
- L133 `_handle_list_comments(args: dict, **kwargs)` (function)
- L208 `_handle_list_replies(args: dict, **kwargs)` (function)
- L280 `_handle_reply_comment(args: dict, **kwargs)` (function)
- L351 `_handle_add_comment(args: dict, **kwargs)` (function)
