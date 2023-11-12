from peewee import *

from notification.persistence.base import BaseModel


class Message(BaseModel):
    template_id = BigAutoField()
    title = TextField()
    content = TextField()


Message.create()
