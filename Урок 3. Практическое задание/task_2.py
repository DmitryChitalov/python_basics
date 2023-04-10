"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def personal_data(first_name, last_name, year_of_birth, city, email, phone):
    return f'{first_name} {last_name} {year_of_birth} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}'


print(personal_data(
    first_name='Иванов',
    last_name='Иван',
    year_of_birth=1846,
    city='Москва',
    email='jackie@gmail.com',
    phone='+74994565225',
))
