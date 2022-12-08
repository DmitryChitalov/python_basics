"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def show_person_info(
    surname: str,
    name: str,
    birth_year: int,
    city: str,
    email: str,
    telephone: str):

    print(surname, name, birth_year, city, email, telephone)

show_person_info(surname="Иванов", name="Иван", birth_year=1998, city="Минск", email="ivanov@mail.ru", telephone="375331234567")