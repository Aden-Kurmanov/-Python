length = int(input('Enter count of list: '))
lst = []

while length:
    length -= 1
    input_data = input('Enter element: ')
    lst.append(input_data)
print(lst)

for i in range(len(lst)):
    print(i)
    check = False
    try:
        check = True if lst[i + 1] else True
    except IndexError as err:
        print('err: ', err)

    if i % 2 == 0 and check:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)
