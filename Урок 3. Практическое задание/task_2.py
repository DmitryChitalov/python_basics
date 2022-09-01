"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def information_func(name, surname, birth_year, city, email, phone):
    print(f"{name}, {surname}, {birth_year}, {city}, {email}, {phone}")


information_func(name='Ivan', surname='Ivanov', birth_year=2000, city='Msc', email='randomemail@mail.ru', phone='77777777777')
