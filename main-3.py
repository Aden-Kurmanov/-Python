# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('Введите число: '))
num = number
arr = []
whileLength = int(input('Введите количество чисел: '))
i = 0
while i < whileLength:
    arr.append(number)
    number = int(str(number) + str(num))
    i = i + 1

count = 0
i = 0
while i < whileLength:
    count += arr[i]
    i = i + 1
print(count)