"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def define_user(name='', surname='', year_of_birth='', city='', email='', phone_numb=''):
    """Функция принимающая несколько элементов"""
    if name:
        print(name, end=' ')
    if surname:
        print(surname, end=' ')
    if year_of_birth:
        print(f'{year_of_birth} года рождения', end=', ')
    if city:
        print(f'проживает в городе {city}', end=', ')
    if email:
        print(f'email: {email}', end='; ')
    if phone_numb:
        print(f'телефон: {phone_numb}', end=', ')
    print()


define_user(name='Иван', surname='Иванов', year_of_birth='1846')
define_user(name='Иван', city='Москва', email='jackie@gmail.com', phone_numb='01005321456')
define_user(name='Иван', surname='Иванов')
