# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

name = input('Имя: ')
surname = input('Фамилия: ')
year = input('Год рождения: ')
city = input('Город: ')
email = input('Е-мэйл: ')
telephone = input('Телефон: ')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname, name, year, city, email, telephone))
