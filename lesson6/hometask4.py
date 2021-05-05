# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if speed > 0:
            print('машина поехала', speed, 'км/ч')
        else:
            print('машина не поехала', speed, 'км/ч')

    def stop(self, speed):
        if speed == 0:
            print('машина остановилась')
        else:
            print('машина не остановилась')

    def turn(self, direction):
        self.direction = direction
        print('машина повернула на', self.direction)

    def show_speed(self, speed):
        print('текущая скорость автомобиля', self.speed, 'км/ч')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Обычная машина')
        if self.speed > 60:
            print('Превышена скорость > 60')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Спортивная машина')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Рабочая машина')
        if self.speed > 40:
            print('Превышена скорость > 40')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police:
            print('Полицейская машина')


t = TownCar(70, 'grey', 'Audi', False)
print(t.name, t.speed, 'км/ч', t.color)
t.show_speed(t.speed)
t.go(20)
t.turn("лево")
t.stop(0)
print("-------")
p = PoliceCar(80, 'grey', 'Audi', True)
print(p.name, p.speed, 'км/ч', p.color)
p.show_speed(p.speed)
p.go(20)
p.turn("лево")
p.stop(0)
print("-------")
w = WorkCar(50, 'yellow', 'KAMAZ', False)
print(w.name, w.speed, 'км/ч', w.color)
w.show_speed(w.speed)
w.go(0)
w.turn("лево")
w.stop(0)
print("-------")
s = SportCar(250, 'red', 'SportCar', False)
print(s.name, s.speed, 'км/ч', s.color)
s.show_speed(s.speed)
s.go(2)
s.turn("лево")
s.stop(10)


