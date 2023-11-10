import json

import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="template_test",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@hourly",
)

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
    dag=dag,
)

dag = DAG(
    dag_id="print_context",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)


def _print_context(**kwargs):
    print("\n\n\n\n\nprint:: ", kwargs['dag'])


print_context = PythonOperator(
    task_id="print_context",
    python_callable=_print_context,
    dag=dag,
)

# Result
"""
{
  'conf': <airflow.configuration.AirflowConfigParser object at 0x104f75550>, 
  'dag': <DAG: print_context>, 
  'dag_run': <DagRun print_context @ 2023-10-14T15:00:18.710593+00:00: manual__2023-10-14T15:00:18.710593+00:00, state:running, queued_at: None. externally triggered: False>, 
  'data_interval_end': DateTime(2023, 10, 14, 0, 0, 0, tzinfo=Timezone('UTC')),
  'data_interval_start': DateTime(2023, 10, 13, 0, 0, 0, tzinfo=Timezone('UTC')), 
  'ds': '2023-10-14', 
  'ds_nodash': '20231014', 
  'execution_date': <Proxy at 0x1253851c0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>,
  'execution_date', DateTime(2023, 10, 14, 15, 0, 18, 710593, tzinfo=Timezone('UTC')))>,
  'expanded_ti_count': None,
  'inlets': [],
  'logical_date': DateTime(2023, 10, 14, 15, 0, 18, 710593, tzinfo=Timezone('UTC')),
  'macros': <module 'airflow.macros' from '/Users/gyeongsun/git/gngsn-airflow-lab/.venv/lib/python3.9/site-packages/airflow/macros/__init__.py'>,
  'next_ds': <Proxy at 0x1253bb880 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'next_ds',  '2023-10-14')>,
  'next_ds_nodash': <Proxy at 0x1253bb940 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'next_ds_nodash', '20231014')>,
  'next_execution_date': <Proxy at 0x1253bb9c0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>,
  'next_execution_date', DateTime(2023, 10, 14, 0, 0, 0, tzinfo=Timezone('UTC')))>,
  'outlets': [],
  'params': {},
  'prev_data_interval_start_success': None,
  'prev_data_interval_end_success': None,
  'prev_ds': <Proxy at 0x1253bb1c0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'prev_ds', '2023-10-14')>,
  'prev_ds_nodash': <Proxy at 0x1253a5600 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'prev_ds_nodash', '20231014')>,
  'prev_execution_date': <Proxy at 0x1253a5440 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'prev_execution_date', DateTime(2023, 10, 14, 0, 0, 0, tzinfo=Timezone('UTC')))>,
  'prev_execution_date_success': <Proxy at 0x1253c00c0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'prev_execution_date_success', None)>,
  'prev_start_date_success': None,
  'run_id': 'manual__2023-10-14T15:00:18.710593+00:00',
  'task': <Task(PythonOperator): print_context>,
  'task_instance': <TaskInstance: print_context.print_context manual__2023-10-14T15:00:18.710593+00:00 [None]>,
  'task_instance_key_str': 'print_context__print_context__20231014',
  'test_mode': False,
  'ti': <TaskInstance: print_context.print_context manual__2023-10-14T15:00:18.710593+00:00 [None]>,
  'tomorrow_ds': <Proxy at 0x1253c0200 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'tomorrow_ds', '2023-10-15')>,
  'tomorrow_ds_nodash': <Proxy at 0x1253c02c0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'tomorrow_ds_nodash', '20231015')>,
  'triggering_dataset_events': <Proxy at 0x12532ab80 with factory <function TaskInstance.get_template_context.<locals>.get_triggering_events at 0x125328af0>>,
  'ts': '2023-10-14T15:00:18.710593+00:00',
  'ts_nodash': '20231014T150018',
  'ts_nodash_with_tz': '20231014T150018.710593+0000',
  'var': {'json': None, 'value': None}, 
  'conn': None,
  'yesterday_ds': <Proxy at 0x1253c0340 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'yesterday_ds', '2023-10-13')>,
  'yesterday_ds_nodash': <Proxy at 0x1253c0580 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0x1253823a0>, 'yesterday_ds_nodash', '20231013')>, 'templates_dict': None
}
"""
