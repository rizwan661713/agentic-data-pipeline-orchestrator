from src.failure_classifier import classify_failure


def test_schema_change_failure():
    result = classify_failure("Missing column customer_id in source file")

    assert result["category"] == "Schema Change"
    assert result["severity"] == "High"


def test_missing_file_failure():
    result = classify_failure("File not found in landing folder")

    assert result["category"] == "Missing Source File"
    assert result["severity"] == "High"


def test_permission_failure():
    result = classify_failure("Access denied while reading storage path")

    assert result["category"] == "Access Issue"
    assert result["severity"] == "High"


def test_unknown_failure():
    result = classify_failure("Unexpected system error")

    assert result["category"] == "Unknown Failure"
    assert result["severity"] == "Medium"


