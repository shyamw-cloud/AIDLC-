from typing import Dict, Any

from ai_sdlc.jira_mcp import JiraMCPClient
from ai_sdlc.planner import Planner, SpecBuilder


class Orchestrator:
    def __init__(self, jira_client=None):
        self.jira_client = jira_client or JiraMCPClient()
        self.spec_builder = SpecBuilder()
        self.planner = Planner()

    def run(self, ticket_id: str) -> Dict[str, Any]:
        ticket = self.jira_client.fetch_ticket(ticket_id)
        spec = self.spec_builder.build(ticket)
        plan = self.planner.plan(spec)

        status_update = self.jira_client.update_issue_status(ticket_id, "In Progress")

        return {
            "ticket": {
                "key": ticket.key,
                "summary": ticket.summary,
                "priority": ticket.priority,
            },
            "spec": spec,
            "plan": plan,
            "jira_status": status_update,
            "status": "ok",
        }
