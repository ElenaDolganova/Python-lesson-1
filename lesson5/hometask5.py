# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


out_f = open("file_task5.txt", "w")
inp_str = input("Введите данные:  ")
out_f.writelines(inp_str)
out_f.close()


my_f = open("file_task5.txt", "r")

line_str = my_f.readline()
line_string = line_str.replace('\n', '')
line_list = line_string.split(' ')
print(line_list)

list_sum = 0

for i in range(0, len(line_list)):
    a = int(line_list[i])
    list_sum = list_sum + a

print(list_sum)

my_f.close()
