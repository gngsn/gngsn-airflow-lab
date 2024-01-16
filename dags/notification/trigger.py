import airflow.utils.dates
from airflow.models.dag import dag
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


@dag(
    dag_id="notification_batch",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@hourly",
)
def notification_batch():
    get_data = BashOperator(
        task_id="get_data",
        bash_command=(
            "curl -o ${AIRFLOW_HOME}/.tmp/wikipageviews.gz "
            "https://dumps.wikimedia.org/other/pageviews/"
            "{{ execution_date.year }}/"
            "{{ execution_date.year }}-"
            "{{ '{:02}'.format(execution_date.month) }}/"
            "pageviews-{{ execution_date.year }}"
            "{{ '{:02}'.format(execution_date.month) }}"
            "{{ '{:02}'.format(execution_date.day) }}-"
            "{{ '{:02}'.format(execution_date.hour) }}0000.gz"
        ),
    )

    get_data


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
