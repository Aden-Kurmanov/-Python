# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translations = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_1 = open('files/text-4.txt', 'r', encoding='utf-8')
file_2 = open('files/text-4-2.txt', 'w', encoding='utf-8')

lst = []

for line in file_1:
    line = line.split(' ')
    lst.append(f'{translations[line[0]]} {line[1]} {line[2]}')

file_2.writelines(lst)

file_1.close()
file_2.close()




