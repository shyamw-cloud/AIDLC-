from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class GitHubBranchCreateRequest:
    branch_name: str
    base_branch: str = "main"


@dataclass
class GitHubPRCreateRequest:
    title: str
    body: str
    head_branch: str
    base_branch: str = "main"
    labels: list = None


class GitHubClient:
    """Minimal stub for GitHub branch and PR operations via MCP."""

    def create_branch(self, owner: str, repo: str, branch_name: str, base_branch: str = "main") -> Dict[str, Any]:
        """Create a feature branch from the base branch."""
        return {
            "status": "created",
            "owner": owner,
            "repo": repo,
            "branch": branch_name,
            "base": base_branch,
        }

    def create_pull_request(self, owner: str, repo: str, title: str, body: str, head: str, base: str = "main", labels: list = None) -> Dict[str, Any]:
        """Create a pull request."""
        labels = labels or []
        return {
            "status": "created",
            "owner": owner,
            "repo": repo,
            "pr_number": 42,  # mock PR number
            "title": title,
            "head": head,
            "base": base,
            "labels": labels,
            "url": f"https://github.com/{owner}/{repo}/pull/42",
        }

    def add_issue_link(self, owner: str, repo: str, pr_number: int, issue_key: str) -> Dict[str, Any]:
        """Link a Jira issue to the PR in the body or comment."""
        return {
            "status": "linked",
            "pr_number": pr_number,
            "issue_key": issue_key,
        }
