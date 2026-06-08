---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/skills_guard.py

Symbols in `tools/skills_guard.py`.

- L71 `Finding` (class)
- L82 `ScanResult` (class)
- L562 `scan_file(file_path: Path, rel_path: str='')` (function) — Scan a single file for threat patterns and invisible unicode characters.
- L627 `scan_skill(skill_path: Path, source: str='community')` (function) — Scan all files in a skill directory for security threats.
- L686 `should_allow_install(result: ScanResult, force: bool=False)` (function) — Determine whether a skill should be installed based on scan result and trust.
- L730 `format_scan_report(result: ScanResult)` (function) — Format a scan result as a human-readable report string.
- L766 `content_hash(skill_path: Path)` (function) — Compute a SHA-256 hash of all files in a skill directory for integrity tracking.
- L797 `_check_structure(skill_dir: Path, ignore=None)` (function) — Check the skill directory for structural anomalies:
- L926 `_unicode_char_name(char: str)` (function) — Get a readable name for an invisible unicode character.
- L966 `_load_skill_ignore(skill_dir: Path)` (function) — Build a matcher from a skill's `.skillignore` / `.clawhubignore`.
- L1035 `_resolve_trust_level(source: str)` (function) — Map a source identifier to a trust level.
- L1064 `_determine_verdict(findings: List[Finding])` (function) — Determine the overall verdict from a list of findings.
- L1080 `_build_summary(name: str, source: str, trust: str, verdict: str, findings: List[Finding])` (function) — Build a one-line summary of the scan result.
