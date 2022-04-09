"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def print_user(firstname, lastname, year_of_birth, city, email, mobilephone):
    """
        Функция выводящая данные пользователя

        :param firstname: имя пользователя
        :param lastname: фамилия пользователя
        :param year_of_birth: год рождения пользователя
        :param city: город пользователя
        :param email: email пользователя
        :param mobilephone: номер телефона пользователя
    """

    print(f"{lastname} {firstname} born in {year_of_birth}, lives in city {city}, email - {email}, mobilephone - {mobilephone}")


input_firstname = input("Input person firstname: ")
input_lastname = input("Input person lastname: ")
input_birhdate = input("input person birthdate like dd.MM.yyyy: ")
input_city = input("Input person city of residence: ")
input_email = input("Input person email: ")
input_mobilephone = input("Input person mobilephone: ")

year_of_birth = input_birhdate[-4:]

print_user(firstname=input_firstname, lastname=input_lastname, year_of_birth=year_of_birth, city=input_city, email=input_email, mobilephone=input_mobilephone)