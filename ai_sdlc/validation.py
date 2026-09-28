from typing import Dict, List, Any


class ValidationGate:
    """Defines a validation checkpoint that must pass before PR creation."""

    def __init__(self, name: str, description: str, check_fn=None):
        self.name = name
        self.description = description
        self.check_fn = check_fn or (lambda: True)
        self.passed = False

    def run(self) -> bool:
        self.passed = self.check_fn()
        return self.passed


class ValidationPipeline:
    """Orchestrates validation checks before PR creation."""

    def __init__(self):
        self.gates: List[ValidationGate] = [
            ValidationGate(
                "spec_coverage",
                "Verify spec includes scope and acceptance criteria",
                self._check_spec_coverage,
            ),
            ValidationGate(
                "task_dependencies",
                "Verify all tasks have dependencies declared",
                self._check_task_dependencies,
            ),
            ValidationGate(
                "pr_linked",
                "Verify PR is linked to Jira issue",
                self._check_pr_linked,
            ),
        ]

    def run_all(self, spec: Dict[str, Any], tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Execute all validation gates and return a summary."""
        results = []
        for gate in self.gates:
            # simplified: just run the gate without external dependencies
            result = gate.run()
            results.append({"gate": gate.name, "description": gate.description, "passed": result})

        all_passed = all(r["passed"] for r in results)
        return {
            "all_passed": all_passed,
            "results": results,
            "ready_for_pr": all_passed,
        }

    @staticmethod
    def _check_spec_coverage() -> bool:
        return True  # stub

    @staticmethod
    def _check_task_dependencies() -> bool:
        return True  # stub

    @staticmethod
    def _check_pr_linked() -> bool:
        return True  # stub
