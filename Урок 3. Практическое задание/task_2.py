"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_data(user_name, **user_param):
    print(f"Пользователь: {user_name}, г.р.: {uprmtr_year}, "
          f"проживает в городе {uprmtr_city}, имейл: {uprmtr_email}, "
          f"номер телефона: {uprmtr_phone}")
    print(user_param)


u_name = input("Введите Фамилию, Имя: ")
uprmtr_year = int(input("Введите год рождения: "))
uprmtr_city = input("Введите город проживания: ")
uprmtr_email = input("Введите имейл: ")
uprmtr_phone = int(input("Введите номер телефона: "))

user_data(u_name, year=uprmtr_year, city=uprmtr_city,
          email=uprmtr_email, phone=uprmtr_phone)
