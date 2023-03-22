"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
# Пользователь вводит свои данные
first_name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
age = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')


# Функция принимает значение введенные пользователем и преобразует их в одну строку
def user_life(name_1, name_2, age_user, town_city, email_add, phone_num):
    return print(f'{name_1} {name_2} {age_user} года рождения, проживает в городе {town_city},\n'
                 f'email: {email_add}, телефон: {phone_num}')


user_life(name_1=first_name, name_2=second_name, age_user=age, town_city=town, email_add=email, phone_num=phone)
