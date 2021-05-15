# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self._matrix])

    def get_value(self, x, y):
        row = self._matrix[x]
        return row[y]

    def __add__(self, other):
        result = []
        for x in range(len(self._matrix)):
            result.append([0 for i in self._matrix[x]])
            for y in range(len(self._matrix[x])):
                result[x][y] = other.get_value(x, y) + self.get_value(x, y)

        return Matrix(result)


m1 = [[31, 22], [37, 43], [51, 86]]
m11 = Matrix(m1)
print(m11)
print("-------")
m2 = [[3, 5], [2, 4], [-1, 64]]
m22 = Matrix(m2)
print(m22)
print("-------")
m3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
m33 = Matrix(m3)
print(m33)
print("-------")
print(m11 + m22)
