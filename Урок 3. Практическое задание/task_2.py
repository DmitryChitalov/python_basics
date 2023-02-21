"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_data_func(name, surname, birth_year, city_residence, email, phone_number):
    print(f'{name} {surname} {birth_year} года рождения, проживает в городе {city_residence}, email: {email}, телефон: {phone_number}')
    
user_data_func(name = 'Иван', surname = 'Иванов', birth_year = 1846, city_residence = 'Москва', email = 'jackie@gmail.com', phone_number = '01005321456')

