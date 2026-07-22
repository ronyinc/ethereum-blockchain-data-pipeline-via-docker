from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "rony",
}

with DAG(
    dag_id="dbt_run_job",
    default_args=default_args,
    start_date=datetime(2026, 7, 1),
    schedule=None,        # Manual trigger only
    catchup=False,
    tags=["dbt"],
) as dag:

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command="cd /opt/airflow/dbt && dbt build --target dev --select marts",
    )