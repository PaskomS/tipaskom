# сводная статистика по портфелю
# from main import usd
import tinvest as tinvest

def cCalkulateStatistik(r, aAccountID):
    usd = float(r.get_market_orderbook("BBG0013HGFT4", 1).payload.close_price)  # цена доллара из стакана, имхо
    print(usd)
    r = r.get_portfolio(aAccountID)

    # print(r)

    ############ Классы объектов ответа get_portfolio в SDK от @daxartio https://github.com/daxartio/tinvest
    # tinvest.Portfolio = List[PortfolioPosition] # список объектов класса tinvest.PortfolioPosition

    # tinvest.PortfolioPosition
    # class PortfolioPosition(BaseModel):
    #     name: str  # Название бумаги

    #     average_position_price: Optional[MoneyAmount] = Field(alias='averagePositionPrice') # сред. цена покупок бумаги в портфеле
    #     average_position_price_no_nkd: Optional[MoneyAmount] = Field( # актуально для облигаций
    #         alias='averagePositionPriceNoNkd'
    #     )

    #     balance: Decimal # колво акций (не лотов)
    #     lots: int # лот, минимальный объем покупки
    #     blocked: Optional[Decimal]  # заблокировано под продажу

    #     expected_yield: Optional[MoneyAmount] = Field(alias='expectedYield') # ожидаемая прибыль НА ВСЮ ПОЗИЦИЮ !!!

    #     figi: str # обязательно
    #     ticker: Optional[str]
    #     isin: Optional[str]

    #     instrument_type: InstrumentType = Field(alias='instrumentType') # stock, bond, etf etc.

    # class MoneyAmount(BaseModel):
    #     currency: Currency
    #     value: Decimal

    ################# посчитаю ожидаемую прибыль портфеля за вычетом комиссий и налогов ПРИМЕРНО !

    profit = []
    sales = []
    for p in r.payload.positions:
        y = float(p.expected_yield.value)  # НА ВСЮ ПОЗИЦИЮ, а не на 1 бумагу
        price = float(p.average_position_price.value)
        # для долларовых бумаг (доллар в портфеле тоже считается бумагой)
        if p.expected_yield.currency == tinvest.Currency.usd:
            y *= usd
            price *= usd

        profit.append(y)  # налоги считаю по прибыли уменьшая налог. базу убытками
        sales.append(price * float(p.balance) + y)

    # комиссию считаю от всей суммы продаж
    total = {
        'sales_total, rub': sum(sales),
        'profit_total, rub': sum(profit),
    }

    total['taxes'] = total['profit_total, rub'] * 0.13  # 0.13% НДФЛ
    total['comission'] = total['sales_total, rub'] * 0.003  # 0.3% Тариф Инвестор на 2021-07 Тинькофф Инвестиции
    total['payed_total'] = total['taxes'] + total['comission']
    total['money_cleaned'] = total['sales_total, rub'] - total['payed_total']
    total['profit_cleaned'] = total['profit_total, rub'] - total['payed_total']

    print(total)

    # "positions": [
    #     {
    #         "figi": "string",
    #         "ticker": "string",
    #         "isin": "string",
    #         "instrumentType": "Stock",
    #         "balance": 0,
    #         "blocked": 0,
    #         "expectedYield": {
    #             "currency": "RUB",
    #             "value": 0
    #         },
    #         "lots": 0,
    #         "averagePositionPrice": {
    #             "currency": "RUB",
    #             "value": 0
    #         },
    #         "averagePositionPriceNoNkd": {
    #             "currency": "RUB",
    #             "value": 0
    #         },
    #         "name": "string"
    #     }
