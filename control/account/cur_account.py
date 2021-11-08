import tinvest as tinvest
import control.account.variables as variables

account = tinvest.SyncClient(variables.token)

class Portfolio:
    """ клас Портфолио, пока по умолчанию используется обычный брокер счет (variables.broker_account_id)
    """
    def __init__(self):
        self.broker_account_id = variables.broker_account_id
        self.portfolio = account.get_portfolio(self.broker_account_id)
        self.stocks = []
        self.bond = []
        self.etf = []
        self.currency = []
        self.get_all_position()

    def get_all_position(self):
        """ разбираем по коллекциям акции, облигации, фонды и тп
        """
        for p in self.portfolio.payload.positions:
            if p.instrument_type.value == "Stock":
                self.stocks.append(p)
            if p.instrument_type.value == "Bond":
                self.bond.append(p)
            if p.instrument_type.value == "Etf":
                self.etf.append(p)
            if p.instrument_type.value == "Currency":
                self.currency.append(p)

    def get_exchange_rate_usd(self):
        return float(account.get_market_orderbook("BBG0013HGFT4", 1).payload.close_price)  # цена доллара из стакана, имхо


portfolio = Portfolio()
