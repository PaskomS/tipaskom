import datetime
utc_now = datetime.datetime.utcnow()
str_utc_now = datetime.datetime.strftime(utc_now, '%Y-%m-%d %H:%M:%S')  #конвертация даты в строку

point_time = str_utc_now

with open(r'../control/db/request_count.info', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 0)
    #fp.write(point_time)
    atell = fp.tell()

    fp.seek(24, 0)
    fp.write("1005")

    fp.seek(0, 0)
    point_time_in_file = fp.read(19)  # прочитать дату и время из файла (первые 19 символов)

    fp.seek(24, 0)
    req_count_in_file = fp.read(4)  # прочитать количество запросов из файла (4 символа с позиции 24)

point_time_in_file = datetime.datetime.strptime(point_time_in_file, '%Y-%m-%d %H:%M:%S')  # конвертация строки из файла в дату
utc_now = datetime.datetime.utcnow()
elapsed_time = utc_now - point_time_in_file  # timedelta подсчет разницы, между датами начала и окончания
elapsed_time_min = elapsed_time.seconds  # timedelta разница в SECONDS 300 секунд в 5 минутах


now_time = datetime.datetime.now().time()
#elapsed_time = now_time - datetime.timedelta(time.tiiiime_point)

