"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def set_user_info(**user):
    print(f"{user['name']} {user['sur_name']} {user['year']} года рождения, проживает в городе {user['city']}, "
          f"email: {user['email']}, телефон: {user['phone']}")


properties = {"name": "имя", "sur_name": "фамилия", "year": "год рождения", "city": "город проживания",
              "email": "email", "phone": "телефон"}

user_info = {}
for key, value in properties.items():
    user_info[key] = input(f"Введите {value}: ")

set_user_info(**user_info)
