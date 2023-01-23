"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def profile(name=None, surname=None, year=None, city=None, email=None, phone=None):
    return f"{name} {surname} {year} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}"


def less2():
    name = input("Введите имя пользователя: ")
    surname = input("Введите фамилию: ")
    year = input("Введите год рождения: ")
    city = input("Введите город проживания: ")
    email = input("Введите электронный адрес почты: ")
    phone = input("Введите номер телефона: ")
    print(profile(year, name, surname, city, email, phone))


if __name__ == '__main__':
    less2()

