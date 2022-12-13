{{ config(materialized='table') }}

select
  _airbyte_data->'TableID' as TableId,
  _airbyte_data->'SubjectID' as SubjectID,
  _airbyte_data->'TableName' as TableName,
  _airbyte_data->'NextUpdate' as NextUpdate,
  _airbyte_data->'FirstPeriod' as FirstPeriod,
  _airbyte_data->'SubjectName' as SubjectName,
  _airbyte_data->'LatestPeriod' as LatestPeriod,
  _airbyte_data->'LatestUpdate' as LatestUpdate,
  _airbyte_data->'UpdateFrequency' as UpdateFrequency
  from _airbyte_raw_jobindsats_tables


--  "Dimensions": [{"DimensionID": "_erhvervsgrp_jo", "DimensionName": "Erhvervsområder"}],
--  "Measurements": [{"ID": "mgrpjo01_1", "Name": "Antal oprettede jobordrer"}, {"ID": "mgrpjo01_2", "Name": "Antal stillinger blandt oprettede jobordrer"}, {"ID": "mgrpjo01_3", "Name": "Formidlingsgrad"}, {"ID": "mgrpjo01_4", "Name": "Besættelsesgrad"}],
--  "AreaHierarchy": ["Hele landet", "rar", "jobcent"], "PeriodCategory": ["M", "Q"],
