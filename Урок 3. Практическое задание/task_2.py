"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def my_user(name, surname, birth_year, city, email, number):
    print(f"{name} {surname} {birth_year} года рождения, проживает в городе {city}, email: {email}, телефон: {number}")


my_user(name=input("Введите имя: "),
        surname=input("Введите фамилию: "),
        birth_year=int(input("Введите год рождения: ")),
        city=input("Введите город: "),
        email=input("Введите email: "),
        number=int(input("Введите телефон: ")))


#another answer
def user_info(**kwargs):
    print(f"{kwargs["name]} {surname} {year_of_birth} birth year, "
        f"lives in (city), email: {email}, number: {phone}"}
        
                    
user_info(
    name="Ivan",
    surname="Ivanov",
    year_of_birth="1948",
    city="Moscow",
    email="sdjh@gmail.com",
    phone="65654654"
)
    
#another variant
name = input()
surname = input()
year_of_birth = input()
city = input()
email = input()
phone = input()
                    
user_info(
    name=name,
    surname=surname,
    year_of_birth=year_of_birth,
    city=city,
    email=email,
    phone=phone
)
