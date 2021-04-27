# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(word_lower):
    new_word = word_lower[0].upper() + word_lower[1:]
    return new_word

one_word = int_func("wordwordword")
print(one_word)

result_string = []
words_lower = "word word word"
list_words_lower = words_lower.split()

for word in list_words_lower:
    a = int_func(word)
    result_string.append(a)

result_string = ' '.join(result_string)
print(result_string)
 

