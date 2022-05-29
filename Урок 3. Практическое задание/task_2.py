"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_user_data(name, last_name, year_of_birth, city, email, phone):
    print(f'''{name} {last_name} {year_of_birth} года рождения, проживает в городе {city},\n email: {email}, телефон: {phone}''')


name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

print_user_data(name, last_name, year_of_birth, city, email, phone)
