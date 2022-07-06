"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def func_info(name, surname, year_birth, city, email, phone):
    print(
        f'{name}{surname}{year_birth} года рождения, проживает в городе'
        f'{city},')
    print(f'email:{email}, телефон:{phone}')


user_info = input('Введите имя, фамилия, год рождения, город проживания, '
                  'email, телефон: ').split(',')

func_info(name=user_info[0], surname=user_info[1], year_birth=user_info[2],
          city=user_info[3], email=user_info[4], phone=user_info[5])
