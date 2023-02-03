"""
2. Выполнить функцию, которая принимает несколько параметров,
 описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def personal_data_function(name, family, year, city, email, phone):
    """
    Функция вовзращает данные пользователя.
    """
    print(f"{city} ; {name} ; {family} ; {phone} ; {email} ; {year}")


personal_data_function(name='Oleg', family='Oblomov', year=60, city='Novgorod', email='yyu @ ya.ru', phone=87676)
