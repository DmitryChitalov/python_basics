"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def my_func(name, surname, year_of_birth, city, email, phone):
    print(my_func(name='Ivan', surname='Ivanov', year_of_birth='1846', city='Moscow', email='jackie@gmail.com', phone='01005321456'))

my_func(
    name="Ivan",
    surname="Ivanov",
    year_of_birth="1846",
    city="Moscow",
    email="jackie@gmail.com",
    phone="01005321456"
)

