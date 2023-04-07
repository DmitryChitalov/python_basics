"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def people_info():
    firstname = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    born_year = int(input('Введите год рождения: '))
    place = input('Введите город проживания: ')
    e_mail = input('Введите электронную почту: ')
    phone_number = int(input('Введите номер телефона: '))
    return firstname, lastname, born_year, place, e_mail, phone_number
firstname, lastname, born_year, place, e_mail, phone_number = people_info()
print(f"{firstname} {lastname} {born_year} года рождения, проживает в городе {place}, email: {e_mail}, телефон: {phone_number} ")