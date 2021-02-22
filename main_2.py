# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyClass(Exception):
    def __init__(self, txt):
        self.txt = txt


def count(a, b):
    try:
        if b == 0:
            raise MyClass('Делить на ноль нельзя')
        print(a / b)
    except MyClass as err:
        print(err)
        print()
        get_numbers()


def get_numbers():
    num_1 = int(input('number 1: '))
    num_2 = int(input('number 2: '))
    count(num_1, num_2)


get_numbers()
