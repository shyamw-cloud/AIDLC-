from typing import Dict, Any

from ai_sdlc.models import Ticket


class JiraMCPClient:
    """Minimal Jira MCP client stub for prototype workflow."""

    def fetch_ticket(self, ticket_id: str) -> Ticket:
        payload = {
            "key": ticket_id,
            "summary": "Add AI SDLC task orchestration skeleton",
            "description": "Create a framework that reads Jira tickets through MCP, produces a spec, builds a plan, validates work, and drafts a PR summary.",
            "acceptance_criteria": [
                "The issue can be fetched via MCP.",
                "A spec is created before implementation.",
                "A task plan is generated from the spec.",
                "Validation is included before PR drafting.",
            ],
            "priority": "high",
            "labels": ["ai-sdlc", "mcp", "jira"],
        }
        return Ticket.from_dict(payload)

    def update_issue_status(self, ticket_id: str, status: str) -> Dict[str, Any]:
        return {"ticket_id": ticket_id, "status": status, "updated": True}
