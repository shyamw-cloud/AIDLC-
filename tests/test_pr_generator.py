from ai_sdlc.pr_generator import PRGenerator


def test_pr_generator_creates_summary():
    spec = {
        "summary": "Add audit trail logging",
        "scope": ["Add event logging", "Add database schema"],
        "acceptance_criteria": ["Events are logged", "Schema migration is applied"],
        "risks": ["Database migration complexity"],
    }
    tasks = [
        {"id": "T1", "title": "Plan", "description": "Create plan"},
        {"id": "T2", "title": "Implement", "description": "Write code"},
    ]
    
    pr = PRGenerator().draft("JIRA-1042", "Add audit trail", spec, tasks)
    
    assert "JIRA-1042" in pr.title
    assert "feat/jira/1042" in pr.branch_name
    assert "Add audit trail" in pr.body
    assert "T1: Plan" in pr.body
    assert "ai-sdlc" in pr.labels
