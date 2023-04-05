"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
name_1 = input("Имя : ")
surname_1 = input("Фамилия : ")
year_of_birth_1 = input("Год рождения : ")
city_of_birth_1 = input("Место рождения: ")
email_1 = input("Е-mail : ")
phone_1 = input("Номер телефона : ")


def print_data(name_2, surname_2, year_of_birth_2, city_of_birth_2, email_2, phone_2):
    print(f"Имя: {name_2}, Фамилия: {surname_2}, Год рождения: {year_of_birth_2}, Место рождения: {city_of_birth_2}, "
          f"Е-mail: {email_2},  Номер телефона: {phone_2}. ")


print_data(name_2=name_1, surname_2=surname_1, year_of_birth_2=year_of_birth_1, city_of_birth_2=city_of_birth_1,
           email_2=email_1, phone_2=phone_1)