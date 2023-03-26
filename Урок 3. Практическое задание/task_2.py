"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_info(name, surname, year_birth, city, email, phone):
    print(f"{name} {surname} {year_birth} года рождения, проживает в городе {city}. E-mail: {email}, телефон: {phone}")


name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
year_birth = input("Введите ваш год рождения: ")
city = input("Введите ваш город проживания: ")
email = input("Введите ваш email: ")
phone = input("Введите ваш номер телефона: ")
user_info(name=name, surname=surname, year_birth=year_birth, city=city, email=email, phone=phone)
