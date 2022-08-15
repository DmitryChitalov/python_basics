"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def display(name, surname, birth_date, city, email, phone):
    return f'{name} {surname} {birth_date} года рождения, ' \
           f'проживает в городе {city}, email: {email}, ' \
           f'телефон: {phone}'


fields = ('имя', 'фамилию', 'год рождения', 'город проживания', 'email', 'телефон')
data = dict()
for field in fields:
    data[field] = input(f'Введите {field}: ')

print(display(name=data['имя'], surname=data['фамилию'], birth_date=data['год рождения'],city=data['город проживания'],
              email=data['email'], phone=data['телефон']))