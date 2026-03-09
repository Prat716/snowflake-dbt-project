# my_first_python_model.py
#
# Simplest possible dbt Python model using Snowpark.
# Reads the upstream SQL model as a Snowpark DataFrame and returns it unchanged.
#
# Key points:
# - Every dbt Python model must define a model(dbt, session) function.
# - Only 'table' or 'incremental' materializations are supported (not 'view').
# - dbt.ref() works exactly like ref() in SQL models.
# - No explicit Snowpark imports are needed -- dbt injects them automatically.
#
# Run with: dbt run --select my_first_python_model


def model(dbt, session):
    # Must be 'table' or 'incremental' — views are not supported for Python models
    dbt.config(materialized="table", python_version="3.9")

    # Reference the upstream SQL model as a Snowpark DataFrame
    df = dbt.ref("my_first_dbt_model")

    return df
