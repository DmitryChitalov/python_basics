"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_info(_name, _second_name, _years, _city, _email, _phone):
    print(f'{_name} {_second_name} {_years} года рождения, проживает в городе {_city}, email: {_email}, телефон: {_phone}')


name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
years = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

user_info(name, second_name, years, city, email, phone)
