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
user_name = input("Укажите имя: ")
user_surname = input("Укажите фамилию: ")
user_year = int(input("Укажите год рождения: "))
user_city = input("Укажите город проживания: ")
user_email = input("Укажите электронный адрес: ")
user_phone = input("Укажите телефон: ")
user_info(name=user_name, year=user_year, surname=user_surname, city=user_city, email=user_email, phone=user_phone)
