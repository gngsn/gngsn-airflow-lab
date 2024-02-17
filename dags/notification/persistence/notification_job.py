from notification.persistence.base import BaseModel
from peewee import *


class NotificationJob(BaseModel):
    id = BigIntegerField(primary_key=True)
    notification_id = BigIntegerField()
    status = CharField()
