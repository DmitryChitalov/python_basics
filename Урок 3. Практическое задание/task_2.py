"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_user_data(name, surname, year, city, email, phone):
    return f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, Email: {email}, " \
           f"Телефон: {phone}"


outputString = print_user_data(name="Vladyslav", surname="Nikolaichuk", email="VladNikolaichuk@gmail.com",
                               phone="+380000000", year="1997", city="Ukraine")
print(f"{outputString}")
