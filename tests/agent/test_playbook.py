"""Tests for the ACE-style learning-loop playbook (agent/playbook.py)."""
from types import SimpleNamespace

from agent import playbook as pb


def _llm(reply):
    def _c(**kw):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _c


def test_scopes_constant():
    assert "memory" in pb.SCOPES and "general" in pb.SCOPES


def test_add_and_for_scope():
    pb.add_entry("memory", "Prefer durable facts over transient details.")
    pb.add_entry("general", "Be concise.")
    pb.add_entry("skills", "Only mine multi-step procedures.")
    block = pb.for_scope("memory")
    assert "durable facts" in block          # scope match
    assert "Be concise" in block             # general is always included
    assert "multi-step procedures" not in block  # other scope excluded


def test_for_scope_empty_when_none():
    assert pb.for_scope("memory") == ""


def test_dedup_case_insensitive():
    pb.add_entry("memory", "Prefer durable facts.")
    assert pb.add_entry("memory", "prefer durable facts.") is None
    assert len(pb.load()) == 1


def test_prune_keeps_highest_score():
    for i in range(5):
        pb.add_entry("general", f"guidance {i}", score=i / 10)
    evicted = pb.prune(max_entries=3)
    kept = [e["guidance"] for e in pb.load()]
    assert len(kept) == 3 and len(evicted) == 2
    assert "guidance 4" in kept and "guidance 0" not in kept


def test_propose_parses_scoped_guidance():
    reply = ('[{"scope":"memory","guidance":"Capture tool quirks."},'
             '{"scope":"lessons","guidance":"Name the fix, not just the bug."}]')
    out = pb.propose("recent activity text", llm_caller=_llm(reply))
    assert {"scope": "memory", "guidance": "Capture tool quirks."} in out


def test_curate_admits_only_vetted(monkeypatch):
    monkeypatch.setattr("agent.deliberation.red_team_claims",
        lambda claims, **kw: {"error": None, "verdicts": {
            claims[0]["id"]: {"verdict": "accept"},
            claims[1]["id"]: {"verdict": "reject", "skeptic_objection": "too vague"},
        }})
    res = pb.curate([{"scope": "memory", "guidance": "Capture tool quirks."},
                     {"scope": "general", "guidance": "be good"}], llm_caller=_llm("{}"))
    guides = [e["guidance"] for e in pb.load()]
    assert "Capture tool quirks." in guides and "be good" not in guides
    assert res["added"] == 1 and len(res["rejected"]) == 1


def test_curate_revise_uses_revised_text(monkeypatch):
    monkeypatch.setattr("agent.deliberation.red_team_claims",
        lambda claims, **kw: {"error": None, "verdicts": {
            claims[0]["id"]: {"verdict": "revise",
                              "revised_content": "Capture tool quirks AND versions."}}})
    pb.curate([{"scope": "memory", "guidance": "Capture tool quirks."}], llm_caller=_llm("{}"))
    assert any("AND versions" in e["guidance"] for e in pb.load())


def test_curate_fails_closed_when_reflector_errors(monkeypatch):
    monkeypatch.setattr("agent.deliberation.red_team_claims",
        lambda claims, **kw: {"error": "provider down", "verdicts": {}})
    res = pb.curate([{"scope": "memory", "guidance": "x"}], llm_caller=_llm("{}"))
    assert pb.load() == []          # nothing admitted without a passing verdict
    assert res["added"] == 0 and res["error"]


def test_best_effort_never_raises():
    assert isinstance(pb.for_scope("memory"), str)
    assert isinstance(pb.curate([], llm_caller=None), dict)
    assert pb.enabled({}) is False


def test_augment_system_noop_when_disabled():
    pb.add_entry("memory", "Some guidance.")
    assert pb.augment_system("BASE", "memory") == "BASE"  # disabled in tests → no-op


def test_augment_system_prepends_when_enabled(monkeypatch):
    monkeypatch.setattr(pb, "enabled", lambda config=None: True)
    pb.add_entry("memory", "Capture tool quirks.")
    out = pb.augment_system("BASE", "memory")
    assert out.startswith("BASE") and "Capture tool quirks." in out


def test_run_curation_proposes_then_admits(monkeypatch):
    monkeypatch.setattr("agent.playbook.propose",
                        lambda ctx, **kw: [{"scope": "memory", "guidance": "From activity guidance."}])
    monkeypatch.setattr("agent.deliberation.red_team_claims",
        lambda claims, **kw: {"error": None, "verdicts": {claims[0]["id"]: {"verdict": "accept"}}})
    res = pb.run_curation("some recent activity", llm_caller=_llm("{}"))
    assert res["added"] == 1
    assert any("From activity guidance." in e["guidance"] for e in pb.load())


def test_memory_miner_injects_playbook_guidance(monkeypatch):
    monkeypatch.setattr("agent.playbook.enabled", lambda config=None: True)
    pb.add_entry("memory", "PLAYBOOK_MARKER_GUIDANCE")
    seen = {}

    def fake_llm(**kw):
        seen["system"] = kw["messages"][0]["content"]
        return SimpleNamespace(choices=[SimpleNamespace(
            message=SimpleNamespace(content='{"user": [], "memory": []}'))])

    from agent import memory_miner as mm
    from tools.memory_tool import MemoryStore
    store = MemoryStore(); store.load_from_disk()
    msgs = [{"role": "user", "content": "hi, this is a test conversation about deploys"},
            {"role": "assistant", "content": "ok, noted the deploy detail"}]
    mm.mine_session_memory(msgs, store, llm_caller=fake_llm)
    assert "PLAYBOOK_MARKER_GUIDANCE" in seen["system"]


def test_sleep_cycle_curates_playbook_when_enabled(monkeypatch):
    monkeypatch.setattr("agent.playbook.enabled", lambda config=None: True)
    called = {}
    monkeypatch.setattr("agent.playbook.run_curation",
                        lambda ctx, **kw: (called.setdefault("ctx", ctx), {"added": 1})[1])
    from agent import sleep as sl
    from tools.memory_tool import MemoryStore
    store = MemoryStore(); store.load_from_disk()
    report = sl.run_sleep_cycle(store, llm_caller=_llm('{"user": [], "memory": []}'),
                                session_summaries=["session A did X", "session B did Y"])
    assert "ctx" in called and report.get("playbook") == {"added": 1}
