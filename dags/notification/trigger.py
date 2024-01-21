import airflow.utils.dates
from airflow.models.dag import dag
from airflow.operators.python import PythonOperator


@dag(
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)
def print_context():
    def _print_context(**kwargs):
        print("\n\n\n\n\nprint:: ", kwargs['dag'])

    do = PythonOperator(
        task_id="print_context",
        python_callable=_print_context,
    )

    do


print_context()
