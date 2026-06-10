"""Tests for the dashboard self-learning API endpoints."""
import pytest


def _client():
    from starlette.testclient import TestClient
    from janus_cli.web_server import app, _SESSION_HEADER_NAME, _SESSION_TOKEN

    client = TestClient(app)
    client.headers[_SESSION_HEADER_NAME] = _SESSION_TOKEN
    return client


class TestLearningEndpoints:
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.client = _client()

    def test_learning_stats_empty_then_populated(self):
        r = self.client.get("/api/learning/stats")
        assert r.status_code == 200
        assert r.json()["overall"]["sessions"] == 0

        from agent import outcome_tracker as ot
        ot.record_outcome("s1", True, skills=["deploy"])
        ot.record_outcome("s2", False, skills=["deploy"])
        body = self.client.get("/api/learning/stats").json()
        assert body["overall"]["sessions"] == 2
        assert body["skills"][0]["name"] == "deploy" and body["skills"][0]["uses"] == 2

    def test_aspirations_crud(self):
        assert self.client.get("/api/aspirations").json()["aspirations"] == []
        rec = self.client.post("/api/aspirations", json={"goal": "Ship Janus 1.0"}).json()["aspiration"]
        assert rec["id"] == "ship-janus-1-0"
        assert len(self.client.get("/api/aspirations").json()["aspirations"]) == 1
        assert self.client.delete(f"/api/aspirations/{rec['id']}").json()["ok"] is True
        assert self.client.get("/api/aspirations").json()["aspirations"] == []

    def test_aspiration_requires_goal(self):
        assert self.client.post("/api/aspirations", json={"goal": "  "}).status_code == 400

    def test_interests_crud(self):
        rec = self.client.post("/api/interests", json={"field": "graphic design"}).json()["interest"]
        assert rec["id"] == "graphic-design"
        assert any(i["id"] == "graphic-design" for i in self.client.get("/api/interests").json()["interests"])
        assert self.client.delete(f"/api/interests/{rec['id']}").json()["ok"] is True

    def test_skill_graph_endpoint(self):
        r = self.client.get("/api/skills/graph")
        assert r.status_code == 200
        body = r.json()
        assert "nodes" in body and "edges" in body

    def test_sleep_status_and_pause(self):
        assert self.client.get("/api/sleep").json()["paused"] is False
        assert self.client.put("/api/sleep/paused", json={"paused": True}).json()["paused"] is True
        assert self.client.get("/api/sleep").json()["paused"] is True
