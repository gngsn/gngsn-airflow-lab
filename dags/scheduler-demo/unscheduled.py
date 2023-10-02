import datetime as dt
import os
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

current_dir=os.getcwd()

dag = DAG(
    dag_id="unscheduled-demo",
    start_date=dt.datetime(2023, 10, 1),   # 1. DAG 시작 날짜 명시
    schedule_interval=None,                                # 2. unscheduled 임을 명시적으로 표시
)

fetch_events = BashOperator(
    task_id="fetch_events",
    bash_command=(
        f"mkdir -p {current_dir}/data && "
        f"curl -o {current_dir}/data/events.json "
        "http://localhost:5000/events"                     # 3. API로 부터 이벤트를 fetch하고 저장
    ),
    dag=dag,
)


def _calculate_stats(input_path, output_path):
    """Calculates event statistics."""
    print("input_path: " + input_path)
    events = pd.read_json(input_path, orient='index')                      # 4.
    stats = events.groupby(["date", "user"]).size().reset_index()  # 4. 이벤트를 로드하고 필요한 통계 계산
    print(stats)
    Path(output_path).parent.mkdir(exist_ok=True)          # 5.
    stats.to_csv(output_path)                 # 5. 출력 디렉토리가 존재하는지 확인하고 CSV로 결과 작성


calculate_stats = PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    op_kwargs={
        "input_path": f"{current_dir}/data/events.json",
        "output_path": f"{current_dir}/data/stats.csv",
    },
    dag=dag,
)


fetch_events >> calculate_stats                             # 6. 순서 명시
