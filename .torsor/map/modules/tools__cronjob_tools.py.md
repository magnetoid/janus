---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/cronjob_tools.py

Symbols in `tools/cronjob_tools.py`.

- L125 `_is_emoji_cp(cp: int)` (function)
- L129 `_zwj_has_emoji_neighbour(text: str, idx: int)` (function) — Return True when the ZWJ at text[idx] appears inside an emoji sequence.
- L144 `_strip_legitimate_emoji_zwj(prompt: str)` (function)
- L155 `_strip_cron_safe_constructs(prompt: str)` (function) — Strip the GitHub `Authorization: token $GITHUB_TOKEN` auth-header
- L173 `_check_invisible_unicode(prompt: str)` (function) — Return an error string if the prompt contains invisible-unicode
- L184 `_strip_invisible_unicode(prompt: str)` (function) — Strip invisible-unicode characters from *prompt*, preserving the ZWJ
- L213 `_scan_cron_prompt(prompt: str)` (function) — Scan the USER-SUPPLIED cron prompt for critical threats.
- L235 `_scan_cron_skill_assembled(assembled: str)` (function) — Scan an ASSEMBLED cron prompt that includes loaded skill content.
- L269 `_origin_from_env()` (function)
- L289 `_repeat_display(job: Dict[str, Any])` (function)
- L299 `_canonical_skills(skill: Optional[str]=None, skills: Optional[Any]=None)` (function)
- L317 `_resolve_model_override(model_obj: Optional[Dict[str, Any]])` (function) — Resolve a model override object into (provider, model) for job storage.
- L351 `_normalize_optional_job_value(value: Optional[Any], *, strip_trailing_slash: bool=False)` (function)
- L360 `_normalize_deliver_param(value: Any)` (function) — Normalize a user-supplied ``deliver`` value to the canonical string form.
- L381 `_validate_cron_script_path(script: Optional[str])` (function) — Validate a cron job script path at the API boundary.
- L420 `_format_job(job: Dict[str, Any])` (function)
- L459 `cronjob(action: str, job_id: Optional[str]=None, prompt: Optional[str]=None, schedule: Optional[str]=None, name: Optional[str]=None, repeat: Optional[int]=None, deliver: Optional[str]=None, include_disabled: bool=False, skill: Optional[str]=None, skills: Optional[List[str]]=None, model: Optional[str]=None, provider: Optional[str]=None, base_url: Optional[str]=None, reason: Optional[str]=None, script: Optional[str]=None, context_from: Optional[Union[str, List[str]]]=None, enabled_toolsets: Optional[List[str]]=None, workdir: Optional[str]=None, profile: Optional[str]=None, no_agent: Optional[bool]=None, task_id: str=None)` (function) — Unified cron job management tool.
- L847 `check_cronjob_requirements()` (function) — Check if cronjob tools can be used.
