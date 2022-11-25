from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.empty import EmptyOperator
from time import sleep

with DAG(dag_id='trigger_jobindsats_job_load',
         default_args={'owner': 'airflow'},
         schedule_interval='@hourly',
         start_date=days_ago(1)
    ) as dag:

    def generate():
        api_json_psql = AirbyteTriggerSyncOperator(
            task_id='airbyte_jobindsats_api_json',
            airbyte_conn_id='airbyte',
            connection_id='35120c9e-69d3-4b0c-9c41-70d2ae46be7b',
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        dt_begin = BashOperator(task_id='data_transform_begin',bash_command='sleep 10',wait_for_downstream=True)


        dt_end = BashOperator(task_id='data_transform_end',bash_command='sleep 10',wait_for_downstream=True)


        return api_json_psql >> dt_begin >> dt_end
    generate()
