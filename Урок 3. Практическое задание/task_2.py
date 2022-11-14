"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = int(input('Введите год рождения: '))
city = input('Введите название города: ')
email = input('Введите ваш email: ')
phone = input('Введите ваш телефон: ')
def user_data(**kwargs):
    print(f"{kwargs['name']} {surname} {birth_year} года рождения "
          f"проживает в городе {city}, email: {email}, телефон: {phone}")

user_data(
    name = name,
    surname = surname,
    birth_year = birth_year,
    city = city,
    email = email,
    phone = phone
)

