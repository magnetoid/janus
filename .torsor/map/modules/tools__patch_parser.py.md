---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/patch_parser.py

Symbols in `tools/patch_parser.py`.

- L38 `OperationType` (class)
- L46 `HunkLine` (class) — A single line in a patch hunk.
- L53 `Hunk` (class) — A group of changes within a file.
- L60 `PatchOperation` (class) — A single operation in a V4A patch.
- L69 `parse_v4a_patch(patch_content: str)` (function) — Parse a V4A format patch.
- L227 `_count_occurrences(text: str, pattern: str)` (function) — Count non-overlapping occurrences of *pattern* in *text*.
- L240 `_validate_operations(operations: List[PatchOperation], file_ops: Any)` (function) — Validate all operations without writing any files.
- L331 `apply_v4a_operations(operations: List[PatchOperation], file_ops: Any)` (function) — Apply V4A patch operations using a file operations interface.
- L455 `_apply_add(op: PatchOperation, file_ops: Any)` (function) — Apply an add file operation.
- L483 `_apply_delete(op: PatchOperation, file_ops: Any)` (function) — Apply a delete file operation.
- L504 `_apply_move(op: PatchOperation, file_ops: Any)` (function) — Apply a move file operation.
- L514 `_apply_update(op: PatchOperation, file_ops: Any)` (function) — Apply an update file operation.
