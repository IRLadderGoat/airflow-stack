from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
def dbt_run(model):
    return f"""

    cd doa_dbt &&
    dbt run --models {model}"""

with DAG(dag_id='trigger_jobindsats_job_load',
         default_args={'owner': 'airflow', 'dir': 'doa_dbt'},
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

    dt_begin = BashOperator(task_id='data_transform_begin',bash_command='sleep 10' )

    subjects_transform = DbtRunOperator(task_id='transform_subjects', models="jobindsats_subjects")

    subjects_test = DbtTestOperator(task_id='test_subjects', models="jobindsats_subjects")

    tables_transform = DbtRunOperator(task_id='transform_tables', models="jobindsats_tables")

    tables_test = DbtTestOperator(task_id='test_tables', models="jobindsats_tables")

    tables_measurements_transform = DbtRunOperator(task_id='transform_tables_measurements', models="jobindsats_tables_measurements")

    tables_measurements_test = DbtTestOperator(task_id='test_tables_measurements', models="jobindsats_tables_measurements")

    tables_dimensions_transform = DbtRunOperator(task_id='transform_tables_dimensions', models="jobindsats_tables_dimensions")

    tables_dimensions_test = DbtTestOperator(task_id='test_tables_dimensions', models="jobindsats_tables_dimensions")

    tables_areahierachy_transform = DbtRunOperator(task_id='transform_tables_hierachy', models="jobindsats_tables_hierachy")

    tables_areahierachy_test = DbtTestOperator(task_id='test_tables_hierachy', models="jobindsats_tables_hierachy")

    dt_end = BashOperator(task_id='data_transform_end',bash_command='sleep 10' )


    api_json_psql >> dt_begin >> subjects_transform >> subjects_test >>\
    tables_transform >> tables_test >> tables_measurements_transform >>\
    tables_measurements_test >> tables_dimensions_transform >> \
    tables_dimensions_test >> tables_areahierachy_transform >> \
    tables_areahierachy_test >> dt_end
