import control.account.cur_account as cur_account
import control.db.hystory_candles as hystory_candles


class Figi:
    """
        ИД портфеля пока по умолчанию
        Класс акции, загрузка данных по акции,
        проверка есть ли данная акция в портфеле
    """

    def __init__(self, figi:str):
        self.figi = figi
        self.cur_account = cur_account
        try:
            self.stock = cur_account.account.get_market_search_by_figi(self.figi)
            self.figi_found = True
            self.table = hystory_candles.create_table(self.figi)
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
        for stock in cur_account.portfolio.stocks:
            if self.figi == stock.figi:
                return True
            else:
                return False

    def update_hystory(self):
        """
            получение исторических котировок акции,
            заполнение и обновление базы данных в случае необходимости
            1 разобраться, нужно ли вообще обновление, те проверить актуальность данных
            2 если нужно обновление, запросить с какого момента
            3 в этом модуле запросить котировки
            4 отправить котировки на запись в бд
        """

        hystory_candles.update(self)

        #candl = account.get_market_candles(self.figi, "2019-08-01T00:00:00+00:00", "2019-09-01T00:00:00+00:00", acc.tinvest.CandleResolution.day)
        #candl = acc.account.get_market_candles(self.figi, "2022-01-06T00:00:00+00:00", "2022-01-06T23:00:00+00:00",
        #                                   acc.tinvest.CandleResolution.min1)
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
