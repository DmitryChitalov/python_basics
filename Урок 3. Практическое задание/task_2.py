"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def pers_data(**info):
    print(f"{info['pers_name']} {info['pers_sec_name']} {info['pers_year']} года рождения, "
          f"проживает в городе {info['pers_city']}, "
          f"\nemail: {info['pers_email']}, телефон: {info['pers_phone_number']}")


input_name = input("Введите имя: ")
input_sec_name = input("Введите фамилию: ")
input_year = input("Введите год рождения: ")
input_city = input("Введите город проживания: ")
input_email = input("Введите email: ")
input_phone = input("Введите телефон: ")

pers_data(pers_name=input_name,
            pers_sec_name=input_sec_name,
            pers_year=input_year,
            pers_city=input_city,
            pers_email=input_email,
            pers_phone_number=input_phone)
