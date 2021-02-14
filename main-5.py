# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title} для класса ', end='')

class Pen(Stationary):

    def __init__(self, title):
        super(Pen, self).__init__(title=title)

    def draw(self):
        super().draw()
        print(Pen.__name__)

class Pencil(Stationary):

    def __init__(self, title):
        super(Pencil, self).__init__(title=title)

    def draw(self):
        super().draw()
        print(Pencil.__name__)

class Handle(Stationary):

    def __init__(self, title):
        super(Handle, self).__init__(title=title)

    def draw(self):
        super().draw()
        print(Handle.__name__)

pen = Pen('ручка')
pen.draw()

print()

pencil = Pencil('карандаш')
pencil.draw()

print()

handle = Handle('handle')
handle.draw()

