# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                           Физика:   30(л)   —   10(лаб)
#                      Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}
my_f = open("file_task6.txt", "r", encoding='utf-8')

for line in my_f:
    line_str = line.replace('\n', '')
    list_from_string = line_str.split('   ')

    res = 0
    for i in range(1, len(list_from_string)):

        if list_from_string[i] == '—':
            list_from_string[i] = 0
        else:
            elem_from_list = list_from_string[i].split('(')
            list_from_string[i] = elem_from_list[0]
            res = res + int(list_from_string[i])
    list_from_string[1] = res

    elem = list_from_string[0]
    list_from_string[0] = elem[0:(len(list_from_string[0])-1)]

    my_dict[list_from_string[0]] = list_from_string[1]


print(my_dict)
my_f.close()
