/*
    my_first_dbt_model — the base SQL model.
    A table is materialized so downstream Python models can reference it.
*/

{{ config(materialized='table') }}

with source_data as (
    select 1 as id
    union all
    select null as id
)

select *
from source_data
