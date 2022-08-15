"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def func(name, surname, birth_year, residence_city, email, phone_number):
    print(f"Имя - {name}, Фамилия - {surname}, Год рождения - {birth_year}, "
          f"Город проживания - {residence_city}, email - {email}, Телефонный номер - {phone_number}")
    print(name, surname, birth_year, residence_city, email, phone_number)

print("Введите данные: ")
name = input("Имя: ")
surname = input("Фамилия: ")
birth_year = input("Год рождения: ")
residence_city = input("Город проживания: ")
email = input("email: ")
phone_number = input("Телефонный номер: ")

func(name, surname, birth_year, residence_city, email, phone_number)
