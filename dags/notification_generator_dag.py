import json
from datetime import datetime

from airflow import DAG
from airflow.decorators import task

from notification.persistence.base import DB
from notification.persistence.notification import Notification
from notification.persistence.users import Users

with DAG(dag_id="notification_generator",
         start_date=datetime(2022, 1, 1),
         ) as dag:
    @task
    def generate_data():
        DB.drop_tables([Users, Notification])
        DB.create_tables([Users, Notification])

        Notification.create(
            schedule='* * * * MON',
            message='{"title": "Weekly Newsletter", "content": "오늘은 월요일입니다. 출근하세요! ^~^"}',
            target="SELECT u.email as target FROM users u JOIN subscribe s ON s.id = n.user_id",
            args=None,
        )

        Notification.create(
            schedule='{{ next }}',
            message='{"title": "What\'s new today!", "content": "너무 졸리당"}',
            target="SELECT u.email as target FROM users u JOIN subscribe s ON s.id = n.user_id",
            args=json.dumps({"next": {"sql": "SELECT a.create_at FROM articles a WHERE "}})
        )

        Users.create(username="sunny", email="sunny@email.com")
        Users.create(username="agustin", email="agustin@email.com")
        Users.create(username="etienne", email="etienne@email.com")
        Users.create(username="tai", email="tai@email.com")

        print('Notification : ', Notification.select())
        print('Users : ', Users.select())


    generate_data()
