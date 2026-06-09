"""Tests for the skill verification gate (agent/skill_verifier.py)."""
import pytest

from agent.skill_verifier import verify_skill_dir


GOOD_MD = "---\nname: deploy\ndescription: Deploy to staging safely.\n---\n# Deploy\n"


def _make_skill(d, md=GOOD_MD, script=None):
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(md, encoding="utf-8")
    if script is not None:
        (d / "scripts").mkdir(exist_ok=True)
        (d / "scripts" / "run.py").write_text(script, encoding="utf-8")
    return d


def test_good_skill_passes(tmp_path):
    d = _make_skill(tmp_path / "s", script="print('ok')\n")
    assert verify_skill_dir(d) == {"ok": True, "issues": []}


def test_missing_skill_md(tmp_path):
    (tmp_path / "s").mkdir()
    r = verify_skill_dir(tmp_path / "s")
    assert r["ok"] is False and "missing SKILL.md" in r["issues"]


def test_missing_name_and_description(tmp_path):
    d = _make_skill(tmp_path / "s", md="---\n---\n# x\n")
    r = verify_skill_dir(d)
    assert r["ok"] is False
    assert any("name" in i for i in r["issues"]) and any("description" in i for i in r["issues"])


def test_description_too_long(tmp_path):
    long = "x" * 80
    d = _make_skill(tmp_path / "s", md=f"---\nname: a\ndescription: {long}\n---\n")
    r = verify_skill_dir(d)
    assert r["ok"] is False and any("too long" in i for i in r["issues"])


def test_broken_script_flagged(tmp_path):
    d = _make_skill(tmp_path / "s", script="def f(:\n  pass\n")  # syntax error
    r = verify_skill_dir(d)
    assert r["ok"] is False and any("syntax error" in i for i in r["issues"])
