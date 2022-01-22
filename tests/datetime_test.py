import datetime
from zoneinfo import ZoneInfo

d1 = datetime.datetime.strptime('2018-03-07 18:00:00', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2021-08-13 15:00:00', '%Y-%m-%d %H:%M:%S')
total_write_days = d2 - d1  # timedelta подсчет разницы, между датами начала и окончания периода
period_in_days = total_write_days.days  # timedelta разница в ДНЯХ, дробное


utc_now = datetime.datetime.utcnow()
start_date = utc_now - datetime.timedelta(days=1825)  # 5 лет, 1825 дней

start_date = datetime.datetime.strptime('2010-01-01 00:00:01', '%Y-%m-%d %H:%M:%S')  # дата начала для записи котировок, может быть либо продолжением ранее записанного либо заданным вручную
stop_date = datetime.datetime.utcnow()  # текущая дата UTC, для окончания периода для записи исторических котировок
total_write_days = stop_date - start_date  # timedelta подсчет разницы, между датами начала и окончания периода
period_in_days = total_write_days.days  # timedelta разница в ДНЯХ, дробное
request_period = 7  # ограничение на порцию запрашиваемой информации, тут по X дней
request_number_total = period_in_days/request_period  # считаем сколько раз подряд придется обращаться к брокеру за котировками

first_date = start_date  # начальная инициализация
second_date = first_date + datetime.timedelta(days=request_period)  # начальная инициализация - дата начала + лимитный период
for x in range(int(request_number_total)):  # цикл запроса порций нотировок, повторить N раз
    str_first_date = datetime.datetime.strftime(first_date, '%Y-%m-%dT%H:%M:%S+00:00')
    str_second_date = datetime.datetime.strftime(second_date, '%Y-%m-%dT%H:%M:%S+00:00')
    print(str_first_date)
    print(str_second_date)
    print('--запрос')
    # запрос first_date -- second_date
    first_date = second_date + datetime.timedelta(seconds=1)  # добавляем 1 секунду для даты начала новой порции
    second_date = first_date + datetime.timedelta(days=request_period)  # вычисляем дату окончания очередной порции


str_first_date = datetime.datetime.strftime(first_date, '%Y-%m-%dT%H:%M:%S+00:00')
str_second_date = datetime.datetime.strftime(datetime.datetime.utcnow(), '%Y-%m-%dT%H:%M:%S+00:00')
# последняя порция, дозаписываем остаток
print(str_first_date)
print(str_second_date)
print('--запрос')

aaa = datetime.datetime.utcnow()
sss = datetime.time(1, 0, 0)  # задать время
bbb = aaa + datetime.timedelta(minutes=133)  # прибавить время

date_str = 'Fri, 24 Apr 2021 16:22:54 +0000'
format = '%a, %d %b %Y %H:%M:%S +0000'
ddd = datetime.datetime.strptime(date_str, format)

date_str = '2021 03 06 16:22:54'
format = '%Y %m %d %H:%M:%S'
ddddf = datetime.datetime.strptime(date_str, format)

date_str = '2021 03 06 16:22:54'
format = '%Y %m %d %H:%M:%S'
dddd = datetime.datetime.strptime('2021 03 06 16:22:54', '%Y %m %d %H:%M:%S')

#fff = datetime.datetime.strptime('2022-01-06 00:00:00', '%y-%m-%d %H:%M:%S +0000')

...

# Конвертация строки в объект
# datetime_string = "11/17/20 15:02:34"
# datetime_obj = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')
# "# создадим даты как строки
# ds1 = 'Friday, November 17, 2020'
# ds2 = '11/17/20'
# ds3 = '11-17-2020'
# "# Конвертируем строки в объекты datetime и сохраним
# dt1 = datetime.strptime(ds1, '%A, %B %d, %Y')
# dt2 = datetime.strptime(ds2, '%m/%d/%y')
# dt3 = datetime.strptime(ds3, '%m-%d-%Y')
#
#
# Как конвертировать объект datetime в строку
# current_date = datetime.datetime.now()
# current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')
#
#
# Всегда храните даты в UTC. Вот примеры:
#
# import datetime
# import pytz
# time_now = datetime.datetime.now(pytz.utc)
# print(time_now) Результат для этого кода — 2020-11-14 14:38:46.462397+00:00, хотя локальное время может быть, например, таким 2020-11-14 16:38:46.462397+00:00.
#
# А уже при демонстрации даты пользователю стоит использовать метод localize с местными настройками:
# import datetime
# import pytz
# now = datetime.datetime.today()
# now_utc = pytz.utc.localize(now) Вернет текущее локальное время — 2020-11-14 16:42:38.228528+00:00.
#

# Таблица форматов:
#
# Символ	Описание	Пример
# %a	День недели, короткий вариант	Wed
# %A	Будний день, полный вариант	Wednesday
# %w	День недели числом 0-6, 0 — воскресенье	3
# %d	День месяца 01-31	31
# %b	Название месяца, короткий вариант	Dec
# %B	Название месяца, полное название	December
# %m	Месяц числом 01-12	12
# %y	Год, короткий вариант, без века	18
# %Y	Год, полный вариант	2018
# %H	Час 00-23	17
# %I	Час 00-12	05
# %p	AM/PM	PM
# %M	Минута 00-59	41
# %S	Секунда 00-59	08
# %f	Микросекунда 000000-999999	548513
# %z	Разница UTC	+0100
# %Z	Часовой пояс	CST
# %j	День в году 001-366	365
# %U	Неделя числом в году, Воскресенье первый день недели, 00-53	52
# %W	Неделя числом в году, Понедельник первый день недели, 00-53	52
# %c	Локальная версия даты и времени	Mon Dec 31 17:41:00 2018
# %x	Локальная версия даты	12/31/18
# %X	Локальная версия времени	17:41:00
# %%	Символ “%”	%


