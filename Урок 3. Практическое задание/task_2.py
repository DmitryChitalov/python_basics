"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
 email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_data(first_name, last_name, year_of_birth, city, email, phone):
    """
    Принимает данные о пользователе и выводит их в стандартный поток вывода

    :param first_name: имя
    :param last_name: фамилия
    :param year_of_birth: год рождения
    :param city: город проживания
    :param email: электронная почта
    :param phone: телефон
    :return:
    """
    print(f"{first_name} {last_name} {year_of_birth} года рождения, проживает "
          f"в городе {city}, email: {email}, телефон: {phone}")


user_data(first_name="Петр", last_name="Сидоров", year_of_birth=1981,
          city="Таганрог", email="petr.sidorov@mail.com", phone="8077332211")
