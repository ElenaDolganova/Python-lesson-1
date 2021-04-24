# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def my_func(arg1, arg2, arg3):
    list_arg = [arg1, arg2, arg3]
    list_arg1 = sorted(list_arg, reverse=True)
    result_sum = list_arg1[0] + list_arg1[1]
    print(result_sum)

my_func(1, 2, 3)