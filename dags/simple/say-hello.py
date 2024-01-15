from datetime import datetime

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


# ① A DAG represents a workflow, a collection of tasks
@dag(start_date=datetime(2022, 1, 1), schedule="0 0 * * *")
def demo():
    # ② Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # ③ Set dependencies between tasks
    hello >> airflow()
