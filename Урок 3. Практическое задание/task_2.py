"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def info(f_name, l_name, birth, city, email, phone):
    return f_name, l_name, birth, city, email, phone


print(info('d3eded', '3edecd', 'cedced', 'decde', 'cedcedc', 'cdecdece'))

f_name, l_name, birth, city, email, phone = info()
