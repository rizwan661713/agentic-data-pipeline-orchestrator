"""
Agentic Data Pipeline Orchestrator

This module analyzes pipeline failures using metadata, data quality results,
and dependency information. It returns a plain-English incident summary that
can be sent to Slack, email, or a ticketing system.
"""

from typing import Any, Dict, List


def analyze_pipeline_failure(
    run_metadata: Dict[str, Any],
    dq_results: List[Dict[str, Any]],
    dependency_map: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Analyze a failed pipeline run and return an incident summary.

    Parameters:
        run_metadata: Pipeline run metadata such as status, failed task, and error message.
        dq_results: List of data quality check results for the pipeline run.
        dependency_map: List of downstream dependencies for the pipeline.

    Returns:
        Dictionary containing likely cause, impact, priority, and recommended action.
    """

    summary = {
        "pipeline_name": run_metadata.get("pipeline_name"),
        "environment": run_metadata.get("environment"),
        "status": run_metadata.get("status"),
        "failed_task": run_metadata.get("failed_task_name"),
        "likely_cause": "Unknown pipeline failure",
        "downstream_impact": [],
        "recommended_action": "Review detailed logs and retry after validation.",
        "priority": "Medium",
    }

    error_message = str(run_metadata.get("error_message", "")).lower()

    if "missing column" in error_message or "schema" in error_message:
        summary["likely_cause"] = "Schema change detected in source data"
        summary["recommended_action"] = (
            "Review the source schema and update the mapping if the change is approved."
        )
        summary["priority"] = "High"

    elif "file not found" in error_message or "missing file" in error_message:
        summary["likely_cause"] = "Expected source file did not arrive"
        summary["recommended_action"] = (
            "Check the source delivery process and confirm file availability."
        )
        summary["priority"] = "High"

    elif dq_results and any(result.get("status") == "failed" for result in dq_results):
        failed_checks = [
            result.get("check_name")
            for result in dq_results
            if result.get("status") == "failed"
        ]

        summary["likely_cause"] = "Data quality validation failed"
        summary["recommended_action"] = (
            f"Review failed data quality checks: {', '.join(failed_checks)}."
        )
        summary["priority"] = "Medium"

    summary["downstream_impact"] = [
        item.get("downstream_report")
        for item in dependency_map
        if item.get("pipeline_name") == run_metadata.get("pipeline_name")
        and item.get("downstream_report")
    ]

    return summary


if __name__ == "__main__":
    sample_run_metadata = {
        "pipeline_name": "customer_activity_daily_load",
        "environment": "production",
        "status": "failed",
        "failed_task_name": "validate_schema",
        "error_message": "Missing column customer_id in source file",
    }

    sample_dq_results = []

    sample_dependency_map = [
        {
            "pipeline_name": "customer_activity_daily_load",
            "downstream_report": "Executive Activity Dashboard",
        }
    ]

    incident_summary = analyze_pipeline_failure(
        sample_run_metadata,
        sample_dq_results,
        sample_dependency_map,
    )

    print(incident_summary)








