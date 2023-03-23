"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def print_user(first_name, last_name, year_of_birth, city, email, phone_number):
    print(f"{first_name} {last_name} {year_of_birth} года рождения, проживает в городе {city}, email: {email}, телефон: {phone_number}")

name = input("Введите имя: ")
last_name = input("Введите фамилия: ")
year_of_birth = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone_number = input("Введите телефон: ")

print_user(phone_number=phone_number, first_name=name, year_of_birth=year_of_birth, city=city, email=email, last_name=last_name)