"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def person_description(**kwargs) -> None:
    print(f'{kwargs["first_name"]} {kwargs["last_name"]} {kwargs["birth_year"]} года рождения, проживает в городе '
          f'{kwargs["residence_city"]}, email:{kwargs["email"]}, телефон: {kwargs["phone_number"]}')


person_description(
    first_name='Иван',
    last_name='Иванов',
    birth_year=1990,
    residence_city='Москва',
    email='qwe@gmail.com',
    phone_number='88005553535'
)
