# AI SDLC framework overview

This project creates a lightweight, spec-driven AI SDLC scaffold for GitHub Copilot-style workflows. It includes the following layers:

- Jira/MCP intake
- specification generation
- task planning
- execution orchestration
- validation checks
- PR drafting
- Jira status synchronization

## Architecture

```text
Jira issue -> MCP adapter -> Ticket model -> Spec builder -> Plan builder -> Orchestrator -> Code + tests -> PR summary -> Jira update
```

## Goals

- Reduce context loss between ticket intake and implementation
- Make AI-generated work traceable to explicit requirements
- Standardize planning and validation before PR creation
- Build reviewable, reusable automation around SDLC tasks

## Key concepts

### Spec-first
The system should not begin coding before a structured spec exists. The spec acts as the contract for implementation.

### Skill-based
The framework is composed of modules, not one monolithic prompt. Examples include:
- issue intake
- risk analysis
- task planning
- coding
- validation
- PR authoring

### PR-oriented
Every task should end with a review-ready pull request summary that references the ticket and validation evidence.
