"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def your_data (your_name, your_lastname, birth_year, your_city, your_email, your_phone):
    return print(your_name, your_lastname, birth_year, your_city, your_email, your_phone)

your_data(
your_name = input('Напишие свое имя'),
your_lastname = input('Напишите свою фамилию'),
birth_year = input('Введите ваш год рождения'),
your_city = input('Укажите город проживания'),
your_email = input('Укажите вашу электронную почту'),
your_phone = input('Укажите ваш номер телефона'),
)
