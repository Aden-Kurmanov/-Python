# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime


class Date:

    def __init__(self, inp_date):
        self.date = inp_date

    @classmethod
    def date_to_number(cls, date: str):
        arr = [int(el) for el in (date.split('-'))]
        return arr

    @staticmethod
    def validation(date):
        day, month, year = [int(el) for el in (date.split('-'))]
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= datetime.date.today().year:
                    return True
                else:
                    return 'Вы ввели неккоректный год'
            else:
                return 'Вы ввели неккоректный месяц'
        else:
            return f'Вы ввели неккоректный день'


date = input(f'Введите дату в формате дд-мм-гггг: ')
validation = Date.validation(date)
if validation:
    print(Date.date_to_number(date))
else:
    print(validation)
