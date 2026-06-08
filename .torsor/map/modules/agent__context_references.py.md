---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/context_references.py

Symbols in `agent/context_references.py`.

- L41 `ContextReference` (class)
- L52 `ContextReferenceResult` (class)
- L62 `parse_context_references(message: str)` (function)
- L105 `preprocess_context_references(message: str, *, cwd: str | Path, context_length: int, url_fetcher: Callable[[str], str | Awaitable[str]] | None=None, allowed_root: str | Path | None=None)` (function)
- L132 `preprocess_context_references_async(message: str, *, cwd: str | Path, context_length: int, url_fetcher: Callable[[str], str | Awaitable[str]] | None=None, allowed_root: str | Path | None=None)` (function)
- L206 `_expand_reference(ref: ContextReference, cwd: Path, *, url_fetcher: Callable[[str], str | Awaitable[str]] | None=None, allowed_root: Path | None=None)` (function)
- L236 `_expand_file_reference(ref: ContextReference, cwd: Path, *, allowed_root: Path | None=None)` (function)
- L263 `_expand_folder_reference(ref: ContextReference, cwd: Path, *, allowed_root: Path | None=None)` (function)
- L280 `_expand_git_reference(ref: ContextReference, cwd: Path, args: list[str], label: str)` (function)
- L305 `_fetch_url_content(url: str, *, url_fetcher: Callable[[str], str | Awaitable[str]] | None=None)` (function)
- L317 `_default_url_fetcher(url: str)` (function)
- L329 `_resolve_path(cwd: Path, target: str, *, allowed_root: Path | None=None)` (function)
- L342 `_ensure_reference_path_allowed(path: Path)` (function)
- L363 `_strip_trailing_punctuation(value: str)` (function)
- L375 `_strip_reference_wrappers(value: str)` (function)
- L381 `_parse_file_reference_value(value: str)` (function)
- L407 `_remove_reference_tokens(message: str, refs: list[ContextReference])` (function)
- L420 `_is_binary_file(path: Path)` (function)
- L430 `_build_folder_listing(path: Path, cwd: Path, limit: int=200)` (function)
- L446 `_iter_visible_entries(path: Path, cwd: Path, limit: int)` (function)
- L477 `_rg_files(path: Path, cwd: Path, limit: int)` (function)
- L494 `_file_metadata(path: Path)` (function)
- L504 `_code_fence_language(path: Path)` (function)
