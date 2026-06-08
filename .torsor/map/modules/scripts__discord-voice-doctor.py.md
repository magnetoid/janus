---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/discord-voice-doctor.py

Symbols in `scripts/discord-voice-doctor.py`.

- L33 `mask(value)` (function) — Mask sensitive value: show only first 4 chars.
- L40 `check(label, ok, detail='')` (function)
- L49 `warn(label, detail='')` (function)
- L56 `section(title)` (function)
- L60 `check_packages()` (function) — Check Python package dependencies. Returns True if all critical deps OK.
- L121 `check_system_tools()` (function) — Check system-level tools (opus, ffmpeg). Returns True if all OK.
- L173 `check_env_vars()` (function) — Check environment variables. Returns (ok, token, groq_key, eleven_key).
- L237 `check_config(groq_key, eleven_key)` (function) — Check hermes config.yaml.
- L281 `check_bot_permissions(token)` (function) — Check bot permissions via Discord API. Returns True if all OK.
- L370 `main()` (function)
