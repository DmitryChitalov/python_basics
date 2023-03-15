"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
name = input('enter name ')
surname = input('enter surname ')
year = int(input('enter year '))
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')

print(name,surname,year, " год рождения "" проживает в городе ",city," email: ",email," телефон ",telephone) 
