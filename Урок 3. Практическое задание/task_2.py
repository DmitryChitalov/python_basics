"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def persona(name, familiya, date_of_birth, city, email, telephone):
    return print(f'Имя: {name} Фамилия: {familiya} Год рождения: {date_of_birth} '
                 f'Город проживания: {city} Email: {email} Телефон: {telephone} ')

persona(
    name=input('Имя: '),
    familiya=input('Фамилия: '),
    date_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    telephone=input('phone: '))
