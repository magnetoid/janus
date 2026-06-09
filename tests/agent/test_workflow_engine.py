"""Tests for the declarative workflow engine (control flow, no live model)."""
import pytest

from agent import workflow_engine as wf


def _recording_runner(log):
    """A step_runner that records (name, rendered_prompt) and echoes a canned output."""
    def _run(step, context):
        log.append((step.get("name"), step["prompt"]))
        return f"out:{step.get('name')}"
    return _run


def test_sequential_steps_thread_outputs():
    log = []
    workflow = {"steps": [
        {"name": "a", "prompt": "do A", "output": "ra"},
        {"name": "b", "prompt": "use {ra}"},
    ]}
    res = wf.run_workflow(workflow, step_runner=_recording_runner(log))
    assert res["error"] is None
    assert res["ran"] == ["a", "b"]
    # step b's prompt saw step a's output via {ra}
    assert log[1] == ("b", "use out:a")
    assert res["context"]["ra"] == "out:a"
    assert res["context"]["b"] == "out:b"  # default output key = step name


def test_when_truthy_skips_step():
    log = []
    workflow = {"steps": [
        {"name": "guarded", "prompt": "x", "when": "missing"},
        {"name": "always", "prompt": "y"},
    ]}
    res = wf.run_workflow(workflow, step_runner=_recording_runner(log))
    assert res["skipped"] == ["guarded"]
    assert res["ran"] == ["always"]


def test_when_equality_and_contains():
    assert wf._eval_when("{a} == yes", {"a": "yes"}) is True
    assert wf._eval_when("{a} == yes", {"a": "no"}) is False
    assert wf._eval_when("{a} != yes", {"a": "no"}) is True
    assert wf._eval_when("{a} contains err", {"a": "an error"}) is True
    assert wf._eval_when("flag", {"flag": True}) is True
    assert wf._eval_when("flag", {"flag": ""}) is False
    assert wf._eval_when(None, {}) is True


def test_for_each_runs_per_item_and_joins():
    log = []
    workflow = {"steps": [
        {"name": "loop", "prompt": "handle {item}", "for_each": "files", "output": "results"},
    ]}
    res = wf.run_workflow(workflow, step_runner=_recording_runner(log),
                          context={"files": ["a.py", "b.py"]})
    assert [p for _, p in log] == ["handle a.py", "handle b.py"]
    assert res["context"]["results"] == "out:loop\n\nout:loop"


def test_for_each_string_is_split():
    assert wf._resolve_list("v", {"v": "a, b\nc"}) == ["a", "b", "c"]


def test_for_each_empty_skips():
    res = wf.run_workflow({"steps": [{"name": "l", "prompt": "x", "for_each": "none"}]},
                          step_runner=lambda s, c: "x")
    assert res["skipped"] == ["l"] and res["ran"] == []


def test_render_unknown_var_is_empty():
    assert wf._render("a {x} b {y}", {"x": "1"}) == "a 1 b "


def test_runner_exception_is_reported_not_raised():
    def boom(step, ctx):
        raise RuntimeError("kaboom")
    res = wf.run_workflow({"steps": [{"name": "s", "prompt": "x"}]}, step_runner=boom)
    assert res["error"] is not None and res["ran"] == []


def test_load_and_list_workflows(tmp_path, monkeypatch):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path))
    d = tmp_path / "workflows"
    d.mkdir()
    (d / "demo.yaml").write_text("name: demo\nsteps:\n  - name: s\n    prompt: hi\n", encoding="utf-8")
    assert wf.list_workflows() == ["demo"]
    loaded = wf.load_workflow("demo")
    assert loaded["name"] == "demo" and loaded["steps"][0]["name"] == "s"
    with pytest.raises(FileNotFoundError):
        wf.load_workflow("nope")
