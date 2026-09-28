# Contribution guidelines

## Adding a new skill

Skills are modular, reusable units of work. To add one:

1. Create a new file in `ai_sdlc/skills/` (e.g., `backend_api_skill.py`)
2. Implement a skill class with an `execute()` method
3. Register it in the skill registry
4. Add tests in `tests/`
5. Update the README with the skill

## Example skill

```python
class BackendAPISkill:
    def execute(self, spec, context):
        # Generate backend API code from spec
        return {"files": [...], "tests": [...]}
```

## Updating the orchestrator

The orchestrator is the coordination layer. Changes here should:
- Add a new phase or layer
- Preserve the 7-phase structure (intake → spec → plan → tasks → PR → GitHub → Jira)
- Include tests
- Update docs

## Review guidelines

- Ensure all tests pass
- Validate JSON output contracts
- Check that Jira and GitHub interactions are mocked correctly
- Confirm spec coverage in PR descriptions
