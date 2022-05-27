"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def inf_func(name, surname, year, city, email, number):
    print(f'{name} {surname} {year} года рождения, проживает в городе {city} '
          f'email: {email}, телефон: {number}')



name = input('Enter your name')
surname = input('Enter surname')
year = input('Enter your year ')
city = input('Enter your city')
email = input('Enter email')
number = input('Enter number')

print(inf_func(name, surname, year, city, email, number))