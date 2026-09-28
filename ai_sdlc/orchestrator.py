from typing import Dict, Any

from ai_sdlc.jira_mcp import JiraMCPClient
from ai_sdlc.planner import Planner, SpecBuilder
from ai_sdlc.tasks import TaskEngine
from ai_sdlc.pr_generator import PRGenerator
from ai_sdlc.github_client import GitHubClient


class Orchestrator:
    def __init__(self, jira_client=None, github_client=None):
        self.jira_client = jira_client or JiraMCPClient()
        self.github_client = github_client or GitHubClient()
        self.spec_builder = SpecBuilder()
        self.planner = Planner()
        self.task_engine = TaskEngine()
        self.pr_generator = PRGenerator()

    def run(self, ticket_id: str, owner: str = "shyamw-cloud", repo: str = "AIDLC-") -> Dict[str, Any]:
        # Phase 1: Ticket intake
        ticket = self.jira_client.fetch_ticket(ticket_id)
        
        # Phase 2: Spec creation
        spec = self.spec_builder.build(ticket)
        
        # Phase 3: Planning
        plan = self.planner.plan(spec)
        
        # Phase 4: Task generation
        tasks = self.task_engine.generate(spec)
        tasks_dict = [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "dependencies": task.dependencies,
                "validation": task.validation,
                "effort": task.effort,
            }
            for task in tasks
        ]
        
        # Phase 5: PR generation
        pr_draft = self.pr_generator.draft(
            ticket_id,
            ticket.summary,
            spec,
            tasks_dict,
        )
        
        # Phase 6: GitHub operations (branch and PR creation)
        branch_result = self.github_client.create_branch(owner, repo, pr_draft.branch_name)
        pr_result = self.github_client.create_pull_request(
            owner,
            repo,
            pr_draft.title,
            pr_draft.body,
            head=pr_draft.branch_name,
            labels=pr_draft.labels,
        )
        
        # Phase 7: Jira status update
        status_update = self.jira_client.update_issue_status(ticket_id, "In Review")
        jira_link = self.jira_client.add_pr_link(ticket_id, pr_result["url"])
        
        return {
            "ticket": {
                "key": ticket.key,
                "summary": ticket.summary,
                "priority": ticket.priority,
            },
            "spec": spec,
            "plan": plan,
            "tasks": tasks_dict,
            "pr": {
                "title": pr_draft.title,
                "branch": pr_draft.branch_name,
                "url": pr_result.get("url"),
                "number": pr_result.get("pr_number"),
            },
            "github_status": {
                "branch_created": branch_result["status"],
                "pr_created": pr_result["status"],
            },
            "jira_status": {
                "status_updated": status_update["status"],
                "pr_linked": jira_link["status"],
            },
            "status": "ok",
        }
