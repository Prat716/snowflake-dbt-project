# snowflake-dbt-project

A dbt project demonstrating **Snowpark Python models** on Snowflake, following the
[Data Engineering with Snowpark Python and dbt](https://www.snowflake.com/en/developers/guides/data-engineering-with-snowpark-python-and-dbt/) quickstart guide.

---

## Prerequisites

| Requirement | Notes |
|---|---|
| Snowflake account | Free trial works |
| `DEMO_DB` database | Create it in Snowflake before running |
| Anaconda | [Install guide](https://docs.anaconda.com/anaconda/install/) |
| Git | For cloning this repo |

---

## Setup

### 1. Create & activate the Conda environment

```bash
conda env create -f environment.yml
conda activate snowflake-dbt-env
```

### 2. Configure your Snowflake connection

Copy `profiles.yml` from the project root to `~/.dbt/` and fill in your credentials:

```bash
# Windows (PowerShell)
Copy-Item profiles.yml "$env:USERPROFILE\.dbt\profiles.yml"
```

Then open `~/.dbt/profiles.yml` and replace every `<placeholder>` with your real values:

| Placeholder | Example value |
|---|---|
| `<your_account>` | `xy12345.us-east-1` |
| `<your_username>` | `JSMITH` |
| `<your_password>` | your Snowflake password |
| `<your_role>` | `SYSADMIN` |
| `<your_warehouse>` | `COMPUTE_WH` |

### 3. Verify the connection

```bash
dbt debug
```

---

## Running the project

### Run all models

```bash
dbt run
```

This creates the following objects in `DEMO_DB.DEMO_SCHEMA`:

| Object | Type | Description |
|---|---|---|
| `my_first_dbt_model` | table | Base SQL model — source data with an id column |
| `my_second_dbt_model` | view | SQL view filtering nulls from the base model |
| `my_first_python_model` | table | Snowpark Python model — mirrors the base table |
| `my_second_python_model` | table | Snowpark Python model with a UDF (`id_plus_one`) |

### Run a single model

```bash
dbt run --select my_second_python_model
```

### Run tests

```bash
dbt test
```

### Compile (without running) to inspect generated SQL/Python

```bash
dbt compile
```

Compiled files appear in `target/compiled/`. The stored-procedure code that dbt
generates for each Python model is especially useful for debugging.

---

## Project structure

```
snowflake-dbt-project/
├── dbt_project.yml                  # Project config
├── profiles.yml                     # Connection profile template (copy to ~/.dbt/)
├── environment.yml                  # Conda environment spec
└── models/
    └── example/
        ├── schema.yml               # Model documentation & tests
        ├── my_first_dbt_model.sql   # Base SQL table
        ├── my_second_dbt_model.sql  # SQL view (filters nulls)
        ├── my_first_python_model.py # Simple Snowpark Python model
        └── my_second_python_model.py# Snowpark Python model with UDF
```

---

## How dbt Python models work on Snowflake

1. **You write** a `model(dbt, session)` function in a `.py` file.
2. **dbt compiles** it into a Snowflake stored procedure (LANGUAGE PYTHON, Snowpark runtime 3.8).
3. **dbt executes** the stored procedure inside Snowflake — no Python runs locally.
4. **The result DataFrame** is materialized as a table or incremental model.

See `target/compiled/` after running `dbt compile` to inspect the full generated code.

---

## Resources

- [Snowpark Developer Guide for Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index.html)
- [dbt Python models docs](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/python-models)
- [dbt-snowflake adapter](https://docs.getdbt.com/docs/core/connect-data-platform/snowflake-setup)
