# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Введите натуральное число: ")
number1 = int(n)
number2 = int(n + n)
number3 = int(n + n + n)
result = number1 + number2 + number3
print("n + nn + nnn = ", result)
