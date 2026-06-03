# Operating Model

## Purpose

This document explains how the Agentic Data Pipeline Orchestrator supports day-to-day data engineering operations.

The goal is to reduce manual troubleshooting time by combining pipeline metadata, data quality results, dependency mapping, and AI-assisted incident summaries.

## How the Process Works

1. A pipeline runs through an orchestrator such as Databricks Workflows, Airflow, dbt Cloud, or Snowflake Tasks.
2. The pipeline writes execution details to the pipeline metadata store.
3. Data quality checks run after ingestion and transformation steps.
4. If a failure occurs, the AI agent reviews the error message, metadata, quality results, and dependency map.
5. The agent creates a clear incident summary with likely cause, downstream impact, priority, and recommended action.
6. The notification builder formats the message for Slack, email, ticketing, or dashboard use.

## Operational Roles

### Data Engineer

Responsible for:
- Reviewing failed pipeline runs
- Validating the AI-generated summary
- Fixing source, transformation, or data quality issues
- Rerunning pipelines when needed

### Data Owner

Responsible for:
- Confirming business impact
- Approving source schema changes
- Communicating delays to business users

### Analytics Owner

Responsible for:
- Validating dashboard impact
- Confirming whether reporting outputs are stale or delayed

## Failure Handling Pattern

```text
Pipeline Failure
   |
   v
Classify Failure Type
   |
   v
Check Data Quality Results
   |
   v
Identify Downstream Impact
   |
   v
Generate Incident Summary
   |
   v
Send Notification
   |
   v
Resolve and Rerun
```

## Common Failure Types

- Missing source file
- Empty source file
- Schema change
- Data type mismatch
- Duplicate records
- Missing required fields
- Record count anomaly
- Permission issue
- Runtime timeout
- Downstream dependency failure

## Example Severity Rules

| Failure Type | Severity | Reason |
|---|---|---|
| Missing source file | High | Pipeline cannot continue without expected input |
| Schema change | High | Downstream models may break or produce incorrect results |
| Permission issue | High | Pipeline may be blocked across environments |
| Duplicate records | Medium | May impact metrics but can often be isolated |
| Null required fields | Medium | Usually requires data quality investigation |
| Runtime timeout | Medium | May be solved through retry, tuning, or scaling |

## Success Criteria

The orchestrator is successful when:

- Pipeline failures are easier to understand
- Root cause analysis takes less time
- Downstream report impact is visible
- Data quality issues are captured consistently
- Notifications are clear and actionable
- Teams spend less time manually reading logs
- 




