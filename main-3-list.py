lst_1 = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
lst_2 = ['Зима', 'Весна', 'Лето', 'Осень']


month_number = int(input('Введите номер месяца: '))

if month_number > 12:
    print('Вы ввели некорректный номер месяца')

for i in range(len(lst_1)):
    if month_number in lst_1[i]:
        print(lst_2[i])
        break

