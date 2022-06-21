"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def main(**kwargs):
    return f"{kwargs['f_name']} {kwargs['l_name']} " \
           f"({kwargs['year']}), {kwargs['city']}, {kwargs['email']}, {kwargs['phone']}"


first_name = input('Имя: ')
last_name = input('Фамилия: ')
birth_year = input('Год: ')
user_city = input('Город: ')
user_email = input('email: ')
user_phone = input('phone: ')

print(
    main(f_name=first_name, l_name=last_name, year=birth_year,
         city=user_city, email=user_email, phone=user_phone)
)
