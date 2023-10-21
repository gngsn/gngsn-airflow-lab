from datetime import datetime

from peewee import *

db = SqliteDatabase('people.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Notification(BaseModel):
    __tablename__ = "notification"

    id = BigAutoField() #  `primary_key=True` is implied. Event.event_id will be auto-incrementing PK.
    schedule = TextField()
    message = TextField()
    target = TextField()
    update_at = TextField(default=datetime.now)


Notification.create(
    schedule="",
    message="",
    target="",
    update_at="",
)