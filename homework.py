import datetime as dt

NOW = dt.date.today()  # Дата на данный момент


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
        sym_amount = sum(record.amount for record in self.records
                         if record.date == NOW)
        return sym_amount  # Сумма amount за сегодня

    def get_week_stats(self):
        """Возвращает значение суммы потраченного/съеденного за неделю."""
        week = NOW - dt.timedelta(weeks=1)  # Промежуток в неделю от NOW
        result = sum(record.amount for record in self.records
                     if record.date > week and record.date <= NOW)
        return result  # Сумма amount за неделю


class Record:
    """Класс для хранения записей. Хранит количество, комментарий и дату."""
    def __init__(self, amount, comment, date=None):
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

    def get_today_cash_remained(self, currency='rub'):
        """В качестве аргумента принимает валюту (по умолчанию рубли),
        затем определяет достинуг ли лимит и возвращает остатко если он есть.
        """
        sym_amount = self.get_today_stats()  # Сумма amount за сегодня
        left_money = self.limit - sym_amount  # Остаток денег
        euro = left_money / self.EURO_RATE  # Остаток в евро
        usd = left_money / self.USD_RATE  # Остаток в доллорах
        if currency == 'eur':
            if left_money == 0:
                return 'Денег нет, держись'
            elif left_money < 0:
                return ('Денег нет, держись: твой долг - '
                        f'{abs(euro):.2f} Euro')
            else:
                return ('На сегодня осталось '
                        f'{euro:.2f} Euro')
        elif currency == 'usd':
            if left_money == 0:
                return 'Денег нет, держись'
            elif left_money < 0:
                return ('Денег нет, держись: твой долг - '
                        f'{abs(usd):.2f} USD')
            else:
                return ('На сегодня осталось '
                        f'{usd:.2f} USD')
        else:
            if left_money == 0:
                return 'Денег нет, держись'
            elif left_money < 0:
                return('Денег нет, держись: твой долг - '
                       f'{abs(left_money)} руб')
            else:
                return ('На сегодня осталось '
                        f'{left_money} руб')


class CaloriesCalculator(Calculator):
    """Калькулятор каллорий."""
    def get_calories_remained(self):
        """Определяет достигнут ли лимит каллорий на сегодня.
        Выбиравает ответ в зависимости от результата.
        """
        sym_amount = self.get_today_stats()  # Сумма amount за сегодня
        # Остаток каллорий на сегодня:
        left_calories = (self.limit - sym_amount)
        if left_calories >= 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {left_calories} кКал')
        else:
            return 'Хватит есть!'
