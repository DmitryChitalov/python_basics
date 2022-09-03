"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def user_data(name, lastname, born_year, city, email, cell_phone):
    return print(f"{name} {lastname} {born_year} года рождения,"
                 f" проживает в городе {city}, e-mail: {email}, телефон: {cell_phone}")


user_data(name=input("Имя: "), lastname=input("Фамилия: "), born_year=input("Год Рождения: "),
          city=input("Город проживания: "), email=input("E-Mail: "), cell_phone=input("Телефон: "), )