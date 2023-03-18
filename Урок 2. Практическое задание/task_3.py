"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456

"""


def user_data(firstname, lastname, date_birth, city, email, phone):
    return print(f'Имя: {firstname}, Фамилия: {lastname}, '
                 f'Год рождения: {date_birth}, Город проживания: {city}, '
                 f'Email: {email}, Телефон: {phone}.')


firstname = input('Имя: ')
lastname = input('Фамилия: ')
date_birth = input('Год Рождения: ')
city = input('Город проживания: ')
email = input('Email: ')
phone = input('Телефон: ')

user_data(firstname, lastname, date_birth, city, email, phone)
