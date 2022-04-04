"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def print_user_info(city, first_name, birth_year, email, phone_num, last_name):
    """
    Функция формирует вывод информации о пользователе в одну строку
    :param first_name: Имя
    :param last_name: Фамилия
    :param birth_year: Год рождения
    :param city: Город проживания
    :param email: Адрес электронной почты
    :param phone_num: Номер телефона
    :return: Вывод информации в одной строке.
    """
    info_str = "{0} {1} {2} года рождения, проживает в городе {3}, email: {4}, телефон: {5}".format(str(first_name),
                                                str(last_name),
                                                str(birth_year),
                                                str(city),
                                                str(email),
                                                str(phone_num))
    return info_str


print(print_user_info(birth_year="1846", city="Москва", email="jackie@gmail.com", phone_num="01005321456",
                      first_name="Иван", last_name="Иванов"))
