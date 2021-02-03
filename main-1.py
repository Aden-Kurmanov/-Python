# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def exit(num):
    return True if num == 'q' else False

def count(num1: int, num2: int):
    return num1 / num2

while True:
    print('Для выхода введите q')
    first = input('Введите первое число: ')


    if exit(first):
        break
    first = int(first)

    second = input('Введите второе число: ')

    if exit(second):
        break
    second = int(second)

    if second == 0:
        print('Делить на 0 нельзя, попробуйте еще раз')
        print()
        continue

    res = count(num1=first, num2=second)
    print(f'Результат деления равен {res}')
    print()
