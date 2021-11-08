"""
Основной управляющий модуль.

Реагирует на события, вызывает исполнения.
"""
#mport tinvest as tinvest

#import control.account.variables as variables

from control.account.cur_account import account
from control.account.cur_account import portfolio

import control.stocks as stocks

serfigi = 'BBG000PSKYX7' # visa figi 'BBG000PSKYX7'
visa = stocks.Stock(serfigi)
bashneft = stocks.Stock("BBG004S68758")
# if stocks.Stock(serfigi).figi_found:
#     asd = stocks.Stock(serfigi)
# if stocks.Stock("BBG004S68758").figi_found:
#     asdddd = stocks.Stock("BBG004S68758")

bashneft.update_hystory()

pass
#
# import control.hystory.gethystory as gethystory
#
#
# acc = curacc.get_account(variables.token, variables.broker_account_id)
# abb = acc.curPortfolio
# # print(acc.chkStatus())
# acc.syncAcc()
# # print(acc.gGetExRateUSD())
#
#
#
# bbb = acc.myStocks[0].figi
#
# fff = acc.curAccount.get_market_candles(bbb, "2021-09-23T15:00:00+04:00", "2021-09-24T15:00:00+04:00", tinvest.CandleResolution.day)
#
#
# aaa = fff.payload.candles[0]
#
#
# #ff = gethystory.gethystory(acc.curAccount, bbb)
#
#
# pass
