"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
from more_itertools import last


def print_data(name, lastname, b_year, city, email, phone):
    print(f'''{name} {lastname} {b_year} года рождения, проживает в городе {city},\n email: {email}, телефон: {phone}''')

name = input('Введите имя ==>')
lastname = input('Введите фамилию ==>')
b_year = input('Введите год рождения ==>')
city = input('Введите город проживания ==>')
email = input('Введите email ==>')
phone = input('Введите телефон ==>')

print_data(name=name, lastname=lastname, b_year=b_year, city=city, email=email, phone=phone)
