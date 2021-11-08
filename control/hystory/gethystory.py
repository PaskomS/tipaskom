import tinvest as tinvest
from datetime import datetime, timedelta
"""
Запрос истории.

На входе инструмент figi, период, размерность свечи.
История сохраняется в файл.
"""


def get_hystory(figi):
    aaa = figi
    bbb = 2

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