"""Regression pin: draft skills must NOT be walked as active skills.

`skills/.drafts/` is the mining quarantine. Before the exclusion fix, the
scanner walked it, so every mined draft was silently live in the skill library
— defeating the "review before activation" guarantee and the whole
graduated-promotion design.
"""

from __future__ import annotations

import agent.skill_utils as su


def _write(p, name):
    p.mkdir(parents=True, exist_ok=True)
    (p / "SKILL.md").write_text(f"---\nname: {name}\n---\nbody\n", encoding="utf-8")


def test_drafts_dir_is_excluded_constant():
    assert ".drafts" in su.EXCLUDED_SKILL_DIRS


def test_draft_skill_not_in_index(tmp_path):
    root = tmp_path / "skills"
    _write(root / "cat" / "good", "good")
    _write(root / ".drafts" / "draftee", "draftee")

    found = [str(p) for p in su.iter_skill_index_files(root, "SKILL.md")]
    assert any("good" in f for f in found)            # active skill is indexed
    assert not any(".drafts" in f for f in found)     # draft is not
