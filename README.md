# AIDLC- AI SDLC Framework

This repository now includes a starter implementation for a skill-based, spec-driven AI SDLC workflow for GitHub Copilot.

The goal is to support a Jira-through-MCP development lifecycle:
- fetch Jira tickets
- create a structured specification
- generate a task plan
- implement code changes
- validate output
- create a pull request summary

## Repository structure

- `ai_sdlc/` — Python framework skeleton
- `tests/` — unit tests for the orchestration flow
- `docs/` — architecture and workflow documentation
- `.ai/` — spec and planning templates
- `.github/copilot-instructions.md` — Copilot-specific guidance for this repo

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## Example orchestration

```python
from ai_sdlc.orchestrator import Orchestrator

orchestrator = Orchestrator()
result = orchestrator.run("JIRA-1042")
print(result["spec"]["summary"])
print(result["plan"]) 
```

## Workflow

1. Fetch Jira ticket via MCP
2. Normalize the issue into a structured ticket model
3. Generate a specification document
4. Build the implementation plan from that spec
5. Execute the declared tasks
6. Validate build/test status
7. Draft PR text and update Jira status

## Current implementation

This repo contains a working prototype framework with:
- Jira/MCP-style ticket interface
- spec generation from a ticket
- planning from acceptance criteria
- orchestrated execution flow
- sample tests

This is designed to be extended with actual Jira MCP integration and repository-specific skills.
