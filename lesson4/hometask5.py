# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def multiply_func(x, y):
    return x * y


even_list = [elem for elem in range(100, 1001) if elem % 2 == 0]
result = reduce(multiply_func, even_list)
print(result)
