# PR workflow

The framework should create pull requests in a structured, evidence-based manner.

## PR creation stages

1. Create or update feature branch.
2. Commit code changes.
3. Run validation checks.
4. Generate summary notes from the ticket spec.
5. Draft PR title and body.
6. Link Jira issue in PR description.
7. Submit PR for review.

## PR body template

```markdown
## Summary
- Fixes JIRA-1042
- Adds support for X

## Spec coverage
- requirement 1
- requirement 2
- acceptance criteria 3

## Validation
- pytest
- lint
- build check

## Risks
- dependency on Jira MCP access
- need for additional review on permissions
```

## Recommendation

Keep PR descriptions grounded in the ticket spec and validation output so reviewers can quickly confirm correctness.
