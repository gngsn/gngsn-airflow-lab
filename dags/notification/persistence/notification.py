from datetime import datetime
from peewee import *

from notification.persistence.base import BaseModel


class Notification(BaseModel):
    id = BigAutoField()  # `primary_key=True` is implied. Event.event_id will be auto-incrementing PK.
    schedule = CharField()
    message = TextField()
    target = JSONField()
    args = JSONField(null=True)
    active = BooleanField(default=False)
    update_at = DateTimeField(default=datetime.now)
