from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print('Verifying Git Sync!')

with DAG(dag_id="git_sync",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    
    task1 = PythonOperator(
            task_id="git_sync_task",
            python_callable=helloWorld)

task1
