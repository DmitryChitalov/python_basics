"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def p_d(p_name, p_fn, p_year,  p_city, p_email, p_phone ):
    print(f"{p_name} {p_fn} {p_year} года рождения, проживает в городе {p_city}, {p_email}, {p_phone}")

p_name = input("Имя: ")
p_surname = input("Фамилия: ")
p_year = int(input("Год: "))
p_city = input("Город: ")
p_email = input("email: ")
p_phone = input("Телефон: ")
p_d(p_name, p_surname, p_year, p_city, p_email, p_phone)


