"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
#3.2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения,  город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой

def func_my_user(first_name='', last_name='', birth_year='', city='', email='', telephone=''):

    if first_name:
        print('Имя:', first_name, end='; ')

    if last_name:
        print('Фамилия:', last_name, end='; ')

    if birth_year:
        print('Год рождения:', birth_year, end='; ')

    if city:
        print('Город проживания:', city, end='; ')

    if email:
        print('e-mail:', email, end='; ')

    if telephone:
        print('№ телефона:', telephone, end='; ')

    print('\n')

func_my_user(first_name='Max', last_name='Pavlov', birth_year='1983' , city='KRD', email='assa@gmail.com', telephone='898-888-8988-88')
