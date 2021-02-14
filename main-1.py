# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight:
    __color = ''

    def running(self):
        while True:
            TrafficLight.__color = 'Красный'
            print(TrafficLight.__color)
            time.sleep(7)

            TrafficLight.__color = 'Желтый'
            print(TrafficLight.__color)
            time.sleep(2)

            TrafficLight.__color = 'Зеленый'
            print(TrafficLight.__color)
            time.sleep(5)

traffic = TrafficLight()
traffic.running()
