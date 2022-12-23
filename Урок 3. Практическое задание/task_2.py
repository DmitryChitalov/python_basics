"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
name = input('имя')
surname = input('фамилия')
year = int(input('год рождения'))
city = input('город проживания')
email = input('email')
telephone = int(input('телефон'))


def card(name, surname, year, city, email, telephone):
    return (f'{name} {surname} {year} {city} {email} {telephone}')


print(card(name, surname, year, city, email, telephone))
