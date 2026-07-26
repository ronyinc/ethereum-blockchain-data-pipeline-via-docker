from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
import logging
import time

logger = logging.getLogger(__name__)

DATE_PATTERN_SQL = """
SET CURRENT_DATE_PATTERN = (
                SELECT CONCAT(
                    '.*date=(',
                    TO_VARCHAR(CURRENT_DATE() - 1, 'YYYY-MM-DD'),
                    '|',
                    TO_VARCHAR(CURRENT_DATE() - 2, 'YYYY-MM-DD'),
                    '|',
                    TO_VARCHAR(CURRENT_DATE() - 3, 'YYYY-MM-DD'),
                    ').*'
                )
            );
"""


def load_contracts():
    """
    Load the latest three days of contract data
    from the Snowflake external stage into the RAW table.
    """
    logger.info("Starting CONTRACTS load...")

    hook = SnowflakeHook(
        snowflake_conn_id="snowflake_default"
        )

    sql = DATE_PATTERN_SQL + """
            COPY INTO RAW.ETH_SCHEMA.CONTRACTS
            FROM (
                SELECT
                    t.$1:address,
                    t.$1:block_hash,
                    t.$1:block_number,
                    t.$1:block_timestamp,
                    t.$1:bytecode,
                    t.$1:date,
                    t.$1:last_modified
                FROM @RAW.ETH_SCHEMA.CONTRACTS_STAGE t
            )
            PATTERN = $CURRENT_DATE_PATTERN;
    """
    start = time.time()

    hook.run(sql, autocommit=True)
    logger.info(
        "Finished CONTRACTS load. in %.2f seconds",
        time.time() - start
        )


def load_token_transfers():
    """
    Load the latest three days of token transfers data
    from the Snowflake external stage into the RAW table.
    """
    logger.info("Starting TOKEN_TRANSFERS load...")


    hook = SnowflakeHook(
        snowflake_conn_id="snowflake_default"
        )

    sql = DATE_PATTERN_SQL + """
            COPY INTO RAW.ETH_SCHEMA.TOKEN_TRANSFERS
            FROM (
                select
                    t.$1:block_hash,
                    t.$1:block_number,
                    t.$1:block_timestamp,
                    t.$1:date,
                    t.$1:from_address,
                    t.$1:to_address,
                    t.$1:last_modified,
                    t.$1:log_index,
                    t.$1:token_address,
                    t.$1:transaction_hash,
                    t.$1:value
                
                from @RAW.ETH_SCHEMA.TOKEN_TRANSFERS_STAGE t
  
            )
            PATTERN = $CURRENT_DATE_PATTERN;
    """
    start = time.time()

    hook.run(sql, autocommit=True)
    logger.info(
                 "Finished TOKEN TRANSFERS load in %.2f seconds",
                 time.time() - start
                )


def load_transactions():
    """
        Load the latest three days of transactions data
        from the Snowflake external stage into the RAW table.
    """
    logger.info("Starting TRANSACTIONS load...")

    hook = SnowflakeHook(
        snowflake_conn_id="snowflake_default"
        )

    sql = DATE_PATTERN_SQL + """
            COPY INTO RAW.ETH_SCHEMA.TRANSACTIONS
		    FROM (
        		select
                		t.$1:block_hash,
                		t.$1:block_number,
                		t.$1:block_timestamp,
                		t.$1:date,
                		t.$1:from_address,
                		t.$1:gas,
                		t.$1:gas_price,
                		t.$1:hash,
                		t.$1:input,
                		t.$1:last_modified,
                		t.$1:max_fee_per_gas,
                		t.$1:max_priority_fee_per_gas,
                		t.$1:nonce,
                		t.$1:receipt_contract_address,
                		t.$1:receipt_cumulative_gas_used,
                		t.$1:receipt_effective_gas_price,
                		t.$1:receipt_gas_used,
                		t.$1:receipt_status,
                		t.$1:to_address,
                		t.$1:transaction_index,
                		t.$1:transaction_type,
                		t.$1:value

		from @RAW.ETH_SCHEMA.TRANSACTIONS_STAGE t
  
		)
		PATTERN = $CURRENT_DATE_PATTERN;
    """

    start = time.time()

    hook.run(sql, autocommit=True)
    logger.info(
                 "Finished TRANSACTIONS load in %.2f seconds",
                 time.time() - start
                )

default_args = {
    "owner": "rony",
    "retries": 2,
}


with DAG(
    dag_id="load_ethereum_source_data",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    tags=["ethereum","snowflake","dbt"],
    default_args=default_args
) as dag:

    t1 = PythonOperator(
        task_id="load_source_contracts",
        python_callable=load_contracts,
    )
    t2 = PythonOperator(
        task_id="load_source_token_transfers",
        python_callable=load_token_transfers,
    )
    t3 = PythonOperator(
         task_id="load_source_transactions",
         python_callable=load_transactions,
    )
    [t1, t2, t3]