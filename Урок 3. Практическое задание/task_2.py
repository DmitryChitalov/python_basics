"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def bio(name, surname, year, city, email, phone):
    print(f'Твоё Имя - {name}, Фамилия - {surname}. Ты родился в {year} году,'
          f' живёшь в городе {city}, Email -{email}, сотовый номер {phone} ')


bio(name=input('name - '), surname=input('surname - '), year=int(input('year - ')),
    city=input('city - '), email=input('email - '), phone=int(input('phone - ')))