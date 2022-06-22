"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва, email: jackie@gmail.com, телефон: 01005321456
"""


def user_information(user_name, user_surname, user_birth_year, user_city, user_email, user_phone):
    """
    Возвращает информацию о пользователе в виде единой строки без переносов
    :param user_name: имя пользователя
    :param user_surname: фамилия пользователя
    :param user_birth_year: год рождения пользователя
    :param user_city: город проживания пользователя
    :param user_email: адрес электронной почты пользователя
    :param user_phone: номер телефона пользоватвеля
    :return: <user_name> <user_surname> <user_bitrh_year> года рождения, проживает в городе <user_city>, email: <user_email>, телефон: <user_phone>
    """
    print(f"{user_name} {user_surname} {user_birth_year} года рождения, проживает в городе {user_city}, email: {user_email}, телефон: {user_phone}")


user_information(user_name="Алексей", user_surname="Голубятников", user_city="Москва", user_email="aleks.golubyatnikov@gmail.com", user_phone="+79161447685", user_birth_year="1983")



