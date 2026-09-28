from ai_sdlc.tasks import Task, TaskEngine


def test_task_engine_generates_work_items():
    spec = {
        "scope": ["Fetch ticket", "Create spec", "Run validation"],
        "acceptance_criteria": [
            "Issue is normalized",
            "Spec includes scope",
            "Validation is included",
        ],
    }

    tasks = TaskEngine().generate(spec)

    assert len(tasks) >= 5
    assert tasks[0].id == "T1"
    assert tasks[0].validation[0] == "Ticket key exists"
    assert tasks[3].title == "Implement feature work"
    assert "Validation" in tasks[4].description or tasks[4].validation[0].startswith("All acceptance")
