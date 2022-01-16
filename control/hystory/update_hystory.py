import sqlalchemy.schema
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, schema, Float, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///control/db/hystory.db')  # используя относительный путь
# engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный путь

session = sessionmaker(bind=engine)
Base = declarative_base()
ses = session()


"""
Запрос истории.

На входе инструмент figi, период, размерность свечи.
История сохраняется в файл.
"""


def get_last_date(Figi, acc):
    table_name = Figi.figi
    table = create_table(table_name)
    aaa = ses.query(table).all()
    ...


def update(Figi, acc):
    #get_last_date(Figi, acc)
    # задается имя таблицы, вызывается алгоритм получения исторической информации по котировкам
    table_name = Figi.figi
    table = create_table(table_name)
    fff = get_candles(Figi.figi, acc)
    for bbb in range(7):
        table.datetime = fff.payload.candles[bbb].time.replace(tzinfo=None)
        table.cl = fff.payload.candles[bbb].c
        table.hi = fff.payload.candles[bbb].h
        table.lo = fff.payload.candles[bbb].l
        table.op = fff.payload.candles[bbb].o
        table.vol = fff.payload.candles[bbb].v
        try:
            ses.add(table)
            ses.commit()
        #Дата уникальная, при попытке записать уже имеющуюся дату транзакцию пропускать
        except Exception as exception:
            if exception.__class__.__name__ == 'IntegrityError':
                ses.rollback()
        else:
            ses.commit()
        ...
    aaa = ses.query(table).all()
    ...

def get_candles(figi, acc):
    # получаем историческую информацию по котировкам
    candl = acc.account.get_market_candles(figi, "2022-01-06T00:00:00+00:00", "2022-01-06T23:00:00+00:00", acc.tinvest.CandleResolution.min1)
    return candl
    ...
    #
    # Интервал свечи и допустимый промежуток запроса:
    # 1 min[1 minute, 1 day] 2 min[2 minutes, 1 day] 3 min[3 minutes, 1 day] 5 min[5 minutes, 1 day] 10 min[10 minutes, 1 day] 15 min[15 minutes, 1 day] 30 min[30 minutes, 1 day]
    # hour[1 hour, 7 days] day[1 day, 1 year] week[7 days, 2 years] month[1 month, 10 years] Enum: Array[11]
    # o * number($double)
    # c * number($double)
    # h * number($double)
    # l * number($double)
    # v * integer($int32)
    # time * string($date - time)
    # example: 2019-08-19T18:38:33+03:00


def create_table(tbl_name):

    class Post(Base):
        __tablename__ = tbl_name
        id = Column(Integer, primary_key=True)
        datetime = Column(DateTime, unique=True)
        cl = Column(Float)
        hi = Column(Float)
        lo = Column(Float)
        op = Column(Float)
        vol = Column(Integer)

    Base.metadata.create_all(engine)
    return Post()


a = 1





# class gethystory:
#     def __init__(self, *args: object):
#         self.a = args
#         f1 = datetime.now()
#         curAcc = self.a[0]
#         curFigi = self.a[1]
# #        ff = tinvest.Candles.candles(self.a[0], "2021-09-24T15:00:00+04:00", "2021-09-24T15:10:00+04:00", tinvest.CandleResolution.day)
# #        return ff
#         pass
#     def getstock(self, *args):
#         #a = tinvest.Candles(self.getstock())
#         a = args[0]
#         pass
# #       return (a)

