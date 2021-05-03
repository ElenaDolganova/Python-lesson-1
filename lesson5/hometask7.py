# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

sum_res = 0
profit_dict = {}
firm_dict = {}
with open("file_task7.txt", "r", encoding='utf-8') as out_f:

    for line in out_f:
        line_str = line.replace('\n', '')
        list_from_string = line_str.split('   ')

        res = int(list_from_string[2]) - int(list_from_string[3])
        firm_dict[list_from_string[0]] = res
        sum_res = sum_res + res

    average_profit = round(sum_res / 3)
    profit_dict['average_profit'] = average_profit
    res_list = [firm_dict, profit_dict]
    print(res_list)

with open('file_task7_result.json', "w") as in_file:
    json.dump(res_list, in_file)


