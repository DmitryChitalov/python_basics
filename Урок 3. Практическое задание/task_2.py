"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def user_info(name, surname, birth_year, city, email, phone):
    '''Возврат входящих параметров в виде строки'''
    return f'{name} {surname}, {birth_year} года рождения ' \
           f'проживает в городе {city}, e-mail: {email} ' \
           f'телефон {phone}'
user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фамилию: ')
user_city = input('Введите ваш город: ')
try:
    user_year = int(input('Введите год вашего рождения: '))
    user_email = input('Введите ваш e-mail: ')
    user_phone = input('Введите ваш телефон: ')
except ValueError:
    print('Вы ввели не число')
print(user_info(
    name=user_name, surname=user_surname,
    birth_year=user_year, city=user_city,
    email=user_email, phone=user_phone
))
