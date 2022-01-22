from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///control/db/hystory_candles.db')  # используя относительный путь
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
c0 = Post()
c0.lLo = 2
Post.lLo = 2

c1 = Post(
    hHi='44',
    lLo='55'
    )
ses.add(c1)
c1 = Post(
    hHi='66',
    lLo='77'
    )
ses.add(c1)
ses.commit()
...

