import airflow.utils.dates
import logging
import pendulum
from airflow.decorators import task
from airflow.models.dag import dag


@dag(
    dag_id="notification_batch",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@hourly",
)
def notification_batch_dag():
    @task
    def start_batch(**context):
        # run_id = context
        logging.info(f"start {context['dag_run'].dag_id}")
        return f"{context['dag_run'].dag_id}-{pendulum.now().to_iso8601_string()}"

    @task
    def generator():
        f = open("/Users/gyeongsun/git/gngsn-airflow-lab/dags/notification/message_mock.json", "r")
        print(f.read())

        return f.read()

    @task
    def scheduler(f):
        print(f)

    @task
    def end_batch(exec_id):
        logging.info(f"end ${exec_id}")

    execution_id = start_batch()

    scheduler(generator())

    end_batch(execution_id)


notification_batch_dag()
