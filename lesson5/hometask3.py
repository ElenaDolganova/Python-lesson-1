# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


my_f = open("file_task3.txt", "r", encoding='utf-8')
n = 0
line_str = ''
persons_list = []
sum_salary = 0
persons_min = []
min_sal = 20000.00
for line in my_f:
    n += 1
    line_str = line.replace('\n', '')
    line_list = line_str.split(' ')
    persons_list.append(line_list)
#    print(line_list)
    sum_salary = sum_salary + float(line_list[1])

    if float(line_list[1]) < min_sal:
        persons_min.append(line_list[0])
    else:
        continue

average_salary = round((sum_salary / n), 2)
print("Средняя величина дохода сотрудников = ", average_salary)
print("Сотрудники с окладом меньше 20000.00:  ", persons_min)

my_f.close()
