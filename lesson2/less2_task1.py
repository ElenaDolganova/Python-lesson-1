# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [1, True, 2, False, 'my_string', {"key1": "word1", }, dict(key2="word2"), {1, "data", 2, 4}, 18, (3, 'name')]
for elem in my_list:
    print(type(elem))
