"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def my_func(f_name, s_name, year, city, email, phone):
    print(f'{f_name} {s_name} {year} year of birth, living in {city}, email: {email}, phone: {phone}')


my_func(f_name=input('input first name: '), s_name=input('input second name: '), year=input('input year of birth: '),
        city=input('input city where you live: '), email=input('input email: '), phone=input('input phone number:'))
