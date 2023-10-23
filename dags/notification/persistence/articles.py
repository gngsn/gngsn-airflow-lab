from datetime import datetime
from peewee import *

from notification.persistence.base import BaseModel


class Articles(BaseModel):
    id = BigAutoField()
    author = BigIntegerField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)
