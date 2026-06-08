---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/yuanbao_sticker.py

Symbols in `gateway/platforms/yuanbao_sticker.py`.

- L331 `get_sticker_by_name(name: str)` (function) — 按名称查找贴纸，支持模糊匹配。
- L364 `get_random_sticker(category: str=None)` (function) — 随机返回一个贴纸。
- L381 `get_sticker_by_id(sticker_id: str)` (function) — 按 sticker_id 精确查找贴纸。
- L399 `_normalize_text(raw: str)` (function)
- L403 `_compact_text(raw: str)` (function)
- L407 `_multiset_char_hit_ratio(needle: str, haystack: str)` (function)
- L422 `_bigram_jaccard(a: str, b: str)` (function)
- L432 `_longest_subsequence_ratio(needle: str, haystack: str)` (function)
- L444 `_score_field(haystack: str, query: str)` (function)
- L468 `search_stickers(query: str, limit: int=10)` (function) — 在内置贴纸表中按模糊匹配排序返回前 N 条结果。
- L511 `build_face_msg_body(face_index: int, face_type: int=1, data: Optional[str]=None)` (function) — 构造 TIMFaceElem 消息体。
- L540 `build_sticker_msg_body(sticker: dict)` (function) — 从 STICKER_MAP 中的 sticker dict 直接构造 TIMFaceElem 消息体。
