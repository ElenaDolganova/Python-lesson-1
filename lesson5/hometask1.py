# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.



out_f = open("file_task1.txt", "w")
inp_str = ''

while True:
    inp_str = input("Введите данные:  ")
    if len(inp_str) > 0:
        inp_str = inp_str + '\n'
        out_f.writelines(inp_str)
    else:
        break

out_f.close()


