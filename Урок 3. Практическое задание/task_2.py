"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def args(name, last_name, year_birth, city, email, phone):
    print(f"{name} {last_name} {year_birth} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}")


name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
year_birth = int(input("Год рождения: "))
city = input("Город проживания: ")
email = input("email: ")
phone = input("Телефон: ")
args(name, last_name, year_birth, city, email, phone)
