---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/yuanbao_tools.py

Symbols in `tools/yuanbao_tools.py`.

- L28 `_get_active_adapter()` (function) — Lazy import to avoid ImportError when gateway.platforms.yuanbao is unavailable.
- L53 `get_group_info(group_code: str)` (function) — 查询群基本信息（群名、群主、成员数）。
- L82 `query_group_members(group_code: str, action: str='list_all', name: str='', mention: bool=False)` (function) — 统一的群成员查询工具（对齐 TS query_session_members）。
- L172 `search_sticker(query: str='', limit: int=10)` (function) — 在内置贴纸表中按关键词模糊搜索，返回 Top-N 候选。
- L208 `send_sticker(sticker: str='', chat_id: str='', reply_to: str='')` (function) — 向 chat_id（缺省取当前会话）发送一张内置贴纸（TIMFaceElem）。
- L290 `send_dm(group_code: str, name: str, message: str, user_id: str='', media_files: Optional[List[Tuple[str, bool]]]=None)` (function) — Send a DM (private chat message) to a group member, with optional media.
- L420 `_check_yuanbao()` (function) — Toolset availability check — True when running in a yuanbao gateway session.
- L431 `_handle_yb_query_group_info(args, **kw)` (function)
- L437 `_handle_yb_query_group_members(args, **kw)` (function)
- L446 `_handle_yb_send_dm(args, **kw)` (function)
- L485 `_handle_yb_search_sticker(args, **kw)` (function)
- L492 `_handle_yb_send_sticker(args, **kw)` (function)
