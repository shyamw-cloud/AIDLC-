# AI SDLC framework specification

## User story
As a GitHub Copilot user, I want a skill-based SDLC pipeline that can read Jira tickets via MCP, turn them into a spec and plan, generate code, and create a PR so that work is structured, reviewable, and traceable.

## Scope
- Jira MCP ticket retrieval
- specification generation
- planning and task decomposition
- orchestration of code generation and validation
- PR drafting and Jira status updates

## Acceptance criteria
- A valid issue key resolves to a normalized ticket object.
- The system produces a specification before implementation begins.
- The specification is turned into a task plan.
- The plan includes validation steps.
- The workflow can return a PR-ready summary.
- The framework is modular and can be extended with custom skills.

## Risks
- MCP connectivity issues
- ambiguous ticket acceptance criteria
- inconsistent repositories and branch conventions
- missing validation pipeline before PR creation

## Non-goals
- Full multi-user orchestration in v1
- Real Jira server deployment in this starter scaffold
- Complete production security hardening
