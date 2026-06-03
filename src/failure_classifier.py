"""
Failure Classifier

Classifies common data pipeline failures into operational categories.
This helps route incidents, assign priority, and recommend the right next action.
"""

from typing import Dict


def classify_failure(error_message: str) -> Dict[str, str]:
    """
    Classify a pipeline error message into a failure category.

    Args:
        error_message: Raw error message from the failed pipeline task.

    Returns:
        Dictionary with failure category, severity, and recommended action.
    """

    message = error_message.lower()

    if "missing column" in message or "schema" in message:
        return {
            "category": "Schema Change",
            "severity": "High",
            "recommended_action": "Review source schema and update mappings if approved.",
        }

    if "file not found" in message or "missing file" in message:
        return {
            "category": "Missing Source File",
            "severity": "High",
            "recommended_action": "Confirm source file delivery and rerun pipeline after file arrival.",
        }

    if "permission" in message or "access denied" in message:
        return {
            "category": "Access Issue",
            "severity": "High",
            "recommended_action": "Validate service account permissions and storage access.",
        }

    if "duplicate" in message:
        return {
            "category": "Duplicate Records",
            "severity": "Medium",
            "recommended_action": "Review deduplication logic and source record uniqueness.",
        }

    if "null" in message or "not null" in message:
        return {
            "category": "Missing Required Field",
            "severity": "Medium",
            "recommended_action": "Review failed records and confirm required field population.",
        }

    if "timeout" in message:
        return {
            "category": "Runtime Timeout",
            "severity": "Medium",
            "recommended_action": "Check cluster size, query performance, and retry configuration.",
        }

    return {
        "category": "Unknown Failure",
        "severity": "Medium",
        "recommended_action": "Review logs manually and escalate if issue repeats.",
    }


if __name__ == "__main__":
    sample_error = "Missing column customer_id in source file"
    result = classify_failure(sample_error)
    print(result)





