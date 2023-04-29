"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_info(**user):
    """
    Данная функция выводит информацию о пользователе
    :param user: Параметр args принимает все именные аргументы
    :return: None. Именная функция выводит встроенную функцию print.
    """
    user_lst = []
    for _, elem in user.items():
        user_lst.append(elem)
    return (f'{user_lst[0]} {user_lst[1]}, Год рождения - {user_lst[2]}, Место проживания - {user_lst[3]}, '
            f'Эл.почта - {user_lst[4]}, Телефон - {user_lst[5]}')


first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
brith_year = input('Введите год рождения: ')
city_user = input('Введите город проживания: ')
email_user = input('Введите почту: ')
number_phone = input('Введите номер телефона: ')
print(user_info(name_user=first_name, surname=last_name, brith=brith_year, city=city_user, mail_user=email_user,
                number_user=number_phone))
