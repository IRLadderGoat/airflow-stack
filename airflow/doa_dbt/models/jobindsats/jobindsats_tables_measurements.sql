{{ config(materialized='table') }}

with a as (
  select _airbyte_data->'TableID' as t,
         _airbyte_data->'Measurements' as d
    from _airbyte_raw_jobindsats_tables
) select t as TableID,
         value->'ID' as measureid,
         value->'Name' as measurename
  from a c
  cross join lateral jsonb_array_elements(c.d)


--  "AreaHierarchy": ["Hele landet", "rar", "jobcent"], "PeriodCategory": ["M", "Q"],
