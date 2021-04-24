import math

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def negative_power(r, z):
    if z == 0:
        result = 0
        return result
    else:
        i = 1
        res = 1
        while i <= abs(z):
            res = res * r
            i += 1
        result = 1 / res
        return result


r = math.sqrt(2)
z = -1

result_func = negative_power(r, z)
print('my   result: ', result_func)
print('real result: ', r ** z)
