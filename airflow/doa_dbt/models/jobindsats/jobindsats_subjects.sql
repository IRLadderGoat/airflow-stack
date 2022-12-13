{{ config(materialized='table') }}

select
  _airbyte_data->'SubjectID' as SubjectID,
  _airbyte_data->'SubjectName' as SubjectName
from _airbyte_raw_jobindsats_subjects
