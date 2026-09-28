from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Task:
    id: str
    title: str
    description: str
    dependencies: List[str] = field(default_factory=list)
    validation: List[str] = field(default_factory=list)
    effort: str = "medium"


class TaskEngine:
    """Converts a ticket specification into executable implementation tasks."""

    def generate(self, spec: Dict[str, Any]) -> List[Task]:
        scope = spec.get("scope", [])
        acceptance = spec.get("acceptance_criteria", [])

        tasks = [
            Task(
                id="T1",
                title="Normalize ticket and scope",
                description="Map Jira issue fields into the internal task model and validate required fields.",
                dependencies=[],
                validation=["Ticket key exists", "Summary is non-empty"],
                effort="small",
            ),
            Task(
                id="T2",
                title="Prepare specification contract",
                description="Write the structured spec covering objective, scope, risks, and acceptance criteria.",
                dependencies=["T1"],
                validation=["Spec contains scope", "Spec contains acceptance criteria"],
                effort="medium",
            ),
            Task(
                id="T3",
                title="Create implementation plan",
                description="Turn the spec into ordered implementation tasks and validation gates.",
                dependencies=["T2"],
                validation=["Plan references scope items", "Plan includes validation steps"],
                effort="medium",
            ),
            Task(
                id="T4",
                title="Implement feature work",
                description="Implement the changes required to satisfy the defined scope and acceptance criteria.",
                dependencies=["T3"],
                validation=["Code changes satisfy spec", "Feature is covered by tests"],
                effort="large",
            ),
            Task(
                id="T5",
                title="Validate and review",
                description="Run tests, lint, and build checks, then review issues before creating the PR.",
                dependencies=["T4"],
                validation=["Validation passes", "Reviewer checklist is complete"],
                effort="medium",
            ),
        ]

        if scope:
            tasks[3].description = (
                "Implement the changes required to satisfy the defined scope: "
                + ", ".join(scope)
            )

        if acceptance:
            tasks[4].validation = [
                "All acceptance criteria are covered",
                *[f"Validate: {item}" for item in acceptance],
            ]

        return tasks
