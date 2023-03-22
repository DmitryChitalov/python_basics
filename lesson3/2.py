"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def main(first_name: str = None,
         last_name: str = None,
         year: int = None,
         city: str = None,
         phone: str = None,
         email: str = None):
    return f"{first_name} {last_name} ({year}), {city}, {phone}, {email}"

print("Введите ваши данные:")

user_first_name = input("Имя >>> ")
user_last_name = input("Фамилия >>> ")
user_year = int(input("Год рождения >>> "))
user_city = input("Город >>> ")
user_email = input("Email >>> ")
user_phone = input("Номер телефона >>> ")

print("Проверьте ваши данные:")
print(
    main(first_name=user_first_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)