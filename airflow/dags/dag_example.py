from airflow import DAG
from airflow.utils.dates import days_ago
#from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash import BashOperator
##from time import sleep

with DAG(dag_id='trigger_test_transform',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
    ) as dag:
    def generate():
        dummy_op = BashOperator(task_id='data_transform_begin', bash_command='sleep 10', wait_for_downstream=True)

        dummy_op2 = BashOperator(task_id='data_transform_end', bash_command='sleep 10', wait_for_downstream=True)

        dummy_op3 = BashOperator(task_id='data_exchange_begin', bash_command='sleep 10', wait_for_downstream=True)

        dummy_op4 = BashOperator(task_id='data_exchange_end', bash_command='sleep 10', wait_for_downstream=True)

        return dummy_op >> dummy_op2 >> dummy_op3 >> dummy_op4

    generate()
