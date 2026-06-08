---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/display.py

Symbols in `agent/display.py`.

- L33 `_diff_ansi()` (function) — Return ANSI escapes for diff display, resolved from the active skin.
- L82 `_diff_dim()` (function)
- L83 `_diff_file()` (function)
- L84 `_diff_hunk()` (function)
- L85 `_diff_minus()` (function)
- L86 `_diff_plus()` (function)
- L92 `LocalEditSnapshot` (class) — Pre-tool filesystem snapshot used to render diffs locally after writes.
- L104 `set_tool_preview_max_len(n: int)` (function) — Set the global max length for tool call previews. 0 = no limit.
- L110 `get_tool_preview_max_len()` (function) — Return the configured max preview length (0 = unlimited).
- L119 `_get_skin()` (function) — Get the active skin config, or None if not available.
- L128 `get_skin_tool_prefix()` (function) — Get tool output prefix character from active skin.
- L136 `get_tool_emoji(tool_name: str, default: str='⚡')` (function) — Get the display emoji for a tool.
- L166 `_oneline(text: str)` (function) — Collapse whitespace (including newlines) to single spaces.
- L171 `build_tool_preview(tool_name: str, args: dict, max_len: int | None=None)` (function) — Build a short preview of a tool call's primary argument for display.
- L269 `_resolved_path(path: str)` (function) — Resolve a possibly-relative filesystem path against the current cwd.
- L277 `_snapshot_text(path: Path)` (function) — Return UTF-8 file content, or None for missing/unreadable files.
- L285 `_display_diff_path(path: Path)` (function) — Prefer cwd-relative paths in diffs when available.
- L293 `_resolve_skill_manage_paths(args: dict)` (function) — Resolve skill_manage write targets to filesystem paths.
- L323 `_resolve_local_edit_paths(tool_name: str, function_args: dict | None)` (function) — Resolve local filesystem targets for write-capable tools.
- L342 `capture_local_edit_snapshot(tool_name: str, function_args: dict | None)` (function) — Capture before-state for local write previews.
- L354 `_result_succeeded(result: str | None)` (function) — Conservatively detect whether a tool result represents success.
- L370 `_diff_from_snapshot(snapshot: LocalEditSnapshot | None)` (function) — Generate unified diff text from a stored before-state and current files.
- L399 `extract_edit_diff(tool_name: str, result: str | None, *, function_args: dict | None=None, snapshot: LocalEditSnapshot | None=None)` (function) — Extract a unified diff from a file-edit tool result.
- L421 `_emit_inline_diff(diff_text: str, print_fn)` (function) — Emit rendered diff text through the CLI's prompt_toolkit-safe printer.
- L434 `_render_inline_unified_diff(diff: str)` (function) — Render unified diff lines in Hermes' inline transcript style.
- L467 `_split_unified_diff_sections(diff: str)` (function) — Split a unified diff into per-file sections.
- L485 `_summarize_rendered_diff_sections(diff: str, *, max_files: int=_MAX_INLINE_DIFF_FILES, max_lines: int=_MAX_INLINE_DIFF_LINES)` (function) — Render diff sections while capping file count and total line count.
- L530 `render_edit_diff_with_delta(tool_name: str, result: str | None, *, function_args: dict | None=None, snapshot: LocalEditSnapshot | None=None, print_fn=None)` (function) — Render an edit diff inline without taking over the terminal UI.
- L559 `KawaiiSpinner` (class) — Animated spinner with kawaii faces for CLI feedback during tool execution.
- L592 `get_waiting_faces(cls)` (method) — Return waiting faces from the active skin, falling back to KAWAII_WAITING.
- L605 `get_thinking_faces(cls)` (method) — Return thinking faces from the active skin, falling back to KAWAII_THINKING.
- L618 `get_thinking_verbs(cls)` (method) — Return thinking verbs from the active skin, falling back to THINKING_VERBS.
- L630 `__init__(self, message: str='', spinner_type: str='dots', print_fn=None)` (method)
- L646 `_write(self, text: str, end: str='\n', flush: bool=False)` (method) — Write to the stdout captured at spinner creation time.
- L666 `_is_tty(self)` (method) — Check if output is a real terminal, safe against closed streams.
- L673 `_is_patch_stdout_proxy(self)` (method) — Return True when stdout is prompt_toolkit's StdoutProxy.
- L689 `_animate(self)` (method)
- L730 `start(self)` (method)
- L738 `update_text(self, new_message: str)` (method)
- L741 `print_above(self, text: str)` (method) — Print a line above the spinner without disrupting animation.
- L759 `stop(self, final_message: str=None)` (method)
- L777 `__enter__(self)` (method)
- L781 `__exit__(self, exc_type, exc_val, exc_tb)` (method)
- L793 `_trim_error(msg: str)` (function) — Shrink an error message for inline display in a tool status line.
- L811 `_detect_tool_failure(tool_name: str, result: str | None)` (function) — Inspect a tool result string for signs of failure.
- L861 `get_cute_tool_message(tool_name: str, args: dict, duration: float, result: str | None=None)` (function) — Generate a formatted tool completion line for CLI quiet mode.
