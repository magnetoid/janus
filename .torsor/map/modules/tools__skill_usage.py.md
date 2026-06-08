---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/skill_usage.py

Symbols in `tools/skill_usage.py`.

- L59 `_skills_dir()` (function)
- L63 `_usage_file()` (function)
- L68 `_usage_file_lock()` (function) — Serialize .usage.json read-modify-write cycles across processes.
- L103 `_archive_dir()` (function)
- L107 `_now_iso()` (function)
- L111 `_parse_iso_timestamp(value: Any)` (function) — Parse an ISO timestamp defensively for activity comparisons.
- L124 `latest_activity_at(record: Dict[str, Any])` (function) — Return the newest actual activity timestamp for a usage record.
- L144 `activity_count(record: Dict[str, Any])` (function) — Return the total observed activity count across use/view/patch events.
- L159 `_read_bundled_manifest_names()` (function) — Return the set of skill names that were seeded from the bundled repo.
- L182 `_read_hub_installed_names()` (function) — Return the set of skill names installed via the Skills Hub.
- L220 `_prune_builtins_enabled()` (function) — Whether bundled built-in skills are eligible for curator pruning.
- L241 `_suppressed_file()` (function)
- L245 `read_suppressed_names()` (function) — Built-in skills the curator pruned — the re-seeder must leave archived.
- L266 `_write_suppressed_names(names: Set[str])` (function)
- L288 `add_suppressed_name(skill_name: str)` (function) — Record that a built-in skill was pruned, so sync won't restore it.
- L298 `remove_suppressed_name(skill_name: str)` (function) — Clear a built-in's suppression entry (e.g. on restore).
- L308 `list_agent_created_skill_names()` (function) — Enumerate skills the curator may manage.
- L355 `list_archived_skill_names()` (function) — Enumerate skills in ``~/.hermes/skills/.archive/``.
- L368 `_read_skill_name(skill_md: Path, fallback: str)` (function) — Parse the `name:` field from a SKILL.md YAML frontmatter.
- L389 `is_agent_created(skill_name: str)` (function) — Whether *skill_name* is neither bundled nor hub-installed.
- L395 `is_hub_installed(skill_name: str)` (function) — Whether *skill_name* was installed via the Skills Hub.
- L400 `is_bundled(skill_name: str)` (function) — Whether *skill_name* was seeded from the bundled repo skills.
- L405 `is_curation_eligible(skill_name: str)` (function) — Whether the curator may track/archive *skill_name*.
- L419 `_is_curator_managed_record(record: Any)` (function) — Return True when a usage record opts a skill into curator management.
- L430 `_empty_record()` (function)
- L446 `load_usage()` (function) — Read the entire .usage.json map. Returns empty dict on missing/corrupt.
- L466 `save_usage(data: Dict[str, Dict[str, Any]])` (function) — Write the usage map atomically. Best-effort — errors are logged, not raised.
- L490 `get_record(skill_name: str)` (function) — Return the record for *skill_name*, creating a fresh one if missing.
- L503 `seed_record_if_missing(skill_name: str)` (function) — Persist a baseline usage record for a curation-eligible skill.
- L525 `_mutate(skill_name: str, mutator, *, require_curation_eligible: bool=False)` (function) — Load, apply *mutator(record)* in place, save. Best-effort.
- L557 `bump_view(skill_name: str)` (function) — Bump view_count and last_viewed_at. Called from skill_view().
- L569 `bump_use(skill_name: str)` (function) — Bump use_count and last_used_at. Called when a skill is actively used
- L581 `bump_patch(skill_name: str)` (function) — Bump patch_count and last_patched_at. Called from skill_manage (patch/edit).
- L592 `mark_agent_created(skill_name: str)` (function) — Opt a skill created by skill_manage into curator management.
- L603 `set_state(skill_name: str, state: str)` (function) — Set lifecycle state. No-op if *state* is invalid or the skill isn't
- L618 `set_pinned(skill_name: str, pinned: bool)` (function)
- L624 `forget(skill_name: str)` (function) — Drop a skill's usage entry entirely. Called when the skill is deleted.
- L642 `archive_skill(skill_name: str)` (function) — Move a curator-eligible skill directory to ~/.hermes/skills/.archive/.
- L692 `restore_skill(skill_name: str)` (function) — Move an archived skill back to ~/.hermes/skills/. Restores to the flat
- L754 `_find_skill_dir(skill_name: str)` (function) — Locate the directory for a skill by its frontmatter `name:` field.
- L775 `agent_created_report()` (function) — Return a list of {name, state, pinned, last_activity_at, ...}
- L801 `provenance(skill_name: str)` (function) — Classify a skill's origin: 'hub', 'bundled', or 'agent'.
- L814 `usage_report()` (function) — Return usage telemetry for EVERY skill on disk, with provenance.
