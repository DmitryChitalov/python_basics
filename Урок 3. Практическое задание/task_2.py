"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
var_1 = str(input("Имя: "))
var_2 = str(input("Фамилия: "))
var_3 = str(input("Год рождения: "))
var_4 = str(input("Город: "))
var_5 = str(input("email: "))
var_6 = str(input("Телефон: "))

def a(name,surname,year,city,email,phone):
    return ' '.join([
        " ", name,
        " крвам", surname,
        ", год рождения ", year,
        ", проживает в городе ", city,
        ", email: ", email,
        ", phone: ", phone, "."
        ])

print(a(name=var_1, surname=var_2, year=var_3, city=var_4, email=var_5, phone=var_6))
