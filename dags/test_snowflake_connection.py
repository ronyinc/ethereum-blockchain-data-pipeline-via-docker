from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook


def test_snowflake():
    hook = SnowflakeHook(snowflake_conn_id="snowflake_default")

    sql = """
    SELECT
        CURRENT_DATABASE(),
        CURRENT_SCHEMA(),
        CURRENT_VERSION();
    """

    result = hook.get_first(sql)

    print(f"Current Database : {result[0]}")
    print(f"Current Schema   : {result[1]}")
    print(f"Current Version  : {result[2]}")


with DAG(
    dag_id="test_snowflake_connection",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    tags=["snowflake"],
) as dag:

    test = PythonOperator(
        task_id="test_connection",
        python_callable=test_snowflake,
    )