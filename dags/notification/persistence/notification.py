from datetime import datetime
from peewee import *

from notification.persistence.base import BaseModel


class Notification(BaseModel):
    id = BigAutoField()  # `primary_key=True` is implied. Event.event_id will be auto-incrementing PK.
    schedule = TextField()  # can return multiple
    message = TextField()
    target = TextField()
    args = TextField(null=True)
    active = BooleanField(default=False)
    update_at = DateTimeField(default=datetime.now)
