-- my_second_dbt_model — a SQL view built on top of the first model.
-- Null IDs are filtered out here to demonstrate model chaining.

select *
from {{ ref('my_first_dbt_model') }}
where id is not null
