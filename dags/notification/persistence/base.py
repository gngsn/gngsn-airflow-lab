from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
# dialect+driver://username:password@host:port/database
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/ums?charset=utf8mb4")

Session = sessionmaker(bind=engine)
session = Session()

# 정의된 테이블 생성
Base.metadata.create_all(engine)

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
