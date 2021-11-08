import control.hystory.gethystory
from control.account.cur_account import account
from control.account.cur_account import portfolio


class Stock:
    """
        ИД портфеля пока по умолчанию
        Класс акции, загрузка данных по акции,
        проверка есть ли данная акция в портфеле
    """

    def __init__(self, figi):
        self.figi = figi
        #self.account = account
        try:
            self.stock = account.get_market_search_by_figi(self.figi)
            self.figi_found = True
        except Exception:
            self.figi_found = False

    def get_position_details(self):
        """ получить информацию по акции,
            куплена ли, если куплена..."""
        pass

    def verify_stock_in_portfolio_exist(self):
        """
            проверка есть ли данная акция в портфеле
        """
        for stock in portfolio.stocks:
            if self.figi == stock.figi:
                return True
            else:
                return False

    def update_hystory(self):
        """
            получение исторических котировок акции,
            заполнение и обновление базы данных в случае необходимости
        """
        control.hystory.gethystory.get_hystory(self.figi)
        #candl = account.get_market_candles(self.figi, "2019-08-01T00:00:00+00:00", "2019-09-01T00:00:00+00:00", tinvest.CandleResolution.day)