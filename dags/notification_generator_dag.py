import json
from datetime import datetime

from croniter import croniter
from airflow import DAG
from airflow.decorators import task

from notification.commander import SQLCommand
from notification.persistence.articles import Articles
from notification.persistence.base import DB
from notification.persistence.notification import Notification
from notification.persistence.users import Users

with DAG(dag_id="notification_generator",
         start_date=datetime(2022, 1, 1),
         ) as dag:
    @task
    def generate_data():
        DB.drop_tables([Users, Notification, Articles])
        DB.create_tables([Users, Notification, Articles])

        Notification.create(
            schedule='* * * * MON',
            schedule_condition='*',
            message='{"title": "Weekly Newsletter", "content": "오늘은 월요일입니다. {{username}}님, 출근하세요! ^~^"}',
            target="SELECT u.email as target FROM users u JOIN subscribe s ON s.id = n.user_id",
            active=True,
        )

        Notification.create(
            schedule='*',
            schedule_condition='{{article.created_at}} == {{now}}',
            message='{"title": "New Newsletter", "content": "새로운 아티클이 발간되었어요!"}',
            target="SELECT u.email as target FROM users u JOIN subscribe s ON s.id = n.user_id",
            active=True,
        )

        # Notification.create(
        #     schedule='*',
        #     schedule_condition='{{ article.created_at }} <= 2 days',
        #     message='{"title": "What\'s new now!", "content": 2시간 뒤에 {{ content_name }} 이 업로드 될 예정입니다!"}',
        #     target="SELECT u.email as target FROM users u JOIN subscribe s ON s.id = n.user_id",
        #     args=json.dumps(
        #         {"name": "ariticles", "type": "sql", "value": "SELECT a FROM articles a WHERE a.created_at >= NOW()"},
        #         # {"order": 1, "next": "scheduled", "type": "sql", "value": "{{ aricles[*].created_at }}"}
        #     ),
        #     active=True,
        # )

        Users.create(username="sunny", email="sunny@email.com")
        Users.create(username="agustin", email="agustin@email.com")
        Users.create(username="etienne", email="etienne@email.com")
        Users.create(username="tai", email="tai@email.com")

        Articles.create(author=0, content="<html><body>HI!!</body></html>", created_at=datetime.now())
        Articles.create(author=2, content="<html><body>Hello ~!</body></html>", created_at=datetime.now())

        print('Notification : ', Notification.select())
        print('Users : ', Users.select())


    @task
    def make_message():
        """
            make message from template
        """
        args = {}

        def make_messages(template: Notification):
            print('## STEP 2 ##\n\n\n\n\n')
            # ① Get args and then make extra args
            if template.args is not None:
                parsed_args = json.loads(template.args)
                print(parsed_args, "\n\n\n\n")

                if parsed_args['type'] == "sql":
                    args[parsed_args['name']] = SQLCommand().execute(parsed_args['value'])
                else:
                    args[parsed_args['name']] = parsed_args.value

                print('args : ', args)

            # ② Get schedule and judge whether it have to run or not
            schedule_condition = json.loads(template.schedule_condition)


            parsed_schedule = json.loads(template.schedule)
            next_schedule = croniter(parsed_schedule, datetime.now()).get_next(datetime)
            print('parsed_schedule : ', parsed_schedule)
            print('next_schedule : ', next_schedule)

            # ③ Get targets and then make common args

            # ④ Make messages with the args got the above

        print('## STEP 1 ##\n\n\n\n\n')
        # ① Get all active notification template
        templates = Notification.select().where(Notification.active == True)

        print('templates : ', templates)
        for t in templates:
            print(t.args)
            make_messages(t)


    generate_data() >> make_message()
