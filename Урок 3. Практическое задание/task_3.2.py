"""  Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""

user_name1 = input("Введите имя: ")
user_surname1 = input("Введите фамилию: ")
user_year1 = input("Введите год рождения: ")
user_city1 = input("Введите город проживания: ")
user_email1 = input("Введите email: ")
user_phone1 = input("Введите телефонный номер: ")

def my_func(user_name, user_surname, user_year, user_city, user_email, user_phone):
    return user_name, user_surname, user_year, user_city, user_email, user_phone

print(my_func(user_name = user_name1, user_surname = user_surname1, user_year = user_year1, user_city = user_city1, user_email = user_email1, user_phone = user_phone1))


