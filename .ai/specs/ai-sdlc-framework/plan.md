# AI SDLC framework plan

## Phase 1: Ticket intake
- Connect to Jira via MCP
- Read issue payload
- Normalize fields into internal model

## Phase 2: Spec creation
- Summarize business goal
- Extract acceptance criteria
- Identify risks, constraints, and edge cases

## Phase 3: Planning
- Build task list from spec
- Sequence tasks and validation gates
- Identify which repository files and skills are needed

## Phase 4: Execution
- Implement code changes
- Add or update tests
- Update docs when needed

## Phase 5: Validation
- Run tests
- Run lint or type checks if configured
- Fix failing items

## Phase 6: PR generation
- Create branch and commit changes
- Draft PR summary
- Link Jira issue
- Submit PR

## Phase 7: Jira sync
- Update issue status
- Add progress comment with PR link
