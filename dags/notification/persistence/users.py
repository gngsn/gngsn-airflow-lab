from datetime import datetime

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine.url import URL

# from dags.notification.persistence.base import Base, session

from airflow import DAG
from airflow.decorators import task

Base = declarative_base()

# DB = {
#     'drivername': 'postgresql',
#     'host': '127.0.0.1',
#     'port': '5432',
#     'username': 'postgres',
#     'password': 'postgres',
#     'database': 'ums',
# }
#
# engine = create_engine(URL(**DB), encoding='utf8')
# dialect+driver://username:password@host:port/database
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/ums")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )

# 정의된 테이블 생성
Base.metadata.create_all(engine)

def run():
    print("Hello World!")

    Session = sessionmaker(bind=engine)
    session = Session()


    ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")

    session.add(ed_user)
    session.add_all(
        [
            User(name="wendy", fullname="Wendy Williams", nickname="windy"),
            User(name="mary", fullname="Mary Contrary", nickname="mary"),
            User(name="fred", fullname="Fred Flintstone", nickname="freddy"),
            User(name="ed", fullname="Fred Flintstone", nickname="freddy"),
        ]
    )

    our_user = (
         session.query(User).filter_by(name="ed").all()
    )

    print(our_user)
    print(ed_user is our_user)

    session.close()

# airflow dags test "persistence"
with DAG(dag_id="persistence",
         start_date=datetime(2022, 1, 1),
         schedule="0 0 * * *") as dag:

    @task()
    def taskk():
        run()

    taskk()
