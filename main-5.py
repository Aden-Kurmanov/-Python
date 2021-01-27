lst = [7, 5, 3, 3, 2]

new_el = int(input('Введите новый элемент листа (число): '))

lst.sort()
index = lst.index(new_el) if new_el in lst else None

if index is not None:
    lst.insert(index, new_el)
else:
    for ind, el in enumerate(lst):
        exist_next = False
        try:
            if lst[ind + 1]:
                exist_next = True
        except Exception as err:
            print('error: ', err)

        if el <= new_el:
            if exist_next:
                continue
            else:
                lst.insert(ind + 1, new_el)
                break
        else:
            lst.insert(ind, new_el)
            break

print(lst)
