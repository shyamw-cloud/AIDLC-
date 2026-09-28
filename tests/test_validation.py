from ai_sdlc.validation import ValidationPipeline


def test_validation_pipeline_checks_gates():
    pipeline = ValidationPipeline()
    spec = {"scope": ["add feature"], "acceptance_criteria": ["feature works"]}
    tasks = [{"id": "T1", "title": "Implement", "dependencies": []}]

    result = pipeline.run_all(spec, tasks)

    assert result["all_passed"] is True
    assert result["ready_for_pr"] is True
    assert len(result["results"]) > 0
