"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
name_val = input("Введите имя:")
surname_val = input("Введите фамилию:")
year_val = input("Введите год рождения:")
city_val = input("Введите город проживания:")
mail_val = input("Введите email:")
phone_val = input("Введите номер телефона:")
def s_inform(a, b, c, d, e, g):
    print(f"{name_val} {surname_val} {year_val} года рождения, проживает в городе {city_val}, email: {mail_val}, телефон: {phone_val}")
s_inform(a=name_val, b=surname_val, c=year_val, d=city_val, e=mail_val, g=phone_val)
