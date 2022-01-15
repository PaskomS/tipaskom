#список переменных
from decimal import Decimal

TAX = Decimal(0.13)  # 0.13% НДФЛ
COMISSION = Decimal(0.003)  # 0.3% Тариф Инвестор на 2021-07 Тинькофф Инвестиции
DT_FORMAT = "%Y-%m-%d %H:%M:%S"

with open('control/account/personal.info', 'r') as f:
    lines = f.readlines()
token = lines[1].rstrip('\n')
broker_account_id = lines[3].rstrip('\n')
iis_broker_account_id = lines[5].rstrip('\n')


# token = "еее"
# broker_account_id = '222'
# iis_broker_account_id = '333'
