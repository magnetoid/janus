"""Failure -> quarantined draft regression-pin eval."""
from types import SimpleNamespace

import yaml

from agent import eval_miner as em
from agent.evals import evals_dir


def _fake_llm(reply):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


_MSGS = [
    {"role": "user", "content": "What test runner does this project use?"},
    {"role": "assistant", "content": "I think it's unittest."},
]


def test_draft_eval_from_failure_parses_spec():
    reply = (
        '{"name": "knows-test-runner", "prompt": "What test runner does this '
        'project use?", "checks": [{"type": "contains", "value": "pytest"}]}'
    )
    spec = em.draft_eval_from_failure(_MSGS, lesson="Project uses pytest.", llm_caller=_fake_llm(reply))
    assert spec is not None
    assert spec.name == "knows-test-runner"
    assert spec.checks == [{"type": "contains", "value": "pytest"}]


def test_draft_rejects_unknown_check_type():
    reply = '{"name": "x", "prompt": "p", "checks": [{"type": "vibes", "value": "z"}]}'
    assert em.draft_eval_from_failure(_MSGS, llm_caller=_fake_llm(reply)) is None


def test_write_eval_draft_quarantines_yaml():
    spec = em.draft_eval_from_failure(
        _MSGS,
        llm_caller=_fake_llm('{"name": "n", "prompt": "p", "checks": [{"type": "contains", "value": "pytest"}]}'),
    )
    path = em.write_eval_draft(spec)
    assert path.parent == evals_dir() / ".drafts"
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert loaded["name"] == "n" and loaded["checks"][0]["value"] == "pytest"


def test_garbage_reply_returns_none():
    assert em.draft_eval_from_failure(_MSGS, llm_caller=_fake_llm("not json")) is None


def test_autopin_writes_draft_on_failure(monkeypatch):
    import yaml as _yaml
    from janus_constants import get_janus_home
    from agent import auto_mine, outcome_tracker

    home = get_janus_home(); home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        _yaml.safe_dump({"learning": {"track_outcomes": True, "reflexion": True},
                         "evals": {"autopin": True}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(outcome_tracker, "classify_session", lambda *a, **k: False)
    monkeypatch.setattr("agent.lessons.reflect_on_failure", lambda *a, **k: {"task_type": "t", "lesson": "Use pytest."})
    spec = em.draft_eval_from_failure(
        _MSGS, llm_caller=_fake_llm('{"name": "p", "prompt": "p", "checks": [{"type": "contains", "value": "pytest"}]}'))
    monkeypatch.setattr(em, "draft_eval_from_failure", lambda *a, **k: spec)

    msgs = [{"role": "user", "content": "q", "session_id": "s1"},
            {"role": "assistant", "content": "a"}] * 3
    auto_mine.maybe_automine(msgs, run_in_thread=False)

    drafts = list((evals_dir() / ".drafts").glob("*.yaml"))
    assert drafts, "a regression-pin draft should have been written"
