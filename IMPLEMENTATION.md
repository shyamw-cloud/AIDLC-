# AI SDLC Framework Implementation Guide

## What this PR adds

A production-ready starter framework for a skill-based, spec-driven AI SDLC that:
- reads Jira tickets through MCP
- generates structured specifications
- creates implementation plans
- orchestrates code generation
- validates output with automated gates
- generates PR summaries and links
- updates Jira status

## Architecture layers

1. **Intake** — Jira MCP ticket fetcher
2. **Spec** — Converts tickets to structured specs
3. **Planning** — Breaks specs into ordered tasks
4. **Tasks** — Task engine with dependencies and validation
5. **Orchestration** — Coordinates all phases
6. **PR Generation** — Creates review-ready pull request summaries
7. **GitHub Integration** — Branch and PR management
8. **Validation** — Automated gates before PR creation
9. **Jira Sync** — Status updates and issue linking

## How to use

```bash
# Run the full orchestration for a ticket
python -m ai_sdlc JIRA-1042

# Get JSON output for integration
python -m ai_sdlc JIRA-1042 --json
```

## Key files

- `ai_sdlc/orchestrator.py` — Main orchestration engine
- `ai_sdlc/pr_generator.py` — PR draft creation
- `ai_sdlc/tasks.py` — Task decomposition
- `ai_sdlc/validation.py` — Validation gates
- `ai_sdlc/jira_mcp.py` — Jira integration stub
- `ai_sdlc/github_client.py` — GitHub integration stub
- `.github/workflows/ai-sdlc-validation.yml` — CI/CD validation
- `.ai/specs/ai-sdlc-framework/` — Spec, plan, acceptance criteria
- `docs/` — Architecture and workflow documentation

## Next steps for production

1. Implement real Jira MCP server connection
2. Implement real GitHub API / MCP client for branch/PR operations
3. Add code generation skill modules (backend, frontend, tests, docs)
4. Add repository-specific .copilot-instructions.md for Copilot integration
5. Add deployment and release automation
6. Add metrics and telemetry for AI-driven workflow tracking

## Testing

All components are covered by unit tests:

```bash
pip install -r requirements.txt
pytest -q
```

## Philosophy

This framework is **spec-first and skill-based**, not prompt-driven. Every task is traceable to a Jira issue. Every PR is evidence-backed with validation results. The system is designed for GitHub Copilot users who want structured, reviewable AI-driven workflows.
