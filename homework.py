import datetime as dt

NOW = dt.date.today()
USD_RATE = 70
EURO_RATE = 85


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, add_record):
        self.records.append(add_record)

    def get_today_stats(self):
        sym_amount = 0
        for day in self.records:
            if day.date == NOW:
                sym_amount += day.amount
        return sym_amount

    def get_week_stats(self):
        week = NOW - dt.timedelta(weeks=1)
        week_amount = 0
        for day in self.records:
            if day.date > week:
                week_amount += day.amount
        if isinstance(self, CashCalculator):
            print(f'За неделю потрачено {week_amount} денег')
        elif isinstance(self, CaloriesCalculator):
            print(f'За неделю накушано {week_amount} каллорий')


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = NOW


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency='rub'):
        """В качестве аргумента принимает валюту (по умолчанию рубли),
        затем определяет достинуг ли лимит и возвращает остатко если он есть.
        """
        sym_amount = self.get_today_stats()
        left_money = (self.limit - sym_amount)
        views_currency = ['руб', 'USD', 'EURO']
        if currency == 'eur':
            if left_money == 0:
                print('Денег нет, держись')
            elif left_money < 0:
                print('Денег нет, держись: твой долг - '
                      f'{(left_money / EURO_RATE):.2f} {views_currency[2]}')
            else:
                print('На сегодня осталось '
                      f'{(left_money / EURO_RATE):.2f} {views_currency[2]}')
        elif currency == 'usd':
            if left_money == 0:
                print('Денег нет, держись')
            elif left_money < 0:
                print('Денег нет, держись: твой долг - '
                      f'{(left_money / USD_RATE):.2f} {views_currency[1]}')
            else:
                print('На сегодня осталось '
                      f'{(left_money / USD_RATE):.2f} {views_currency[1]}')
        else:
            if left_money == 0:
                print('Денег нет, держись')
            elif left_money < 0:
                print('Денег нет, держись: твой долг - '
                      f'{left_money} {views_currency[0]}')
            else:
                print('На сегодня осталось '
                      f'{left_money} {views_currency[0]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        sym_amount = self.get_today_stats()
        left_calories = (self.limit - sym_amount)
        if left_calories >= 0:
            print('Сегодня можно съесть что-нибудь ещё, '
                  f'но с общей калорийностью не более {left_calories} кКал')
        else:
            print('Хватит есть!')


cash_calculator = CashCalculator(5000)
cash_calculator.add_record(Record(amount=300,
                                  comment='кофе'))
cash_calculator.add_record(Record(amount=500,
                                  comment='бутерброд',
                                  date='08.08.2021'))
cash_calculator.add_record(Record(amount=500,
                                  comment='бутерброд',
                                  date='02.08.2021'))
cash_calculator.get_today_cash_remained()
cash_calculator.get_today_cash_remained(currency='usd')
cash_calculator.get_today_cash_remained(currency='eur')
cash_calculator.get_week_stats()
print('------------------------------')
calories_calculator = CaloriesCalculator(3000)
calories_calculator.add_record(Record(amount=400,
                                      comment='супчик'))
calories_calculator.add_record(Record(amount=300,
                                      comment='бургер',
                                      date='08.08.2021'))
calories_calculator.add_record(Record(amount=300,
                                      comment='салат',
                                      date='02.08.2021'))
calories_calculator.get_calories_remained()
calories_calculator.get_week_stats()
