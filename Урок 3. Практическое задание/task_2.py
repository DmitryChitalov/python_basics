"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_user_info(name, lastname, year_birth, city, email, phone):
    print(f"{name} {lastname}, {year_birth} года рождения. Проживает в городе {city}. E-mail:{email}, телефон:{phone}.")
    return


s_name = input("Имя пользователя:")
s_lastname = input("Фамилия пользователя:")
s_year = input("Год рождения:")
s_city = input("Город проживания:")
s_email = input("Электронная почта:")
s_phone = input("Телефон:")

# намеренно передаю функции параметры не в порядке их следования в объявлении функции, чтобы убедиться, что все работает
print_user_info(name=s_name, lastname=s_lastname, city=s_city, phone=s_phone, email=s_email, year_birth=s_year)
