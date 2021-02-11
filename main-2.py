# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('files/text-2.txt', 'r')
lines = file.readlines()

lines_count = 0
words_count = 0

for line in lines:
    if line.strip().replace(' ', ''):
        words = len(line.strip().split())
        words_count += words
        lines_count += 1
        print(f'Количество слов в строке составляет: {words}', end='\n')

print()
print(f'Количество строк составляет: {lines_count}')
print(f'Общее количество слов составляет: {words_count}')
file.close()
