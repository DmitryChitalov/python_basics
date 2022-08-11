"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_info(user_name, user_surname, user_year_of_birth, user_city_of_residence, user_email, user_phone):
    return f"{user_name} {user_surname} {user_year_of_birth} года рождения, проживает в городе " \
           f"{user_city_of_residence}, email: {user_email}, телефон: {user_phone}"


print(user_info(user_name := "Ivan",
                user_surname := "Ivanov",
                user_year_of_birth := 1993,
                user_city_of_residence := "Moscow",
                user_email := "ivan@mail.ru",
                user_phone := "+7333456879"))
