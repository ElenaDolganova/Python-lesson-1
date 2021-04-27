# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


my_list = []
new_list = []


while True:
    spec_symbol = False
    input_string = input("Введите данные: ")
    my_list = input_string.split(' ')
    print(my_list)

    for elem in my_list:
        try:
            elem = int(elem)
            new_list.append(int(elem))
            print("new_list", new_list)
            sum_res = sum(new_list)
            print("sum_res", sum_res)
        except ValueError:
            spec_symbol = True

    if spec_symbol == True:
        break






