"""Tests for session-end procedure (skill) mining."""
import json
from types import SimpleNamespace

import pytest

from agent import skill_miner
from agent.skill_miner import (
    _parse_proposals,
    _slug,
    mine_session_skills,
    render_skill_md,
    write_skill_draft,
)


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=reply))]
        )
    return _caller


TRANSCRIPT = [
    {"role": "user", "content": "Deploy to staging."},
    {"role": "assistant", "content": "Ran tests, built, pushed, smoke-checked — staging is live."},
]

ONE_SKILL = json.dumps([{
    "name": "Deploy Staging",
    "description": "Run tests, build, push, and smoke-check staging.",
    "category": "devops",
    "when_to_use": "When shipping to the staging environment.",
    "steps": ["Run the test suite", "Build the artifact", "Push to staging", "Smoke-check"],
    "script_filename": "deploy.py",
    "script_content": "print('deploying')\n",
}])


def test_slug():
    assert _slug("Deploy Staging") == "deploy-staging"
    assert _slug("  weird__Name!! ") == "weird-name"
    assert _slug("") == "skill"


def test_parse_skips_incomplete_items():
    raw = json.dumps([
        {"name": "ok", "description": "Fine.", "steps": ["a"]},
        {"name": "no-steps", "description": "x"},          # missing steps
        {"name": "", "description": "y", "steps": ["a"]},   # missing name
        "garbage",
    ])
    out = _parse_proposals(raw)
    assert [p["name"] for p in out] == ["ok"]


def test_parse_tolerates_code_fence_and_caps_description():
    long_desc = "x" * 80
    raw = f"```json\n[{{\"name\":\"a\",\"description\":\"{long_desc}\",\"steps\":[\"s\"]}}]\n```"
    out = _parse_proposals(raw)
    assert len(out) == 1 and len(out[0]["description"]) == 60


def test_render_skill_md_has_frontmatter_and_sections():
    p = _parse_proposals(ONE_SKILL)[0]
    md = render_skill_md(p)
    assert md.startswith("---")
    assert "name: deploy-staging" in md
    assert "created_by: agent-draft" in md
    assert "## When to Use" in md and "## Procedure" in md
    assert "1. Run the test suite" in md


def test_mine_writes_draft_with_script(tmp_path):
    res = mine_session_skills(
        TRANSCRIPT, llm_caller=_fake_llm(ONE_SKILL),
        existing_skill_names=[], drafts_dir=tmp_path,
    )
    assert res["error"] is None
    assert len(res["proposals"]) == 1
    skill_dir = tmp_path / "deploy-staging"
    assert (skill_dir / "SKILL.md").is_file()
    assert (skill_dir / "scripts" / "deploy.py").read_text(encoding="utf-8") == "print('deploying')\n"


def test_mine_dedupes_against_existing(tmp_path):
    res = mine_session_skills(
        TRANSCRIPT, llm_caller=_fake_llm(ONE_SKILL),
        existing_skill_names=["deploy-staging"], drafts_dir=tmp_path,
    )
    assert res["proposals"] == []
    assert not (tmp_path / "deploy-staging").exists()


def test_repeated_mine_does_not_overwrite(tmp_path):
    p = _parse_proposals(ONE_SKILL)[0]
    a = write_skill_draft(p, drafts_dir=tmp_path)
    b = write_skill_draft(p, drafts_dir=tmp_path)
    assert a.name == "deploy-staging" and b.name == "deploy-staging-2"


def test_mine_best_effort_on_llm_failure(tmp_path):
    def boom(**kwargs):
        raise RuntimeError("model down")
    res = mine_session_skills(TRANSCRIPT, llm_caller=boom, drafts_dir=tmp_path)
    assert res["error"] is not None and res["proposals"] == []


def test_empty_transcript_noop(tmp_path):
    res = mine_session_skills([], llm_caller=_fake_llm(ONE_SKILL), drafts_dir=tmp_path)
    assert res["proposals"] == [] and res["written"] == []
