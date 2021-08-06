import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.record = record[]


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
        record.append(add_record)

    def get_today_stats(self, currency = 'rub'):

    def get_today_cash_remained(self):

    def get_week_stats(self):


class CaloriesCalculator(Calculator):
    def __init__(self, limit, record):
        super().__init__(limit, record)
    
    def add_record(self):

    def get_today_stats(self):

    def get_calories_remained(self):

    def get_week_stats(self):

cash_calculator.add_record(Record(amount=145, comment='кофе'))

