# my_second_python_model.py
#
# dbt Python model demonstrating a Snowpark Python UDF.
# The add_one UDF increments an integer by 1, handling NULL inputs gracefully.
# It must be defined inside model() because dbt wraps model code in a stored
# procedure, and UDF registration cannot run outside the handler.
#
# Run with: dbt run --select my_second_python_model

from snowflake.snowpark.functions import udf


def model(dbt, session):
    # Must be 'table' or 'incremental'
    dbt.config(materialized="table", python_version="3.9")

    # -----------------------------------------------------------------
    # Define and register a Python UDF inline.
    # NOTE: The UDF must be defined here, inside model(), so that it is
    #       registered within the stored procedure's execution context.
    # -----------------------------------------------------------------
    @udf
    def add_one(x: int) -> int:
        """Return x + 1, treating NULL as 0."""
        x = 0 if not x else x
        return x + 1

    # Reference the upstream SQL model as a Snowpark DataFrame
    df = dbt.ref("my_first_dbt_model")

    # Add a derived column using the UDF
    df = df.withColumn("id_plus_one", add_one(df["id"]))

    return df
