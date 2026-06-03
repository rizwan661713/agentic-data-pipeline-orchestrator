-- Data Quality Results Table
-- Stores validation check results for each pipeline run.

create or replace table ops.data_quality_results (
    check_id varchar,
    pipeline_run_id varchar,
    table_name varchar,
    check_name varchar,
    check_type varchar,
    status varchar,
    failed_record_count number,
    threshold_value number,
    actual_value number,
    check_timestamp timestamp
);

