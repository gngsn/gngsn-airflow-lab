from notification.persistence.base import BaseModel


class NotificationJob(BaseModel):
    id = BigIntegerField(primary_key=True)
    notification_id = BigIntegerField()
    status = CharField()
