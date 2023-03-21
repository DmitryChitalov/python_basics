"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_info(**user_features):
    """
    Функция вывода информации о пользователе
    :param user_features: данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
    :return:
    """
    print(f"{user_features['name']} {user_features['surname']} {user_features['year']} года рождения, "
          f"проживает в городе {user_features['city']}, email: {user_features['email']}, телефон: {user_features['phone']}")


user_info(name=input('Введите имя: '), surname=input('Введите фамилию: '), year=input('Введите год рождения: '),
          city=input('Введите город проживания: '), email=input('Введите email: '),
          phone=input('Введите номер телефона: '))
