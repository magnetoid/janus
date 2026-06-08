---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_unavailable_skill_hint.py

Symbols in `tests/gateway/test_unavailable_skill_hint.py`.

- L29 `tmp_skills(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Isolated skills dir + HERMES_HOME so the real user config is untouched.
- L39 `_write_skill(skills_dir: Path, rel: str, frontmatter_name: str)` (function) — Create a SKILL.md at ``<skills_dir>/<rel>/SKILL.md``.
- L51 `test_frontmatter_slug_matched_even_when_dir_name_differs(tmp_skills: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Directory ``stable-diffusion`` + frontmatter ``Stable Diffusion Image Generation``.
- L87 `test_unknown_command_still_returns_none(tmp_skills: Path)` (function) — A command that matches no on-disk skill still returns None.
- L103 `test_matched_but_not_disabled_returns_none(tmp_skills: Path)` (function) — A skill that exists and isn't disabled shouldn't produce a hint.
- L119 `test_slug_normalization_strips_non_alnum(tmp_skills: Path)` (function) — Frontmatter ``C++ Code Review`` → slug ``c-code-review`` (``+`` stripped).
- L139 `test_optional_skill_uses_frontmatter_slug(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Same drift bug applies to the optional-skills branch.
