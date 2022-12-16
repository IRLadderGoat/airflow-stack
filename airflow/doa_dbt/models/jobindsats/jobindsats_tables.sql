{{ config(materialized='table') }}

select
  _airbyte_data->'TableID' as TableID,
  _airbyte_data->'SubjectID' as SubjectID,
  _airbyte_data->'TableName' as TableName,
  _airbyte_data->'NextUpdate' as NextUpdate,
  _airbyte_data->'FirstPeriod' as FirstPeriod,
  _airbyte_data->'SubjectName' as SubjectName,
  _airbyte_data->'LatestPeriod' as LatestPeriod,
  _airbyte_data->'LatestUpdate' as LatestUpdate,
  _airbyte_data->'UpdateFrequency' as UpdateFrequency
  from _airbyte_raw_jobindsats_tables
