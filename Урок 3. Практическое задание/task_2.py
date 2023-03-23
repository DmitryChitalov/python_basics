"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_data (name_user, surname_user, year_of_birth_user, city_user, email_user, telephone_user):
    print(f"{name_user} {surname_user} {year_of_birth_user} года рождения, проживает в городе {city_user},\nemail: {email_user}, телефон: {telephone_user}")

user_data(name_user='Николай', surname_user='Мальцев', year_of_birth_user='1991', city_user='Нижний Новгород', email_user='malcev_ns@live.ru', telephone_user='+79876543210')
