from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
# Making Chagnes for git-sync

def helloWorld():
    print('Hello World')

with DAG(dag_id="test_add",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    
    task1 = PythonOperator(
            task_id="first_task",
            python_callable=helloWorld)

task1
