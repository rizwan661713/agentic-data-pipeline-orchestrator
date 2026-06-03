-- Pipeline Run History Table
-- Stores each pipeline execution with status, runtime, failed task, and error details.

create or replace table ops.pipeline_run_history (
    pipeline_run_id varchar,
    pipeline_name varchar,
    environment varchar,
    status varchar,
    start_time timestamp,
    end_time timestamp,
    duration_seconds number,
    failed_task_name varchar,
    error_message varchar,
    retry_count number,
    triggered_by varchar,
    created_at timestamp
);

