"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


<<<<<<< HEAD
def my_funkc(**kwargs):
    """ Ввод персональных данных"""
    f_name = input("Введите ваше имя:")
    l_name = input("Введите вашу фамилию:")
    birthday = input("Введите ваш ДР:")
    city = input("Введите ваш город:")
    email = input("Введите ваш email:")
    phone = input("Введите ваш номер телефона:")
    print(f"{f_name} {l_name} {birthday} года рождения, проживает в городе {city} email: {email}, телефон: {phone}")
    return kwargs


print(my_funkc())
=======
def my_funkc(*args):
    """ Ввод персональных данных"""
    print(f"{f_name} {l_name} {birthday} года рождения, проживает в городе {city} email: {email}, телефон: {phone}")


f_name = input("Введите ваше имя:")
l_name = input("Введите вашу фамилию:")
birthday = input("Введите ваш ДР:")
city = input("Введите ваш город:")
email = input("Введите ваш email:")
phone = input("Введите ваш номер телефона:")
my_funkc(f_name, l_name, birthday, city, email, phone)
>>>>>>> Amendments_Homework#1,2,3
