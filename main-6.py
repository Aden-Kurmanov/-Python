length = int(input('Количество новых товаров: '))
lst = []

i = 0
while i < length:
    i += 1
    print()
    print('Добавим новый товар')
    name = input('Наименование: ')
    price = int(input('Цена: '))
    count = int(input('Количество: '))
    unit_measuring = input('Единица измерения: ')
    obj = {
        'название': name,
        'цена': price,
        'количество': count,
        'ед': unit_measuring
    }
    tup = (i, obj)
    lst.append(tup)

dct = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}

for ind, el in enumerate(lst):
    print('el: ', el[1])
    for e in dct:
        dct[e].append(el[1][e])

for e in dct:
    dct[e] = list(set(dct[e]))
print('dct 2: ', dct)
