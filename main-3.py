# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, {'wage': wage, 'bonus': bonus})

    def get_full_name(self):
        return f'{self.surname} {self.name}, {self.position}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

info = Position('Aden', 'Kurmanov', 'Developer', 300000, 0)
print(f'{info.get_full_name()}, {info.get_total_income()}')
