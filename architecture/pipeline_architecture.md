# Pipeline Architecture

## Overview

The Agentic Data Pipeline Orchestrator is designed to improve the reliability and supportability of modern data pipelines.

It combines pipeline metadata, data quality checks, dependency mapping, and AI-assisted incident summaries to help data engineering teams quickly understand failures and take action.

## High-Level Architecture

```text
Source Systems / Files / APIs
   |
   v
Pipeline Orchestrator
Airflow / Databricks Workflows / dbt Cloud Jobs
   |
   v
Pipeline Metadata Store
Run history, task status, errors, and retries
   |
   v
Data Quality Layer
Validation checks, anomaly detection, and failed records
   |
   v
Dependency Map
Target tables, reports, owners, and downstream impact
   |
   v
AI Agent Layer
Root cause summary and recommended action
   |
   v
Notification Layer
Slack, email, ticket, or dashboard alert
```

## Main Design Principles

### Metadata-Driven

Every pipeline run should produce operational metadata such as status, duration, failed task, error message, retry count, and environment.

### Quality-Aware

Data quality checks are treated as first-class pipeline steps, not optional afterthoughts.

### Impact-Focused

Failures are connected to downstream tables, dashboards, and business owners so teams understand what is affected.

### Human-Readable

The AI agent converts technical pipeline details into clear summaries that engineers and analysts can quickly understand.

## Example Failure Flow

```text
1. Pipeline fails during schema validation
2. Metadata store captures failed task and error message
3. Data quality layer confirms required column is missing
4. Dependency map identifies impacted dashboard
5. AI agent creates incident summary
6. Notification is sent to the data engineering team
7. Engineer validates the issue and reruns after correction
```

## Example Output

```text
Pipeline: customer_activity_daily_load
Status: Failed
Failed Task: validate_schema
Likely Cause: Schema change detected in source data
Downstream Impact: Executive Activity Dashboard
Recommended Action: Review the source schema and update the mapping if approved
Priority: High
```

## Future Enhancements

- Add integration with Slack API
- Add GitHub Actions workflow for Python validation
- Add unit tests for failure classification
- Add sample Airflow DAG
- Add Databricks Workflow example
- Add OpenAI or Azure OpenAI integration for LLM-generated summaries


