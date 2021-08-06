import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []


class Record:
    now = dt.datetime.now()
    def __init__(self, amount, comment, date=now.date()):
        self.amount = amount
        self.date = date
        self.comment = comment


class CashCalculator(Calculator):
    def __init__(self, limit, record, currency):
        super().__init__(limit, record)
        self.currency = currency

    def add_record(self, add_record):
        records.append(add_record)

    def get_today_stats(self):
        now = dt.datetime.now()
        sym_amount = 0
        for date in record:
            if date.date == now.date():
                sym_amount += date.amount
        return sym_amount
                
    def get_today_cash_remained(self, currency='rub'): # <--- Закончил тут! Делаю функцию для подставки валюты.
        USD_RATE = 70
        EURO_RATE = 85
        limit = self.limit
        sym_amount = self.get_today_stats()
        left_money = (limit - sym_amount) / USD_RATE
        def response(currency):
            views_currency = ['руб', 'USD', 'EURO']
            if left_money == 0:
                print('Денег нет, держись')
            elif left_money < 0:
                print(f'Денег нет, держись: твой долг - {left_money} {views_currency[]}')
            else:
                print(f'На сегодня осталось {left_money} USD')

        if currency == 'usd':
            if left_money == 0:
                print('Денег нет, держись')
            elif left_money < 0:
                print(f'Денег нет, держись: твой долг - {left_money} USD')
            else:
                print(f'На сегодня осталось {left_money} USD')
        elif currency == 'eur:':
            


    def get_week_stats(self):


class CaloriesCalculator(Calculator):
    def __init__(self, limit, record):
        super().__init__(limit, record)
    
    def add_record(self):

    def get_today_stats(self):

    def get_calories_remained(self):

    def get_week_stats(self):

cash_calculator.add_record(Record(amount=145, comment='кофе'))

