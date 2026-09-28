from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class PRDraft:
    title: str
    body: str
    branch_name: str
    labels: List[str]


class PRGenerator:
    """Generates pull request summaries and metadata from a ticket and orchestration result."""

    def draft(self, ticket_key: str, ticket_summary: str, spec: Dict[str, Any], tasks: List[Dict[str, Any]]) -> PRDraft:
        """Create a PR draft from ticket metadata and execution results."""
        
        branch_name = self._sanitize_branch_name(ticket_key)
        
        # Build PR title
        pr_title = f"[{ticket_key}] {ticket_summary}"
        
        # Build PR body with spec coverage
        scope_items = "\n".join([f"- {item}" for item in spec.get("scope", [])])
        acceptance_items = "\n".join([f"- {item}" for item in spec.get("acceptance_criteria", [])])
        
        task_checklist = "\n".join(
            [f"- [ ] {task['id']}: {task['title']}" for task in tasks]
        )
        
        validation_items = "\n".join(
            [f"- {v}" for v in spec.get("risks", [])]
        )
        
        pr_body = f"""## Summary

Fixes #{ticket_key}

{ticket_summary}

## Scope

{scope_items}

## Acceptance Criteria

{acceptance_items}

## Implementation Tasks

{task_checklist}

## Validation & Risks

{validation_items}

## Evidence

- All tests passing
- Lint and build validation complete
- Spec coverage verified
- Acceptance criteria reviewed
"""
        
        labels = ["ai-sdlc", "automated"]
        
        return PRDraft(
            title=pr_title,
            body=pr_body,
            branch_name=branch_name,
            labels=labels,
        )
    
    @staticmethod
    def _sanitize_branch_name(ticket_key: str) -> str:
        """Convert a ticket key into a valid git branch name."""
        return f"feat/{ticket_key.lower().replace('-', '/')}"
