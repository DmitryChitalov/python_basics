"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def man_info(**kwargs):
    return ' '.join(kwargs.values())


name = input('Введите имя - ')
surname = input('Введите фамилию - ')
birthday = input('Введите год рождения - ')
city = input('Введите город проживания - ')
email = input('Введите email - ')
phone = input('Введите телефон - ')

print(man_info(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))
