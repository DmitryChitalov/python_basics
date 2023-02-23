"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def personal_info(**info):
    print(f"{info['name']} {info['lastname']} {info['year_of_birth']} года рождения, "
          f"проживает в городе {info['city_of_residence']}, email: {info['email']}, телефон: {info['phone_number']}")

"""
personal_info(
    name="Иван",
    lastname="Иванов",
    year_of_birth="1846",
    city_of_residence="Москва",
    email="jackie@gmail.com",
    phone_number="01005321456")
    """