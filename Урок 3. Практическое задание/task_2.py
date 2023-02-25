"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def person_info(name, lastname, year, city, email, phone ):
    print(f'{name} {lastname} {year} года рождения, проживает в городе {city},\n'
          f'email: {email}, телефон: {phone}')

person_info(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year=input('Год рождения: '),
    city=input('Город: '),
    email=input('email: '),
    phone=input('Телефон: ')
)