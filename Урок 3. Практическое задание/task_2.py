"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_data(name, surname, birth_year, user_city, user_email, phone):
    """
    Print user data in one line
    :param name: User name
    :param surname: User surname
    :param birth_year: User's birth year
    :param user_city: User's city
    :param user_email: User's email
    :param phone: User's phone
    :return: Formatted string with user data
    """
    print(
        f"{name} {surname} born in {birth_year} lives in {user_city}"
        f"email : {user_email} phone : {phone}"
    )


user_data(
    name=input("Please enter user name : "),
    surname=input("Please enter user surname : "),
    birth_year=input("Please enter user birth year : "),
    user_city=input("Please enter city : "),
    user_email=input("Please enter user email : "),
    phone=input("Please enter user phone number : "),
)
