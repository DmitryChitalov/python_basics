"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def info(name, surname, birth_year, city, email, phone):
    print(f"{name} {surname}, birth_year: {birth_year} in {city}, email: {email}, phone: {phone}")

info(name = "George", surname = "Fuxn", birth_year = 1978, city= "Berlin",
    email = "george_1978__@gmail.com", phone = "9442-70-60-30")

