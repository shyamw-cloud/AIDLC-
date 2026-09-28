# Jira MCP integration design

## Objective

Use Model Context Protocol (MCP) to connect GitHub Copilot or an orchestrator to Jira without hardcoding ticket retrieval logic into the application.

## Tools

A typical Jira MCP integration exposes tools such as:

- `get_issue(issue_id)`
- `search_issues(jql)`
- `create_comment(issue_id, body)`
- `update_issue_status(issue_id, status)`
- `list_projects()`
- `get_transitions(issue_id)`

## Typical flow

1. The orchestrator requests a Jira issue by ID.
2. MCP returns issue metadata in a structured JSON schema.
3. The ticket is normalized into an internal model.
4. The spec and planning layers consume that model.
5. Jira gets updated as progress changes.

## Data mapping

```text
Jira issue fields:
- key
- summary
- description
- acceptance criteria
- status
- priority
- labels
- project
```

## Implementation notes

In real production deployment, the MCP client should:
- authenticate via secure token management
- retry transient failures
- validate required fields before planning
- avoid writing issue updates unless the task has reached a valid milestone
