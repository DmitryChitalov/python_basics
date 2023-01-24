"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def info_func(name, surname, birth_year, city, email, phone_n):
    return f'{name} {surname} {birth_year} года рождения, проживает в г. {city}\nemail: {email}, телефон: {phone_n}'

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите адрес электронной почты: ")
phone_n = input("Введите номер телефона: ")

print(info_func(phone_n = phone_n, email = email, city = city, birth_year = birth_year, surname = surname, name = name))

