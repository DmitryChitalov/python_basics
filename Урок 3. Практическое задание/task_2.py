"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def func_2(name, surname, bday_year, city, email, phone_num):
    print(name, surname, bday_year, city, email, phone_num)


func_2(name='Anastasiia', surname='Gracheva', bday_year=2000, city='Saint-Petersburg',
       email='111@gmail.com', phone_num=777333)
