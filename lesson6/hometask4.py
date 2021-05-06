# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.
from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed > 0:
            print('машина поехала', self.speed, 'км/ч')
        else:
            print('машина не поехала', self.speed, 'км/ч')

    def stop(self):
        if self.speed == 0:
            print('машина остановилась')
        else:
            print('машина не остановилась')

    def turn(self):
        if self.speed != 0:
            self.direction = ''
            dir = randint(0, 1)
            if dir == 0:
                self.direction = "left"
                print('машина повернула', self.direction)
            else:
                self.direction = "right"
                print('машина повернула', self.direction)
        else:
            print('машина не повернула')

    def show_speed(self):
        print('текущая скорость автомобиля', self.speed, 'км/ч')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        print('Обычная машина')

    def show_speed(self):
        if self.speed > 60:
            print('Превышена скорость > 60')
        else:
            print('скорость автомобиля', self.speed, 'км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        print('Спортивная машина')


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        print('Рабочая машина')

    def show_speed(self):
        if self.speed > 40:
            print('Превышена скорость > 40')
        else:
            print('скорость автомобиля', self.speed, 'км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
        self.is_police = True
        print('Полицейская машина')


t = TownCar(70, 'grey', 'Audi')
print(t.name, t.speed, 'км/ч', t.color)
t.show_speed()
t.go()
t.turn()
t.stop()
print("-------")
t1 = TownCar(0, 'red', 'Audi')
print(t1.name, t1.speed, 'км/ч', t1.color)
t1.show_speed()
t1.go()
t1.turn()
t1.stop()
print("-------")
p = PoliceCar(80, 'grey', 'Audi')
print(p.name, p.speed, 'км/ч', p.color)
p.show_speed()
p.go()
p.turn()
p.stop()
print("-------")
p1 = PoliceCar(10, 'blue', 'Audi')
print(p1.name, p1.speed, 'км/ч', p1.color)
p1.show_speed()
p1.go()
p1.turn()
p1.stop()
print("-------")
w = WorkCar(50, 'yellow', 'KAMAZ')
print(w.name, w.speed, 'км/ч', w.color)
w.show_speed()
w.go()
w.turn()
w.stop()
print("-------")
w1 = WorkCar(30, 'yellow', 'TRACK')
print(w1.name, w1.speed, 'км/ч', w1.color)
w1.show_speed()
w1.go()
w1.turn()
w1.stop()
print("-------")
s = SportCar(250, 'red', 'SportCar')
print(s.name, s.speed, 'км/ч', s.color)
s.show_speed()
s.go()
s.turn()
s.stop()
print("-------")
s1 = SportCar(0, 'white', 'SportCar1')
print(s1.name, s1.speed, 'км/ч', s1.color)
s1.show_speed()
s1.go()
s1.turn()
s1.stop()
