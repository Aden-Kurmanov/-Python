dct = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

month_number = int(input('Введите номер месяца: '))

if month_number > 12:
    print('Вы ввели неккоректный месяц')

for el in dct:
    if month_number in dct[el]:
        print(el)
        break
