# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file = open('files/text-5.txt', 'w')

numbers = (input('Введите числа через пробел: ')).split()
for el in numbers:
    file.writelines(f'{el}\n')
file.close()

file = open('files/text-5.txt', 'r+')
content = file.readlines()
count = 0

for el in content:
    el = el.strip().replace(' ', '')
    if el:
        try:
            el = int(el)
            count += el
        except Exception as err:
            continue
file.writelines(f'{count}')
file.close()
