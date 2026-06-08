---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/secret_prompt.py

Symbols in `hermes_cli/secret_prompt.py`.

- L16 `_collect_masked_input(read_char: Callable[[], str], write: Callable[[str], object], prompt: str, *, mask: str='*')` (function) — Read one secret line while writing a mask character per typed char.
- L56 `masked_secret_prompt(prompt: str, *, mask: str='*')` (function) — Prompt for a secret while showing masked typing feedback.
- L84 `_stream_is_tty(stream)` (function)
- L91 `_masked_secret_prompt_windows(prompt: str, *, mask: str)` (function)
- L108 `_masked_secret_prompt_posix(prompt: str, *, mask: str)` (function)
