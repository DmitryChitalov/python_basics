"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
name = 'Иван'
surname = 'Иванов'
year_of_birth = 1846
city = 'Москва'
email = 'jackie@gmail.com'
tel = '01005321456'
def my_func (name, surname, year_of_birth, city, email, tel):
    final_str = f'{name} {surname} {year_of_birth} года рождения, проживает' \
                f'в городе {city}, email: {email}, телефон: {tel}'
    return final_str

print(my_func(name, surname, year_of_birth, city, email, tel))
