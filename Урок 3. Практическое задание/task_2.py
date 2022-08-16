"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

name = input("Введите имя пользователя: ")
fam = input("Введите фамилию пользователя: ")
try:
    year = int(input("Введите год рождения: "))
except ValueError:
    print("Некорректный ввод")
    exit(1)
city = input("Введите город: ")
mail = input("Введите e-mail: ")
tel = input("Введите телефон: ")


def user_data(name, fam, year, city, mail, tel):
    #   try:

    #  except ValueError:
    #      print("Некорректный ввод")
    #      return
    year = str(year)
    string1 = name + " " + fam + ", " + year + " года рождения, проживает  в городе: " + city + ", " + mail + ", " + tel
    return string1


print(user_data(name, fam, year, city, mail, tel))
