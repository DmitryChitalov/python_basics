"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def person_data(**info):
    print(f"{info['per_name']} {info['per_s_name']} {info['per_year']} года рождения, "
          f"проживает в городе {info['per_city']}, "
          f"\nemail: {info['per_email']}, телефон: {info['per_phone']}")


inp_name = input("Введите имя: ")
inp_s_name = input("Введите фамилию: ")
inp_year = input("Введите год рождения: ")
inp_city = input("Введите город проживания: ")
inp_email = input("Введите email: ")
inp_phone = input("Введите телефон: ")

person_data(per_name=inp_name,
            per_s_name=inp_s_name,
            per_year=inp_year,
            per_city=inp_city,
            per_email=inp_email,
            per_phone=inp_phone)
