"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def id_card(user_name, user_surname, date_birth, user_town, email, user_tel):
    return F'{user_name} {user_surname} {date_birth} года рождения, проживает в городе {user_town} email: {email} телефон: {user_tel}'


user_town = input('Введите город : ')
user_name = input('Введите имя :')
user_surname = input('Введите фамилию :')
date_birth = input('Введите дату рождения :')
email = input('Введите email :')
user_tel = input('Введите телефон :')

print(id_card(user_town=user_town, user_name=user_name, user_surname=user_surname, date_birth=date_birth, email=email,
              user_tel=user_tel))

print(id_card(user_town='Москва', user_name='Иван', user_surname='Иванов', date_birth=1988, email='qaz@ws.ru',
              user_tel='+79991112233'))
