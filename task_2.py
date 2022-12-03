"""
Задание 2.

Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
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