from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.empty import EmptyOperator
from time import sleep

with DAG(dag_id='trigger_jobindsats_job_load',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
    ) as dag:

    api_json_psql = AirbyteTriggerSyncOperator(
        task_id='airbyte_jobindsats_api_json',
        airbyte_conn_id='airbyte',
        connection_id='35120c9e-69d3-4b0c-9c41-70d2ae46be7b',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    dummy_op = EmptyOperator(task_id='data_transform_begin',wait_for_downstream=True)

    sleep(10)

    dummy_op = EmptyOperator(task_id='data_transform_end',wait_for_downstream=True)
