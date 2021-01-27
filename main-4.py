string = input('Введите строку: ')

lst = string.split(' ')

for ind, el in enumerate(lst):
    print(ind + 1, el[0:10])
