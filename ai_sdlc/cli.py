import argparse
import json

from ai_sdlc.orchestrator import Orchestrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AI SDLC orchestration CLI: fetch a Jira ticket, build a spec, plan tasks, and validate workflow state."
    )
    parser.add_argument("ticket_id", nargs="?", default="JIRA-1042", help="Jira issue ID to process")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the orchestration result as JSON",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    orchestrator = Orchestrator()
    result = orchestrator.run(args.ticket_id)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Ticket: {result['ticket']['key']} - {result['ticket']['summary']}")
        print("\nSpec summary:")
        print(result["spec"]["summary"])
        print("\nExecution plan:")
        for index, step in enumerate(result["plan"], start=1):
            print(f"{index}. {step}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
