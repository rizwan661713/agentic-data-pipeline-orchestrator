-- Pipeline Dependency Map
-- Stores upstream and downstream relationships for pipelines, tasks, tables, and reports.

create or replace table ops.pipeline_dependency_map (
    pipeline_name varchar,
    task_name varchar,
    upstream_task_name varchar,
    downstream_task_name varchar,
    target_table varchar,
    downstream_report varchar,
    business_owner varchar
);

