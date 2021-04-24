# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


surname = "Smith"
y_birth = 1985
city = "NY"
email = "email@email.com"
phone = 12345678


def person_data(name, s_name, y_birth=1993, city="Moscow", email="e@e.ee", phone=192929292):
    print(name, s_name, y_birth, city, email, phone)


person_data(name="John", s_name=surname, y_birth=int(input("my date of birth: ")), email=email, phone=phone)
person_data(name="Petr", s_name="Ivanov", y_birth=y_birth, city="Perm", email=email, phone=phone)
