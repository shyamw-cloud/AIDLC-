from typing import Dict, List, Any


class SpecBuilder:
    def build(self, ticket: Any) -> Dict[str, Any]:
        return {
            "summary": ticket.summary,
            "goal": ticket.description,
            "scope": [
                "Fetch Jira issue using MCP",
                "Create spec from ticket",
                "Generate implementation plan",
                "Validate outputs",
                "Draft PR summary",
            ],
            "acceptance_criteria": ticket.acceptance_criteria,
            "risks": [
                "Missing Jira MCP connectivity",
                "Ambiguous acceptance criteria",
                "Missing validation pipeline",
            ],
            "non_goals": [
                "Full production security hardening",
                "Complex multi-repository orchestration",
            ],
        }


class Planner:
    def plan(self, spec: Dict[str, Any]) -> List[str]:
        return [
            "Fetch issue details from Jira via MCP",
            "Normalize ticket into structured model",
            "Build spec from requirements and acceptance criteria",
            "Generate ordered task plan",
            "Implement required changes",
            "Run validation checks",
            "Draft PR summary and update Jira status",
        ]
