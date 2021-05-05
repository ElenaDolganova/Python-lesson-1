# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, n, s, p, income):
        self._income = income
        self.name = n
        self.surname = s
        self.position = p


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        pers_data = self.name + ' ' + self.surname + ' ' + self.position
        return pers_data

    def get_total_income(self):
        money = int(self._income["wage"]) + int(self._income["bonus"])
        return money


income1 = {"wage": 100, "bonus": 10}
income2 = {"wage": 1000, "bonus": 100}
b1 = Position("Bob", "Brown", "Manager", income1)
b2 = Position("John", "Smith", "Director", income2)

print(b1.get_full_name())
print(b1.get_total_income())
print(b1.name, b1.surname, b1.position)
print(b1._income)

print(b2.get_full_name())
print(b2.get_total_income())
print(b2.name, b2.surname, b2.position)
print(b2._income)

