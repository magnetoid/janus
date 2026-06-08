---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/qqbot/chunked_upload.py

Symbols in `gateway/platforms/qqbot/chunked_upload.py`.

- L72 `UploadDailyLimitExceededError` (class) — Raised when ``upload_prepare`` returns biz_code 40093002.
- L80 `__init__(self, file_name: str, file_size: int, message: str='')` (method)
- L88 `file_size_human(self)` (method)
- L92 `UploadFileTooLargeError` (class) — Raised when a file exceeds the platform per-file size limit.
- L95 `__init__(self, file_name: str, file_size: int, limit_bytes: int=0, message: str='')` (method)
- L115 `file_size_human(self)` (method)
- L119 `limit_human(self)` (method)
- L126 `_UploadProgress` (class)
- L136 `_PreparePart` (class)
- L143 `_PrepareResult` (class)
- L151 `_parse_prepare_response(raw: Dict[str, Any])` (function) — Parse the upload_prepare API response into a normalized shape.
- L200 `ChunkedUploader` (class) — Run the prepare → PUT parts → complete sequence.
- L211 `__init__(self, api_request: ApiRequestFn, http_put: Callable[..., Awaitable[Any]], log_tag: str='QQBot')` (method)
- L221 `upload(self, chat_type: str, target_id: str, file_path: str, file_type: int, file_name: str)` (method) — Run the full chunked upload and return the ``complete_upload`` response.
- L310 `_prepare(self, chat_type: str, target_id: str, file_type: int, file_name: str, file_size: int, hashes: Dict[str, str])` (method)
- L346 `_upload_one_part(self, chat_type: str, target_id: str, file_path: str, file_size: int, upload_id: str, rsp_block_size: int, part: _PreparePart, retry_timeout: float, progress: _UploadProgress)` (method) — PUT one part to COS, then call ``upload_part_finish``.
- L393 `_put_to_presigned_url(self, url: str, data: bytes, part_index: int, total_parts: int)` (method) — PUT part data to a pre-signed COS URL with retry.
- L443 `_part_finish_with_retry(self, chat_type: str, target_id: str, upload_id: str, part_index: int, block_size: int, md5: str, retry_timeout: float)` (method) — Call ``upload_part_finish``, retrying on biz_code 40093001.
- L494 `_complete(self, chat_type: str, target_id: str, upload_id: str)` (method) — Call ``complete_upload`` with retry.
- L533 `format_size(size_bytes: int)` (function) — Return a human-readable file size string (e.g. ``'12.3 MB'``).
- L543 `_read_file_chunk(file_path: str, offset: int, length: int)` (function) — Read *length* bytes from *file_path* starting at *offset*.
- L559 `_compute_file_hashes(file_path: str, file_size: int)` (function) — Compute md5, sha1, and md5_10m in a single pass.
- L590 `_run_with_concurrency(tasks: List[Callable[[], Awaitable[None]]], concurrency: int)` (function) — Run a list of thunks with a bounded number in flight at once.
