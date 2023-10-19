from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

# dialect+driver://username:password@host:port/database
engine = create_engine("postgresql://postgres:postgres@localhost/ums")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )

# 정의된 테이블 생성
Base.metadata.create_all(engine)

def main():
    print("Hello World!")

    ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(ed_user)

    session.add_all(
        [
            User(name="wendy", fullname="Wendy Williams", nickname="windy"),
            User(name="mary", fullname="Mary Contrary", nickname="mary"),
            User(name="fred", fullname="Fred Flintstone", nickname="freddy"),
            User(name="ed", fullname="Fred Flintstone", nickname="freddy"),
        ]
    )

    our_user = (
         session.query(User).filter_by(name="ed").all()
    )

    print(our_user)
    print(ed_user is our_user)

    session.delete()
    session.close()


if __name__ == "__main__":
    main()