def calc_divide(num, denom):
    try:
        result = num / denom
        return result
    except ZeroDivisionError:
        print("divide by zero, try again")


num1 = float(input("Введите первое число"))
while True:
    num2 = float(input("Введите второе число"))
    a = calc_divide(num1, num2)
    if a is not None:
        break
print(num1, num2, a)




