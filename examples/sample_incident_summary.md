# Sample Incident Summary

## Incident Overview

A scheduled production pipeline failed during the schema validation step. The AI-assisted pipeline orchestrator reviewed the run metadata, error message, data quality results, and downstream dependency map to generate the summary below.

## AI-Generated Summary

Pipeline: `customer_activity_daily_load`

Environment: `production`

Status: `failed`

Failed Task: `validate_schema`

Likely Cause: Source schema changed. The incoming source file is missing the required `customer_id` column.

Priority: `High`

## Downstream Impact

The following downstream assets may be delayed or stale:

- `gold_customer_activity_summary`
- Executive Activity Dashboard

## Recommended Action

1. Confirm whether the source system intentionally removed or renamed `customer_id`.
2. Review the latest file layout and compare it against the expected schema.
3. Update the schema mapping if the change is approved.
4. Rerun the failed pipeline after validation.
5. Notify the analytics owner if the dashboard refresh will be delayed.

## Notes

This example demonstrates how pipeline metadata and dependency information can be used to create a clear operational summary for data engineering teams.

