import datetime as dt


class Calculator:
    """Родительский класс для калькулятора денег и каллорий."""
    def __init__(self, limit):
        self.limit = limit  # Лимит на день
        self.records = []  # Список для хранения записей

    def add_record(self, record):
        """Добавляет запись в список records."""
        self.records.append(record)

    def get_today_stats(self):
        """Возвращает значение суммы потраченного/съеденного за сегодня."""
        NOW = dt.date.today()  # Дата на данный момент
        sym_amount = sum(record.amount for record in self.records
                         if record.date == NOW)
        return sym_amount  # Сумма amount за сегодня

    def get_week_stats(self):
        """Возвращает значение суммы потраченного/съеденного за неделю."""
        NOW = dt.date.today()  # Дата на данный момент
        week = NOW - dt.timedelta(weeks=1)  # Промежуток в неделю от NOW
        result = sum(record.amount for record in self.records
                     if week < record.date <= NOW)
        return result  # Сумма amount за неделю

    def get_left_amount(self):
        """Возвращает остаток на сегодня"""
        return self.limit - self.get_today_stats()


class Record:
    """Класс для хранения записей. Хранит количество, комментарий и дату."""
    def __init__(self, amount, comment, date=None):
        NOW = dt.date.today()  # Дата на данный момент
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = NOW


class CashCalculator(Calculator):
    """Калькулятор потраченных денег"""
    USD_RATE = 70.0  # Курс доллара
    EURO_RATE = 85.0  # Курс евро
    RUB_RATE = 1.0  # Курс рубля

    def get_today_cash_remained(self, currency='rub'):
        """В качестве аргумента принимает валюту (по умолчанию рубли),
        затем определяет достинуг ли лимит и возвращает остатко если он есть.
        """
        currencies = {
            'rub': ('руб', self.RUB_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE)
        }
        # Выбирает нужное значение из currencies:
        choice_currency = currencies[currency]
        # Остаток денег:
        left_amount = self.get_left_amount()
        # Считатет остатко согласно указанной валюте:
        count_left_amount = abs((round(left_amount/choice_currency[1], 2)))
        response = (f'{count_left_amount} {choice_currency[0]}')
        if left_amount == 0:
            return 'Денег нет, держись'
        if left_amount < 0:
            return f'Денег нет, держись: твой долг - {response}'
        return f'На сегодня осталось {response}'


class CaloriesCalculator(Calculator):
    """Калькулятор каллорий."""
    def get_calories_remained(self):
        """Определяет достигнут ли лимит каллорий на сегодня.
        Выбиравает ответ в зависимости от результата.
        """
        left_amount = self.get_left_amount()
        if left_amount >= 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {left_amount} кКал')
        return 'Хватит есть!'
