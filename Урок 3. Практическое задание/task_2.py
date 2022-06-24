"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

'''Старый вариант'''
'''
def users(name, surname, year, city, email, phone):
    return ' '.join([name, surname, f'{year} года рождения,', f'проживает в городе {city},', f'email: {email},',
                     f'телефон: {phone}'])


print(users(name='Иван', surname='Иванов', year='1846', city='Москва', email='jackie@gmail.com', phone='01005321456'))
'''


'''Новый вариант решения № 1'''
def users(**data):
    tmp = []
    for value in data.values():
        tmp.append(value)
    return f'{tmp[0]} {tmp[1]} {tmp[2]} года рождения, проживает в городе {tmp[3]}, email: {tmp[4]}, ' \
           f'телефон: {tmp[5]}'


print(users(name='Иван', surname='Иванов', year='1846', city='Москва', email='jackie@gmail.com', phone='01005321456'))


'''Новый вариант решения № 2'''
def users(**data):
    return f'{data["name"]} {data["surname"]} {data["year"]} года рождения, проживает в городе {data["city"]}, ' \
           f'email: {data["email"]}, телефон: {data["phone"]}'


print(users(name='Иван', surname='Иванов', year='1846', city='Москва', email='jackie@gmail.com', phone='01005321456'))
