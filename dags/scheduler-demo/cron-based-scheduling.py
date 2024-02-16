import datetime as dt
import os

import requests
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

current_dir = os.getcwd()

dag = DAG(
    dag_id="cron-based-scheduling",
    start_date=dt.datetime(2023, 10, 1),  # 1. DAG 시작 날짜 명시
    schedule_interval="@daily",  # 2. cron-based scheduling
)

# Task 1.
start_flask_server = BashOperator(
    task_id="start_flask_server",
    bash_command=(
        f"cd {current_dir}/scheduler-demo && "
        "flask --app server run "  # 3. API로 부터 이벤트를 fetch하고 저장
    ),
    dag=dag,
)


# Task 2.
def _save_response(output_path):
    """Calculates event statistics."""
    launches = requests.get("http://localhost:5000/events").json()
    print("launches: " + launches)

    f = open(output_path, "a")
    f.write(launches)
    f.close()


# Task 2.
save_response = PythonOperator(
    task_id="calculate_stats",
    python_callable=_save_response,
    op_kwargs={
        "output_path": f"{current_dir}/data/response.csv",
    },
    dag=dag,
)


start_flask_server >> save_response  # 6. 순서 명시
