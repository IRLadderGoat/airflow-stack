{{ config(materialized='table') }}

with a as (
  select _airbyte_data->'TableID' as t,
         _airbyte_data->'Dimensions' as d
    from _airbyte_raw_jobindsats_tables
) select t as TableID,
         value->'DimensionID' as dimensionid,
         value->'DimensionName' as dimensionname
  from a c
  cross join lateral jsonb_array_elements(c.d)
