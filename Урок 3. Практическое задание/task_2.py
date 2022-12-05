"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def card_users(first_name, last_name, year_in, city_live, email, phone):
    """ Функция заполнения сведений о пользователях """
    return f"{first_name} {last_name} {year_in} года рождения, \
проживает в городе {city_live}, email: {email}, телефон: {phone}"


# Пример без функции "input()"
first_name = 'Иван'
last_name = 'Иванов'
year_in = 1997
city_live = "Бамбей"
email = 'goo@gogo.go'
phone = '+73455436789'

print(card_users(first_name, last_name, year_in, city_live, email, phone))
