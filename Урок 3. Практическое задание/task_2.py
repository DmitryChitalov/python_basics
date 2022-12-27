"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def my_func(firstname, lastname, year, city, email, mobile):
    print(f'{firstname} {lastname}, {year} года рождения, проживает в городе {city}, '
    f'email:{email}, телефон: {mobile}')

usr_firstname=input('Введите имя: ')
usr_lastname=input('Введите фамилию: ')
usr_year_of_birth=input('Введите дату рождения: ')
usr_city=input('Введите город: ')
usr_email=input('Введите e-mail: ')
usr_mobile=input('Введите моб.телефон: ')
my_func(usr_firstname, usr_lastname, usr_year_of_birth, usr_city, usr_email, usr_mobile)



#my_func(usr_firstname, usr_lastname, usr_year_of_birth, usr_city, usr_email, usr_mobile)