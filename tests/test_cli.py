from ai_sdlc.cli import main


def test_cli_runs_without_error(capsys):
    import sys

    original_argv = sys.argv[:]
    try:
        sys.argv = ["ai_sdlc", "JIRA-1042"]
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "JIRA-1042" in captured.out
        assert "Spec summary" in captured.out
    finally:
        sys.argv = original_argv
