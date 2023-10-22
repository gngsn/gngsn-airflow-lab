from datetime import datetime
from peewee import *

from notification.persistence.base import BaseModel


class Notification(BaseModel):
    id = BigAutoField()  # `primary_key=True` is implied. Event.event_id will be auto-incrementing PK.
    schedule = TextField()
    message = TextField()
    target = TextField()
    args = TextField(null=True)
    update_at = DateTimeField(default=datetime.now)
