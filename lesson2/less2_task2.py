# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


inp_str = str()
change_list = []
print('Для завершения ввода данных нажмите "///"')
while inp_str != '///':
    inp_str = input('Введите очередное значение: ')
    change_list.append(inp_str)
change_list.remove('///')

new_list = change_list[:]

if len(new_list) % 2 != 0:
    new_len = len(new_list) - 1
else:
    new_len = len(new_list)

for i in range(0, new_len, 2):
    a = new_list[i]
    b = new_list[i + 1]
    new_list[i] = b
    new_list[i + 1] = a

print(change_list)
print(new_list)
