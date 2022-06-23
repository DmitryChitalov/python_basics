"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def main(name: str = None,
         surname: str = None,
         year: int = None,
         city: str = None,
         phone: str = None,
         email: str = None):
    """информация"""
    return f"{name} {surname} ({year}), {city}, {phone}, {email}"


user_name = input("Имя >>> ")
user_surname = input("Фамилия >>> ")
user_year = int(input("Год рождения >>> "))
user_city = input("Город >>> ")
user_email = input("Email >>> ")
user_phone = input("Номер телефона >>> ")

print(
    main(name=user_name, surname=user_surname,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)
