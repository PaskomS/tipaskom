import datetime
import sqlalchemy.schema
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, schema, Float, UniqueConstraint, cast, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///control/db/hystory_candles.db')

session = sessionmaker(bind=engine)
Base = declarative_base()
ses = session()


"""
Запрос истории.

На входе инструмент figi, период, размерность свечи.
История сохраняется в файл.
"""


def get_last_date(table: sqlalchemy.table):
    """Возвращает последнюю дату котировки из таблицы,
    либо, если таблица пустая - возращает дату, начиная с которой будет запрашиваться история котировок
    :param table:
    :return: datetime"""
    exists = ses.query(table.datetime).all()  # is not None
    if len(exists) != 0:
        start_date = ses.query(table.datetime).order_by()[-1][0]
        print("дата из таблицы ", start_date)
    else:
        utc_now = datetime.datetime.utcnow()
        start_date = utc_now - datetime.timedelta(days=1200)  # 5 лет, 1825 дней  3,2 года 1200 дней, вроде не вылетает по ощибке количества запросов
        #start_date = datetime.datetime.strptime('2018-03-06 00:00:01', '%Y-%m-%d %H:%M:%S')
        print("таблица пустая days=1200 ", start_date)
    return start_date

    # https://ploshadka.net/sqlalchemy-primery-zaprosov-orm/#h2-2


def update(figi):
    start_date = get_last_date(figi.table)
    #candl = figi.cur_account.account.get_market_candles(figi.figi, "2018-03-24T00:00:00+00:00", "2018-03-25T00:00:00+00:00", figi.cur_account.tinvest.CandleResolution.hour)
    #start_date = datetime.datetime.strptime('2010-01-01 00:00:01', '%Y-%m-%d %H:%M:%S')  # дата начала для записи котировок, может быть либо продолжением ранее записанного либо заданным вручную
    stop_date = datetime.datetime.utcnow()  # текущая дата UTC, для окончания периода для записи исторических котировок
    total_write_days = stop_date - start_date  # timedelta подсчет разницы, между датами начала и окончания периода
    period_in_days = total_write_days.days  # timedelta разница в ДНЯХ, дробное
    request_period = 7  # ограничение на порцию запрашиваемой информации, тут по X дней
    request_number_total = period_in_days / request_period  # считаем сколько раз подряд придется обращаться к брокеру за котировками
    first_date = start_date + datetime.timedelta(seconds=1)  # добавляем 1 секунду для даты начала новой порции
    second_date = first_date + datetime.timedelta(days=request_period)  # начальная инициализация - дата начала + лимитный период

    for x in range(int(request_number_total)):  # цикл запроса порций нотировок, повторить N раз
        str_first_date = datetime.datetime.strftime(first_date, '%Y-%m-%dT%H:%M:%S+00:00')  #конвертация даты в строку для запроса истории котировок
        str_second_date = datetime.datetime.strftime(second_date, '%Y-%m-%dT%H:%M:%S+00:00')  #конвертация даты в строку для запроса истории котировок

        print(str_first_date)
        print(str_second_date)
        print('--запрос')
        candles_requested = get_candles(figi, str_first_date, str_second_date)  # запрос first_date -- second_date
        candles_requested_count = len(candles_requested.payload.candles)

        if candles_requested_count != 0:
            write_candles_to_base(figi, candles_requested)  # если есть данные, записать их в базу, порцией

        first_date = second_date + datetime.timedelta(seconds=1)  # добавляем 1 секунду для даты начала новой порции
        second_date = first_date + datetime.timedelta(days=request_period)  # вычисляем дату окончания очередной порции

    # последняя порция, дозаписываем остаток
    str_first_date = datetime.datetime.strftime(first_date, '%Y-%m-%dT%H:%M:%S+00:00')  #конвертация даты в строку для запроса истории котировок
    str_second_date = datetime.datetime.strftime(datetime.datetime.utcnow(), '%Y-%m-%dT%H:%M:%S+00:00')  #конвертация даты в строку для запроса истории котировок
    print(str_first_date)
    print(str_second_date)
    print('--запрос')
    candles_requested = get_candles(figi, str_first_date, str_second_date)  # запрос first_date -- second_date
    candles_requested_count = len(candles_requested.payload.candles)
    if candles_requested_count != 0:
        write_candles_to_base(figi, candles_requested)  # если есть данные, записать их в базу, порцией



def write_candles_to_base(figi, candles_requested):

    #fff = get_candles(figi, str_first_date, second_date)
    candles_requested_count = len(candles_requested.payload.candles)
    for candle in candles_requested.payload.candles:
        tmp = figi.table(
            datetime=candle.time.replace(tzinfo=None),
            cl=candle.c,
            hi=candle.h,
            lo=candle.l,
            op=candle.o,
            vol=candle.v
            )
        ses.add(tmp)
    ses.commit()


def get_candles(figi, str_first_date, second_date):
    # получаем историческую информацию по котировкам
    # добавить контроль времени, пример: https://digitology.tech/posts/funktsii-taiminga-python-tri-sposoba-kontrolirovat-vash-kod/
    candl = figi.cur_account.account.get_market_candles(figi.figi, str_first_date, second_date, figi.cur_account.tinvest.CandleResolution.hour)
    return candl

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


def create_table(tbl_name: str):
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
    return Post

# class gethystory:
#     def __init__(self, *args: object):
#         self.a = args
#         f1 = datetime.now()
#         curAcc = self.a[0]
#         curFigi = self.a[1]
#         ff = tinvest.Candles.candles(self.a[0], "2021-09-24T15:00:00+04:00", "2021-09-24T15:10:00+04:00", tinvest.CandleResolution.hour)
#         return ff
#         pass
#     def getstock(self, *args):
#         #a = tinvest.Candles(self.getstock())
#         a = args[0]
#         pass
#         return (a)

