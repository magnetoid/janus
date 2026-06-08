---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/logs.py

Symbols in `hermes_cli/logs.py`.

- L60 `_parse_since(since_str: str)` (function) — Parse a relative time string like '1h', '30m', '2d' into a datetime cutoff.
- L80 `_parse_line_timestamp(line: str)` (function) — Extract timestamp from a log line. Returns None if not parseable.
- L91 `_extract_level(line: str)` (function) — Extract the log level from a line.
- L97 `_extract_logger_name(line: str)` (function) — Extract the logger name from a log line.
- L103 `_line_matches_component(line: str, prefixes: Sequence[str])` (function) — Check if a log line's logger name starts with any of *prefixes*.
- L111 `_matches_filters(line: str, *, min_level: Optional[str]=None, session_filter: Optional[str]=None, since: Optional[datetime]=None, component_prefixes: Optional[Sequence[str]]=None)` (function) — Check if a log line passes all active filters.
- L142 `tail_log(log_name: str='agent', *, num_lines: int=50, follow: bool=False, level: Optional[str]=None, session: Optional[str]=None, since: Optional[str]=None, component: Optional[str]=None)` (function) — Read and display log lines, optionally following in real time.
- L253 `_read_tail(path: Path, num_lines: int, *, has_filters: bool=False, min_level: Optional[str]=None, session_filter: Optional[str]=None, since: Optional[datetime]=None, component_prefixes: Optional[Sequence[str]]=None)` (function) — Read the last *num_lines* matching lines from a log file.
- L282 `_read_last_n_lines(path: Path, n: int)` (function) — Efficiently read the last N lines from a file.
- L338 `_follow_log(path: Path, *, min_level: Optional[str]=None, session_filter: Optional[str]=None, since: Optional[datetime]=None, component_prefixes: Optional[Sequence[str]]=None)` (function) — Poll a log file for new content and print matching lines.
- L362 `list_logs()` (function) — Print available log files with sizes.
