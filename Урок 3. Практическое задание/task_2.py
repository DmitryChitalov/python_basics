"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def user_info(name=None, surname=None, year=None, city=None, email=None, phone=None):
    """ Выводит данные о пользователе """
    print(f'Имя: {name}, Фамилия: {surname}, год рождения: {year}, '
          f'город проживания: {city}, email: {email}, телефон: {phone}')


# Вызов функции
user_name = input("Введите имя пользователя: ")
user_surname = input("Введите фамилию пользователя: ")
user_year = int(input("Введите год рождения пользователя: "))
user_city = input("Введите город проживания пользователя: ")
user_email = input("Введите электронный адрес пользователя: ")
user_phone = input("Введите телефон пользователя: ")
user_info(name=user_name, year=user_year, surname=user_surname, city=user_city, email=user_email, phone=user_phone)
