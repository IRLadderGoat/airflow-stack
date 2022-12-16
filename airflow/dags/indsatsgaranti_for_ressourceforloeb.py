from airflow import DAG
from airflow.utils.dates import days_ago
#from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash import BashOperator
##from time import sleep

with DAG(dag_id='indsatsgaranti_for_ressourceforløb',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
    ) as dag:
    dummy_op = BashOperator(task_id='styring_init', bash_command='sleep 10')

    dummy_op1 = BashOperator(task_id='hent_ressourceforløb_fra_DMSA', bash_command='sleep 10')

    dummy_op2 = BashOperator(task_id='find_relevante_fritagelser', bash_command='sleep 10')

    dummy_op3 = BashOperator(task_id='kombiner_beskæftigelsesindsatser_med_ressourceforløb', bash_command='sleep 10')

    dummy_op4 = BashOperator(task_id='producer_y11iga_fact', bash_command='sleep 10')

    dummy_op5 = BashOperator(task_id='styring_slut', bash_command='sleep 10')

    dummy_op >> dummy_op1 >> dummy_op2 >> dummy_op3 >> dummy_op4 >> dummy_op5
