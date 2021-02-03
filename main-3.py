# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1: int, num2: int, num3: int):
    lst = [num1, num2, num3]
    first = max(lst)
    lst.remove(first)
    second = max(lst)
    return first + second

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

print(f'Сумма двух наибольших чисел составляет: {my_func(num1, num2, num3)}')


