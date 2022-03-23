"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

name = input('Enter your name ')
surname = input('Enter your surname ')
birthday = input('Enter your birthday ')
city = input('Enter your city ')
email = input('Enter your email ')
phone = input('Enter your phone ')


def func(name, surname, birthday, city, email, phone):
    print(
        f'Your name is {surname} {name}, '
        f'your birthday is {birthday}, '
        f'your live in {city}, '
        f'your email is {email}, '
        f'your phone is {phone}')


func(name, surname, birthday, city, email, phone)
