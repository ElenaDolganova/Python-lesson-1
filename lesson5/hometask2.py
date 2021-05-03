# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_f = open("file_task2.txt", "r", encoding='utf-8')
n = 0
line_str = ''
for line in my_f:
    n += 1
#    print(n, ".  ", line.replace('\n', ''))
    line_str = line.replace('\n', '')
    len_line_list = len(line_str.split(' '))
#    print("line_str", line_str)
    print("Количество слов в", n, "-ой строке:", len_line_list)

print("Количество строк в файле = ", n)
my_f.close()

