"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def output_of_user_data (name, surname, date_of_birth, city, email, phone_number):
    print (f'{name} {surname}, {date_of_birth} года рождения, проживает в городе {city}, email: {email}, телефон: {phone_number}')


output_of_user_data(name="Иван", surname="Иванов", date_of_birth=1846, city="Москва", email="jackie@gmail.com", phone_number="01005321456")