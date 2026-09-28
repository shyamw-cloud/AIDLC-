import pytest

from ai_sdlc.orchestrator import Orchestrator


def test_orchestrator_builds_spec_and_plan():
    orchestrator = Orchestrator()
    result = orchestrator.run("JIRA-1042")

    assert result["status"] == "ok"
    assert result["ticket"]["key"] == "JIRA-1042"
    assert "summary" in result["spec"]
    assert result["plan"][0].startswith("Fetch")
    assert result["jira_status"]["updated"] is True
