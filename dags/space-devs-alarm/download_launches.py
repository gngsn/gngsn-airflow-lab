import pathlib

import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


# 1. DAG: DAG 정의
dag = DAG(
    dag_id="download_rocket_launches",  # Airflow UI 에 보여질 DAG 이름
    start_date=airflow.utils.dates.days_ago(14),  # Workflow 가 처음 실행될 일시
    schedule_interval=None,
)


def _get_pictures():
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)

    launches = requests.get('https://ll.thespacedevs.com/2.0.0/launch/upcoming').json()
    image_urls = [launch["image"] for launch in launches["results"]]

    for image_url in image_urls:
        try:
            response = requests.get(image_url)
            image_filename = image_url.split("/")[-1]
            target_file = f"/tmp/images/{image_filename}"
            with open(target_file, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {image_url} to {target_file}")
        except requests_exceptions.MissingSchema:
            print(f"{image_url} appears to be an invalid URL.")
        except requests_exceptions.ConnectionError:
            print(f"Could not connect to {image_url}.")


# 2. PythonOperator: get_pictures
get_pictures = PythonOperator(
    task_id="get_pictures",
    python_callable=_get_pictures,
    dag=dag,
)

# 3. BashOperator: notify
notify = BashOperator(
    task_id="notify",
    bash_command='echo "There are now $(ls /tmp/images/ | wc -l) images."',
    dag=dag,
)

get_pictures >> notify
