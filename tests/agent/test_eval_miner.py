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
