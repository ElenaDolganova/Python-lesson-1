# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


my_f = open("file_task4.txt", "r", encoding='utf-8')

line_str = ''
eng_list = []
rus_eng_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for line in my_f:
    line_str = line.replace('\n', '')
    line_list = line_str.split(' ')
    eng_list.append(line_list)

    k = 0
    for eng_word in line_list[:]:
        k += 1
        for elem in rus_eng_dict.keys():
            if eng_word == elem:
                line_list[k-1] = rus_eng_dict[eng_word]

my_f.close()

out_f = open("file_task4_rus.txt", "w", encoding='utf-8')
for i in range(0, len(eng_list)):
    rus_str = " ".join(eng_list[i])
    rus_str = rus_str + '\n'

    out_f.writelines(rus_str)

out_f.close()
