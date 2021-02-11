# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
file = open('files/text-1.txt', 'w')
lines = []
while True:
    line = input('Введите строку: ')
    if not line:
        break
    line = f'{line}\n'
    lines.append(line)
file.writelines(lines)
file.close()
