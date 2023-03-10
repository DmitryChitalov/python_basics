"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
name2 = str(input("Input name: "))
surname2 = str(input("Input surname: "))
year2 = str(input("Input year: "))
city2 = str(input("Input city: "))
email2 = str(input("Input email: "))
phone2 = str(input("Input phone: "))

def personal_info(name,surname,year,city,email,phone):
    return ' '.join([
        "name: ", name,
        ". surname: ", surname,
        ". year: ", year,
        ". city: ", city,
        ". email: ", email,
        ". phone: ", phone, "."
        ])

print(personal_info(name=name2, surname=surname2, year=year2, city=city2, email=email2, phone=phone2))
