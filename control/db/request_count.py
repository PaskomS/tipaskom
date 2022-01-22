import datetime

time_limit_sec = 300  # время в секундах, в течении которого разрешается сделать request_limit запросов
request_limit = 500  # общее количество запросов, которые можно совершить за time_limit_sec секунд

class RequestInfo:
    """Класс для получения и записи параметров запросов на сервер брокера с целью предотвращения
    превышения лимитов по количеству запросов за единицу времени.
    :param allow_write: bool - если True то при обращении к классу считать что запрос выполнился,
    соответсвенно автоматически прибавлять счетчик запросов.

    Счетчик запросов накапливается в течении 5 минут, выдается по запросу.
    Если от последней метки времени прошло больше 5 минут, метка времени обновляется, счетчик обнуляется.
    """

    def __init__(self):
        self.last_timestamp = None
        self.request_count = None
        self.elapsed_time_sec = None
        self.read_info_in_file()


    def allow_to_request(self):
        utc_now = datetime.datetime.utcnow()  # получить текущее время
        elapsed_time_delta = utc_now - self.last_timestamp  # timedelta подсчет разницы, между датами начала и окончания
        self.elapsed_time_sec = elapsed_time_delta.seconds  # прошло N секунд, timedelta разница в SECONDS (300 секунд в 5 минутах)
        if self.elapsed_time_sec > time_limit_sec:  # разрешить запрос - т. к. после крайнего запроса к броокеру прошло достаточно времени, обновляем временную метку и сбрасываем счетчик запросов
            # записать новую дату и счетчик 1
            self.last_timestamp = utc_now
            self.request_count = 1
            str_utc_now = datetime.datetime.strftime(utc_now, '%Y-%m-%d %H:%M:%S')  # конвертация даты в строку
            self.write_info_to_file(str_utc_now, 1)
            return True
        elif self.request_count < request_limit:  # разрешить запрос - т. к. в течении отведенного времени лимит запросов еще не исчерпан
            # прибавить счетчик
            self.request_count += 1
            return True
        else:  # ЗАПРЕТИТЬ, т.к. не прошло X минут и достигнут лимит запросов
            # после получения False, запрашивающая сторона может обратиться к переменной класса elapsed_time_sec, и самостоятельно реализовать ожидание на оставшуюся часть времени
            return False

    def read_info_in_file(self):
        """Получить из файла данные по последним сетевым запросам
        обновляет переменные класса
        last_timestamp - дата и время из файла, конвертирует в datetime
        request_count - количество запросов из файла, 4 знака, INT
        """

        with open('request_count.info', "r") as fp:
            fp.seek(0, 0)
            point_time_in_file = fp.read(19)  # прочитать дату и время из файла (первые 19 символов)

            fp.seek(24, 0)
            self.request_count = int(fp.read(4))  # прочитать количество запросов из файла (4 символа с позиции 24)

        self.last_timestamp = datetime.datetime.strptime(point_time_in_file,
                                                    '%Y-%m-%d %H:%M:%S')  # конвертация строки из файла в дату

    def write_info_to_file(self, point_time: str, count: int):
        with open('request_count.info', "r+") as fp:
            # Moving the file handle to the end of the file
            fp.seek(0, 0)
            fp.write(point_time)

            fp.seek(24, 0)
            tmp = '{:04}'.format(count)
            fp.write(tmp)


req_to_broker = RequestInfo()

for x in range(600):
    bbb = req_to_broker.allow_to_request()
    if x > 498:
        a = 1


bbb = req_to_broker.allow_to_request()
bbb = req_to_broker.allow_to_request()
bbb = req_to_broker.allow_to_request()
bbb = req_to_broker.allow_to_request()
a=1

def get_in_file_request_info():
    """Получить из файла данные по последним сетевым запросам
    :return elapsed_time_sec - INT время в секундах, прошедшее до настоящего
    :return req_count_in_file - INT набежавшее количество запросов, до 4х знаков
    """

    with open('request_count.info', "r") as fp:
        fp.seek(0, 0)
        point_time_in_file = fp.read(19)  # прочитать дату и время из файла (первые 19 символов)

        fp.seek(24, 0)
        req_count_in_file = int(fp.read(4))  # прочитать количество запросов из файла (4 символа с позиции 24)

    point_time_in_file = datetime.datetime.strptime(point_time_in_file,
                                                    '%Y-%m-%d %H:%M:%S')  # конвертация строки из файла в дату
    utc_now = datetime.datetime.utcnow()  # получить текущее время
    elapsed_time_delta = utc_now - point_time_in_file  # timedelta подсчет разницы, между датами начала и окончания
    elapsed_time_sec = elapsed_time_delta.seconds  # timedelta разница в SECONDS 300 секунд в 5 минутах
    return elapsed_time_sec, req_count_in_file

#get = get_in_file_request_info()
#point_time_in_file = get[0]
#request_count = get[1]

def write_in_file_request_info(request_tick):
    with open(r'../control/db/request_count.info', "r+") as fp:
        # Moving the file handle to the end of the file
        fp.seek(0, 0)
        # fp.write(point_time)
        atell = fp.tell()

        fp.seek(24, 0)
        fp.write("1005")

        fp.seek(0, 0)
        point_time_in_file = fp.read(19)  # прочитать дату и время из файла (первые 19 символов)

        fp.seek(24, 0)
        req_count_in_file = fp.read(4)  # прочитать количество запросов из файла (4 символа с позиции 24)

    point_time_in_file = datetime.datetime.strptime(point_time_in_file,
                                                    '%Y-%m-%d %H:%M:%S')  # конвертация строки из файла в дату
    utc_now = datetime.datetime.utcnow()
    elapsed_time = utc_now - point_time_in_file  # timedelta подсчет разницы, между датами начала и окончания
    elapsed_time_min = elapsed_time.seconds  # timedelta разница в SECONDS 300 секунд в 5 минутах

    now_time = datetime.datetime.now().time()
    # elapsed_time = now_time - datetime.timedelta(time.tiiiime_point)


a=1

