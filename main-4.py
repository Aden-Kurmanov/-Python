# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите целое число: ')

biggest = 0
length = len(number)
i = 0
while i < length:
    num = int(number[i])
    if num > biggest:
        biggest = num
    i += 1
print(biggest)