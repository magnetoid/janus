---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/security_advisories.py

Symbols in `hermes_cli/security_advisories.py`.

- L67 `Advisory` (class) — One security advisory entry.
- L138 `AdvisoryHit` (class) — One package-version match against an advisory.
- L146 `_installed_version(pkg_name: str)` (function) — Return the installed version of ``pkg_name``, or None if not installed.
- L167 `detect_compromised(advisories: Iterable[Advisory]=ADVISORIES)` (function) — Scan installed packages and return all advisory hits.
- L202 `get_acked_ids()` (function) — Return the set of advisory IDs the user has dismissed.
- L222 `ack_advisory(advisory_id: str)` (function) — Persist an ack for ``advisory_id``. Returns True on success.
- L251 `filter_unacked(hits: list[AdvisoryHit])` (function) — Return only hits whose advisories the user has not dismissed.
- L264 `_term_supports_color()` (function)
- L272 `short_banner_lines(hits: list[AdvisoryHit])` (function) — Return 1-3 short lines suitable for a startup banner.
- L292 `full_remediation_text(hit: AdvisoryHit)` (function) — Return a multi-line block describing the advisory + remediation.
- L327 `_banner_cache_path()` (function)
- L337 `_read_banner_cache()` (function)
- L360 `_write_banner_cache(seen: dict[str, float])` (function)
- L371 `hits_due_for_banner(hits: list[AdvisoryHit], *, repeat_hours: int=_BANNER_REPEAT_HOURS)` (function) — Return only hits whose banner is due (not acked, not recently shown).
- L406 `render_doctor_section(hits: list[AdvisoryHit])` (function) — Render the security-advisory section for ``hermes doctor``.
- L424 `startup_banner(hits: list[AdvisoryHit])` (function) — Return a printable startup banner, or None if nothing is due.
- L441 `gateway_log_message(hits: list[AdvisoryHit])` (function) — Return a one-line log message for gateway operators, or None.
