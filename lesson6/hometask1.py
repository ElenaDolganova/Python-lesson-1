# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self, new_color, time_s):
        if new_color == 'red':
            self.__color = 'red'
        if new_color == 'yellow':
            self.__color = 'yellow'
        if new_color == 'green':
            self.__color = 'green'

        print(self.__color)
        time.sleep(time_s)
        print(self.__color, time_s)


a = TrafficLight(color='red')
a.running('red', 7)
a.running('yellow', 2)
a.running('green', 10)



