"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def _humandata_(v_name, v_surname, vb_date, v_town, v_email, v_phone):
    print(f'Пользователь {v_name} {v_surname} {vb_date} года рождения, проживает '
          f'в городе {v_town}, email: {v_email}, телефон: {v_phone}')

usr_name = input('Введите имя пользователя: ')
usr_surname = input('Введите фамилию пользователя: ')
usr_bdate = input('Введите дату рождения: ')
usr_town = input('Введите город проживания: ')
usr_email = input('Введите email пользователя: ')
usr_phone = input('Введите номер телефона пользователя: ')
_humandata_(v_name=usr_name, v_surname=usr_surname, vb_date=usr_bdate,
            v_town=usr_town, v_email=usr_email, v_phone=usr_phone)
