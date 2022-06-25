"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def user_data(name, lastname, patronymic, year_of_birth, city, email, phone):
    return print(f"{lastname} {name} {patronymic}, {year_of_birth} года рождения, проживает в городе {city}. \n"
          f"Контактные данные: email: {email}, телефон: {phone}")


user_data(
    lastname = input('Фамилия: '),
    name = input('Имя: '),
    patronymic = input('Отчество: '),
    year_of_birth = input('Год Рождения: '),
    city = input('Город проживания: '),
    email = input('email: '),
    phone = input('phone: '),
)