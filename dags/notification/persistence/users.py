from datetime import datetime
from peewee import *

from notification.persistence.base import BaseModel


class Users(BaseModel):
    id = BigAutoField()  # `primary_key=True` is implied. Event.event_id will be auto-incrementing PK.
    username = TextField()
    email = TextField()
    create_at = DateTimeField(default=datetime.now)
