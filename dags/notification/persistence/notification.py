from sqlalchemy import Column, Integer, String, JSON, DateTime

from dags.notification.persistence.base import Base


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True)
    schedule = Column(String)
    body = Column(JSON)
    target = Column(String)
    update_at = Column(DateTime)
