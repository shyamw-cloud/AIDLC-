# GitHub Copilot instructions for AI SDLC repository

## Operating model

This repository is a starter framework for a skill-based AI SDLC. The system should behave like a structured software delivery pipeline, not a freeform prompt-only assistant.

## Required behavior

When working in this repository:
- treat Jira tickets as the primary source of task intent
- convert tickets into specs before coding
- decompose the spec into a plan before implementation
- validate outputs with automated tests
- keep changelogs, specs, and PR messages traceable to the ticket

## Output expectations

Every task should produce:
- a clear specification
- a short implementation plan
- code changes that map to the plan
- tests and validation evidence
- a brief PR summary

## Preferred workflow

1. Intake Jira ticket
2. Build spec
3. Generate plan
4. Implement changes
5. Run tests
6. Draft PR summary
7. Update Jira status

## Repo conventions

- Keep AI artifacts under `.ai/`
- Keep documentation under `docs/`
- Keep code under `ai_sdlc/`
- Keep tests under `tests/`
- Prefer deterministic, reviewable outputs over opaque prompt chains

## Notes

This repository intentionally models a prototype architecture. Implementations should be modular, reusable, and skill-driven.
