# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

from time import sleep

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.stopped = False

    def show_speed(self):
        print(f'Скорость: {self.speed}')
        if self.speed > 120 and not self.is_police:
            self.speed = 0
            print('Вас лишают прав')
            self.stop()

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        normal_speed = 60
        super().show_speed()
        if self.speed > normal_speed:
            print(f'Превышение скорости на {self.speed - normal_speed}')

    def turn(self, direction):
        super().turn(direction)


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def turn(self, direction):
        super().turn(direction)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        normal_speed = 40
        super().show_speed()
        if self.speed > normal_speed:
            print(f'Превышение скорости на {self.speed - normal_speed}')

    def turn(self, direction):
        super().turn(direction)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def turn(self, direction):
        super().turn(direction)

town_car = TownCar(73, 'black', 'Mazda', False)
sport_car = SportCar(125, 'white', 'sport', False)
work_car = WorkCar(46, 'green', 'bus', False)
police_car = PoliceCar(140, 'blue', 'ДПС', True)

town_car.go()
town_car.show_speed()
town_car.turn('left')
town_car.stop()

print()

sport_car.go()
sport_car.show_speed()

print()

work_car.go()
work_car.turn('right')
work_car.stop()

print()

police_car.go()
police_car.turn('left')
police_car.go()
police_car.show_speed()
police_car.turn('right')
police_car.stop()
