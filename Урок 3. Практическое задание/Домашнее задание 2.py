# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
def per_data(firstname, lastname, year_, city, email, phone):
    return print(f'Имя: {firstname} Фамилия: {lastname} Год рождения: {year_}'
                 f' Город проживания: {city} Email: {email} Телефон: {phone}')


per_data(
    firstname=input('Имя: '),
    lastname=input('Фамилия: '),
    year_=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('Телефон: '),
)
