# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from exception import MyClassExcept


class Sklad:
    dct = {
        'printer': {'count': 0, 'total_price': 0, 'names': [], 'colors': []},
        'scaner': {'count': 0, 'total_price': 0, 'names': [], 'colors': []},
        'kserox': {'count': 0, 'total_price': 0, 'names': [], 'colors': []}
    }

    @staticmethod
    def update_dct(type_tech, name, price, color):
        Sklad.dct[type_tech]['count'] += 1
        Sklad.dct[type_tech]['total_price'] += price
        Sklad.dct[type_tech]['names'].append(name)
        Sklad.dct[type_tech]['names'] = list(set(Sklad.dct[type_tech]['names']))
        Sklad.dct[type_tech]['colors'].append(color)
        Sklad.dct[type_tech]['colors'] = list(set(Sklad.dct[type_tech]['colors']))


class OrgTechnique:

    def __init__(self, name, price, color, type_tech):
        self.name = name
        self.price = price
        self.color = color
        Sklad.update_dct(type_tech, name, price, color)


class Printer(OrgTechnique):

    def __init__(self, name, price, color, formats):
        super().__init__(name, price, color, 'printer')
        self.formats = formats


class Skaner(OrgTechnique):

    def __init__(self, name, price, color, mode):
        super().__init__(name, price, color, 'scaner')
        self.mode = mode


class Kserox(OrgTechnique):

    def __init__(self, name, price, color, speed):
        super().__init__(name, price, color, 'kserox')
        self.printer_speed = speed


while True:
    type_tech = input('Введите тип оргтехники (1 - принтер, 2 - сканер, 3 - ксерокс, q - выйти): ')
    if type_tech == 'q':
        print(Sklad.dct)
        break
    try:
        if not MyClassExcept.check_number(type_tech):
            raise MyClassExcept('Необходимо вводить только числа')
        type_tech = int(type_tech)
        tech_name = input('Введите название: ')
        tech_price = int(input('Введите цену: '))
        tech_color = input('Введите цвет: ')
        if type_tech == 1:
            tech_formats = (input('Введите поддерживаемые форматы через пробел: ')).split()
            tech = Printer(tech_name, tech_price, tech_color, tech_formats)
        elif type_tech == 2:
            tech_mode = input('Введите режим работы сканера: ')
            tech = Skaner(tech_name, tech_price, tech_color, tech_mode)
        elif type_tech == 3:
            tech_speed = int(input('Введите скорость ксерокса: '))
            tech = Kserox(tech_name, tech_price, tech_color, tech_speed)
        else:
            print('Вы ввели неккоректную цифру')
        print()
    except MyClassExcept as e:
        print(e)
        print()
