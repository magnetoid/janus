---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/file_operations.py

Symbols in `tools/file_operations.py`.

- L59 `_strip_terminal_fence_leaks(text: str)` (function) — Strip leaked terminal fence wrappers from file read output.
- L76 `_detect_line_ending(sample: str)` (function) — Return the dominant line ending in ``sample`` or None if undetermined.
- L98 `_normalize_line_endings(text: str, target: str)` (function) — Convert all line endings in ``text`` to ``target`` (``\n`` or ``\r\n``).
- L130 `_strip_bom(text: str)` (function) — Return (text-without-leading-BOM, had_bom).
- L141 `_has_bom(text: Optional[str])` (function) — True if ``text`` begins with a UTF-8 BOM.
- L146 `_is_write_denied(path: str)` (function) — Return True if path is on the write deny list.
- L156 `ReadResult` (class) — Result from reading a file.
- L171 `to_dict(self)` (method)
- L176 `WriteResult` (class) — Result from writing a file.
- L191 `to_dict(self)` (method)
- L196 `PatchResult` (class) — Result from patching a file.
- L208 `to_dict(self)` (method)
- L228 `SearchMatch` (class) — A single search match.
- L237 `SearchResult` (class) — Result from searching.
- L246 `to_dict(self)` (method)
- L265 `LintResult` (class) — Result from linting a file.
- L272 `to_dict(self)` (method)
- L282 `ExecuteResult` (class) — Result from executing a shell command.
- L288 `_split_tool_diagnostics(output: str)` (function) — Separate rg/grep diagnostic lines from real match output.
- L345 `_parse_search_context_line(line: str)` (function) — Parse grep/rg context output in ``path-line-content`` format.
- L374 `FileOperations` (class) — Abstract interface for file operations across terminal backends.
- L378 `read_file(self, path: str, offset: int=1, limit: int=500)` (method) — Read a file with pagination support.
- L383 `read_file_raw(self, path: str)` (method) — Read the complete file content as a plain string.
- L393 `write_file(self, path: str, content: str)` (method) — Write content to a file, creating directories as needed.
- L398 `patch_replace(self, path: str, old_string: str, new_string: str, replace_all: bool=False)` (method) — Replace text in a file using fuzzy matching.
- L404 `patch_v4a(self, patch_content: str)` (method) — Apply a V4A format patch.
- L409 `delete_file(self, path: str)` (method) — Delete a file. Returns WriteResult with .error set on failure.
- L413 `delete_path(self, path: str, recursive: bool=False)` (method) — Cross-platform delete that handles files and (with recursive=True)
- L424 `move_file(self, src: str, dst: str)` (method) — Move/rename a file from src to dst. Returns WriteResult with .error set on failure.
- L429 `search(self, pattern: str, path: str='.', target: str='content', file_glob: Optional[str]=None, limit: int=50, offset: int=0, output_mode: str='content', context: int=0)` (method) — Search for content or files.
- L526 `_looks_like_linter_unusable(base_cmd: str, output: str)` (function) — Return True iff ``output`` from ``base_cmd`` indicates the linter
- L542 `_lint_json_inproc(content: str)` (function) — In-process JSON syntax check.  Returns (ok, error_message).
- L554 `_lint_yaml_inproc(content: str)` (function) — In-process YAML syntax check.  Returns (ok, error_message).
- L573 `_lint_toml_inproc(content: str)` (function) — In-process TOML syntax check (stdlib tomllib, Python 3.11+).
- L590 `_lint_python_inproc(content: str)` (function) — In-process Python syntax check via ast.parse.
- L631 `_coerce_int(value: Any, default: int)` (function) — Best-effort integer coercion for tool pagination inputs.
- L639 `normalize_read_pagination(offset: Any=DEFAULT_READ_OFFSET, limit: Any=DEFAULT_READ_LIMIT)` (function) — Return safe read_file pagination bounds.
- L658 `normalize_search_pagination(offset: Any=DEFAULT_SEARCH_OFFSET, limit: Any=DEFAULT_SEARCH_LIMIT)` (function) — Return safe search pagination bounds for shell head/tail pipelines.
- L666 `ShellFileOperations` (class) — File operations implemented via shell commands.
- L674 `__init__(self, terminal_env, cwd: str=None)` (method) — Initialize file operations with a terminal environment.
- L709 `_exec(self, command: str, cwd: str=None, timeout: int=None, stdin_data: str=None)` (method) — Execute command via terminal backend.
- L741 `_has_command(self, cmd: str)` (method) — Check if a command exists in the environment (cached).
- L748 `_is_likely_binary(self, path: str, content_sample: str=None)` (method) — Check if a file is likely binary.
- L766 `_is_image(self, path: str)` (method) — Check if file is an image we can return as base64.
- L771 `_add_line_numbers(self, content: str, start_line: int=1)` (method) — Add line numbers to content in ``LINE_NUM|CONTENT`` format.
- L797 `_expand_path(self, path: str)` (method) — Expand shell-style paths like ~ and ~user to absolute paths.
- L834 `_escape_shell_arg(self, arg: str)` (method) — Escape a string for safe use in shell commands.
- L839 `_atomic_write(self, path: str, content: str)` (method) — Write ``content`` to ``path`` atomically via temp-file + rename.
- L893 `_detect_file_line_ending(self, path: str, pre_content: Optional[str]=None)` (method) — Detect the dominant line ending of a file on disk.
- L914 `_file_has_bom(self, path: str, pre_content: Optional[str]=None)` (method) — Whether the file on disk starts with a UTF-8 BOM.
- L931 `_unified_diff(self, old_content: str, new_content: str, filename: str)` (method) — Generate unified diff between old and new content.
- L946 `read_file(self, path: str, offset: int=1, limit: int=500)` (method) — Read a file with pagination, binary detection, and line numbers.
- L1043 `_suggest_similar_files(self, path: str)` (method) — Suggest similar files when the requested file is not found.
- L1095 `read_file_raw(self, path: str)` (method) — Read the complete file content as a plain string.
- L1134 `delete_file(self, path: str)` (method) — Delete a single file.
- L1144 `delete_path(self, path: str, recursive: bool=False)` (method) — Cross-platform delete that handles files and (with recursive=True)
- L1152 `_python_delete(self, path: str, recursive: bool)` (method)
- L1195 `move_file(self, src: str, dst: str)` (method) — Move a file via mv.
- L1213 `write_file(self, path: str, content: str)` (method) — Write content to a file, creating parent directories as needed.
- L1367 `patch_replace(self, path: str, old_string: str, new_string: str, replace_all: bool=False)` (method) — Replace text in a file using fuzzy matching.
- L1490 `patch_v4a(self, patch_content: str)` (method) — Apply a V4A format patch.
- L1520 `_check_lint(self, path: str, content: Optional[str]=None)` (method) — Run syntax check on a file after editing.
- L1608 `_check_lint_delta(self, path: str, pre_content: Optional[str], post_content: Optional[str]=None)` (method) — Run post-write syntax lint with pre-write baseline comparison.
- L1693 `_lsp_local_only(self)` (method) — Return True iff this FileOperations is wired to a local backend.
- L1714 `_lsp_handles_extension(self, ext: str)` (method) — Return True iff some registered LSP server claims this extension.
- L1737 `_lsp_will_handle(self, path: str)` (method) — Return True iff the LSP service is active AND will lint this file.
- L1771 `_snapshot_lsp_baseline(self, path: str)` (method) — Capture pre-edit LSP diagnostics so the post-write delta is correct.
- L1794 `_maybe_lsp_diagnostics(self, path: str, *, pre_content: Optional[str]=None, post_content: Optional[str]=None)` (method) — Best-effort LSP semantic diagnostics for ``path``.
- L1864 `search(self, pattern: str, path: str='.', target: str='content', file_glob: Optional[str]=None, limit: int=50, offset: int=0, output_mode: str='content', context: int=0)` (method) — Search for content or files.
- L1927 `_search_files(self, pattern: str, path: str, limit: int, offset: int)` (method) — Search for files by name pattern (glob-like).
- L2009 `_search_files_rg(self, pattern: str, path: str, limit: int, offset: int)` (method) — Search for files by name using ripgrep's --files mode.
- L2052 `_search_content(self, pattern: str, path: str, file_glob: Optional[str], limit: int, offset: int, output_mode: str, context: int)` (method) — Search for content inside files (grep-like).
- L2069 `_search_with_rg(self, pattern: str, path: str, file_glob: Optional[str], limit: int, offset: int, output_mode: str, context: int)` (method) — Search using ripgrep.
- L2183 `_search_with_grep(self, pattern: str, path: str, file_glob: Optional[str], limit: int, offset: int, output_mode: str, context: int)` (method) — Fallback search using grep.
