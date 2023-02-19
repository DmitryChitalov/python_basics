"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def print_user(**p):
    print(f"{p['name']} {p['surname']}, {p['year_of_birth']} goda rozhdenija, "
          f"prozhivajushij v {p['city']}, e-mail: {p['email']}, "
          f"phone: {p['phone']}")

print_user(
    name="Vasja",
    surname="Pupkin",
    year_of_birth="1988",
    city="Moscow",
    email="vassa@mail.ru",
    phone="911"
)
