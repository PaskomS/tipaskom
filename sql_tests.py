from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///sqlite.db')  # используя относительный путь
# engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный путь

session = sessionmaker(bind=engine)
Base = declarative_base()
ses = session()


class Post(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    hHi = Column(String)
    lLo = Column(String)


Base.metadata.create_all(engine)
c1 = Post(
    hHi='2',
    lLo='3'
    )
ses.add(c1)
ses.commit()

a = 1

class Asd:
    def __init__(self):
        a = 1
        b = 2
        c = a+b



aaaaa = Asd
